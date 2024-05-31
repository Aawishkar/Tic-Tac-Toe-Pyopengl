import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import math

# Initialize global variables
board = [str(i) for i in range(1, 10)]
current_player = "X"
game_over = False
winner = None

def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 300, 0, 300)

def draw_board():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw grid lines
    glColor3f(0, 0, 0)
    glLineWidth(2)
    
    glBegin(GL_LINES)
    glVertex2f(100, 0)
    glVertex2f(100, 300)
    glVertex2f(200, 0)
    glVertex2f(200, 300)
    glVertex2f(0, 100)
    glVertex2f(300, 100)
    glVertex2f(0, 200)
    glVertex2f(300, 200)
    glEnd()

    # Draw X and O
    for i in range(9):
        x = (i % 3) * 100 + 50
        y = 300 - ((i // 3) * 100 + 50)  # Adjusting the y-coordinate
        if board[i] == 'X':
            draw_x(x, y)
        elif board[i] == 'O':
            draw_o(x, y)
    
    pygame.display.flip()

def draw_x(x, y):
    glColor3f(1, 0, 0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(x - 30, y - 30)
    glVertex2f(x + 30, y + 30)
    glVertex2f(x + 30, y - 30)
    glVertex2f(x - 30, y + 30)
    glEnd()

def draw_o(x, y):
    glColor3f(0, 0, 1)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)
    for i in range(100):
        angle = 2 * math.pi * i / 100
        glVertex2f(x + 30 * math.cos(angle), y + 30 * math.sin(angle))
    glEnd()

def check_winner():
    global winner, game_over
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            winner = board[condition[0]]
            game_over = True
            return

    if all(pos in ['X', 'O'] for pos in board):
        game_over = True
        winner = None

def handle_click(pos):
    global current_player
    x, y = pos
    row = y // 100  # Adjusting the row calculation
    col = x // 100
    index = row * 3 + col
    
    if board[index] not in ['X', 'O'] and not game_over:
        board[index] = current_player
        current_player = 'O' if current_player == 'X' else 'X'
        check_winner()

def main():
    pygame.init()
    display = (300, 300)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init()
    global game_over, winner, current_player, board

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(pygame.mouse.get_pos())

        draw_board()

        if game_over:
            print(f"Game Over! Winner: {winner if winner else 'Draw'}")
            time.sleep(3)
            game_over = False
            winner = None
            current_player = "X"
            board = [str(i) for i in range(1, 10)]
            draw_board()

if __name__ == "__main__":
    main()
