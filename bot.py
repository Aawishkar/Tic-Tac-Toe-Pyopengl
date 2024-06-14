import sys
import random
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Global Game Variables
screen_option = 0
mouse_x, mouse_y, Win_x, Win_y, object_select = 0, 0, 0, 0, 0
view_state = 0
spin = 0
spinboxes = 0
win = 0
player, computer = -1, 1
start_game = 0
Cylinder = None
box_map = [0] * 9
object_map = [[-6, 6], [0, 6], [6, 6], [-6, 0], [0, 0], [6, 0], [-6, -6], [0, -6], [6, -6]]
box = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

# Initializing the game
def init_game():
    global box_map, win, start_game
    box_map = [0] * 9
    win = 0
    start_game = 1

# Checking for three in a row/column/diagonal
def check_move():
    global spinboxes
    for i in range(8):
        t = box_map[box[i][0]] + box_map[box[i][1]] + box_map[box[i][2]]
        if t == 3 or t == -3:
            spinboxes = i
            return 1
    t = sum([abs(box_map[box[i][j]]) for i in range(8) for j in range(3)])
    if t == 24:
        return 2
    return 0

# Blocking or winning move for the computer
def blocking_win():
    for i in range(8):
        t = box_map[box[i][0]] + box_map[box[i][1]] + box_map[box[i][2]]
        if t == 2 or t == -2:
            for j in range(3):
                if box_map[box[i][j]] == 0:
                    box_map[box[i][j]] = computer
                    return 1
    return 0

# Checking for a free corner
def check_corner():
    for i in [0, 2, 6, 8]:
        if box_map[i] == 0:
            box_map[i] = computer
            return 1
    return 0

# Checking for a free row
def check_row():
    if box_map[4] == 0:
        box_map[4] = computer
        return 1
    for i in [1, 3, 5, 7]:
        if box_map[i] == 0:
            box_map[i] = computer
            return 1
    return 0

# Computer's turn logic
def computer_move():
    if blocking_win() == 1:
        return 1
    if check_corner() == 1:
        return 1
    if check_row() == 1:
        return 1
    return 0

# Drawing text on the screen
def Sprint(x, y, st):
    glRasterPos2i(x, y)
    for c in st:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))

# Time event to update the spin
def TimeEvent(te):
    global spin
    spin = (spin + 1) % 360
    glutPostRedisplay()
    glutTimerFunc(8, TimeEvent, 1)

# Initializing OpenGL
def init():
    global Cylinder
    glClearColor(0.082, 0.125, 0.169, 0.0)
    start_game = 0
    win = 0
    Cylinder = gluNewQuadric()
    gluQuadricDrawStyle(Cylinder, GLU_FILL)
    gluQuadricNormals(Cylinder, GLU_SMOOTH)
    gluQuadricOrientation(Cylinder, GLU_OUTSIDE)

# Drawing 'O'
def Draw_O(x, y, z, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(a, 0, 1, 0)
    glutSolidTorus(0.5, 2.0, 20, 16)
    glPopMatrix()

# Drawing 'X'
def Draw_X(x, y, z, a):
    glPushMatrix()
    glTranslatef(x, y, z)
    glPushMatrix()
    glRotatef(a, 0, 1, 0)
    glRotatef(90, 0, 1, 0)
    glRotatef(45, 1, 0, 0)
    glTranslatef(0, 0, -3)
    gluCylinder(Cylinder, 0.5, 0.5, 6, 16, 16)
    glPopMatrix()
    glPushMatrix()
    glRotatef(a, 1, 0, 0)
    glRotatef(90, 0, 1, 0)
    glRotatef(315, 1, 0, 0)
    glTranslatef(0, 0, -3)
    gluCylinder(Cylinder, 0.5, 0.5, 6, 16, 16)
    glPopMatrix()
    glPopMatrix()

# Display function to draw the screen
def display():
    global screen_option, win, view_state, spinboxes

    if screen_option == 3:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(0.0, 1.0, 0.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-9.0, 9.0, -9.0, 9.0, 0.0, 30.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glDisable(GL_COLOR_MATERIAL)
        glColor3f(1.0, 1.0, 1.0)
        Sprint(-3, -2, "To Start the game, press right button and select start game")
        glutSwapBuffers()
    elif screen_option == 0:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-9.0, 9.0, -9.0, 9.0, 0.0, 30.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glDisable(GL_COLOR_MATERIAL)
        glColor3f(1.0, 1.0, 1.0)
        Sprint(-2, 3,  "TIC - TAC - TOE")
        Sprint(-2, 1,  "A Game created by")
        Sprint(-3, -1, "Vyom Chopra")
        Sprint(2, -1, "101917060")
        Sprint(-3, -2, "Naman Aggarwal")
        Sprint(2, -2, "101917077")
        Sprint(-3, -3, "Ishav Garg")
        Sprint(2, -3, "101917074")
        Sprint(-3, -5, "Right Click to Start the Game")
        glutSwapBuffers()
    else:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-9.0, 9.0, -9.0, 9.0, 0.0, 30.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glDisable(GL_COLOR_MATERIAL)
        glColor3f(1.0, 0.0, 0.0)
        if win == 1:
            Sprint(-2, 1, "Congratulations!! You Won 🙂")
        elif win == -1:
            Sprint(-2, 1, "Computer Won 🙁")
        elif win == 2:
            Sprint(-2, 1, "It's a Tie")

        if view_state == 1:
            glColor3f(1.0, 0.0, 0.0)
            Sprint(-3, 8, "Perspective View")
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(60, 1, 1, 30)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
        else:
            glColor3f(1.0, 0.0, 0.0)
            Sprint(-2, 8, "Ortho View")

        gluLookAt(0, 0, 20, 0, 0, 0, 0, 1, 0)
        
        for ix in range(4):
            glPushMatrix()
            glColor3f(1, 1, 1)
            glBegin(GL_LINES)
            glVertex2i(-9, -9 + ix * 6)
            glVertex2i(9, -9 + ix * 6)
            glEnd()
            glPopMatrix()

        for iy in range(4):
            glPushMatrix()
            glColor3f(1, 1, 1)
            glBegin(GL_LINES)
            glVertex2i(-9 + iy * 6, 9)
            glVertex2i(-9 + iy * 6, -9)
            glEnd()
            glPopMatrix()

        if start_game == 1:
            for i in range(9):
                if box_map[i] == -1:
                    Draw_O(object_map[i][0], object_map[i][1], 0, spin)
                elif box_map[i] == 1:
                    Draw_X(object_map[i][0], object_map[i][1], 0, spin)

        glutSwapBuffers()

# Handling mouse clicks
def mouse(button, state, x, y):
    global screen_option, Win_x, Win_y, mouse_x, mouse_y, object_select, start_game, win
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        screen_option = (screen_option + 1) % 4
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and screen_option == 2 and start_game == 1:
        Win_x = x
        Win_y = y
        mouse_x = int(math.ceil((x - 300) / 66.7))
        mouse_y = int(math.ceil((y - 300) / 66.7))
        object_select = mouse_x + (3 * mouse_y)

        if box_map[object_select] == 0:
            box_map[object_select] = player
            if check_move() == 1:
                win = 1
                start_game = 0
            elif check_move() == 2:
                win = 2
                start_game = 0
            elif computer_move() == 1:
                if check_move() == 1:
                    win = -1
                    start_game = 0
                elif check_move() == 2:
                    win = 2
                    start_game = 0

# Handling keyboard input
def keyboard(key, x, y):
    global screen_option, start_game, win, view_state
    if key == b'v':
        view_state = (view_state + 1) % 2
    if key == b'r':
        screen_option = 0
        start_game = 0
        win = 0
    if key == b's' and screen_option == 2:
        init_game()
    glutPostRedisplay()

# Handling menu
def menu(option):
    global screen_option, view_state
    if option == 1:
        screen_option = 2
        init_game()
    if option == 2:
        view_state = 0
    if option == 3:
        view_state = 1
    if option == 4:
        sys.exit()
    glutPostRedisplay()

# Main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b'Tic Tac Toe')
    init()
    glutDisplayFunc(display)
    glutTimerFunc(10, TimeEvent, 1)
    glutMouseFunc(mouse)
    glutKeyboardFunc(keyboard)
    glutCreateMenu(menu)
    glutAddMenuEntry("Start Game", 1)
    glutAddMenuEntry("Ortho View", 2)
    glutAddMenuEntry("Perspective View", 3)
    glutAddMenuEntry("Quit", 4)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    glutMainLoop()

if __name__ == "__main__":
    main()
