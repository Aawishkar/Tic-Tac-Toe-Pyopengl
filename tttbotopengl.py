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
human = "X"
ai = "O"

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

def minimax(board, depth, is_maximizing):
    scores = {ai: 1, human: -1, "draw": 0}
    result = check_winner_minimax()
    if result is not None:
        return scores[result]

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] not in ['X', 'O']:
                board[i] = ai
                score = minimax(board, depth + 1, False)
                board[i] = str(i + 1)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] not in ['X', 'O']:
                board[i] = human
                score = minimax(board, depth + 1, True)
                board[i] = str(i + 1)
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board[i] = ai
            score = minimax(board, 0, False)
            board[i] = str(i + 1)
            if score > best_score:
                best_score = score
                move = i
    return move

def check_winner_minimax():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            return board[condition[0]]
    
    if all(pos in ['X', 'O'] for pos in board):
        return "draw"
    
    return None

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
                draw_board()  # Draw the board immediately after handling a click

        if current_player == ai and not game_over:
            ai_move = best_move()
            if ai_move != -1:
                board[ai_move] = ai
                draw_board()  # Draw the board immediately after AI move
                current_player = human
                check_winner()

        draw_board()  # Draw the board in every iteration to keep it updated

        if game_over:
            draw_board()  # Draw the final state before resetting
            print(f"Game Over! Winner: {winner if winner else 'Draw'}")
            time.sleep(3)
            game_over = False
            winner = None
            current_player = human
            board = [str(i) for i in range(1, 10)]
            draw_board()  # Draw the reset board

if __name__ == "__main__":
    main()

