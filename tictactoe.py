import os
import time

# Clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print the board
def print_board(move):
    clear_screen()
    print("     |     |     ")
    print(f"  {move[1]}  |  {move[2]}  |  {move[3]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {move[4]}  |  {move[5]}  |  {move[6]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {move[7]}  |  {move[8]}  |  {move[9]}  ")
    print("     |     |     ")

# Delay function
def delay(t):
    time.sleep(t)

# Check win or draw condition
def win_verification(move):
    if move[1] == move[2] == move[3]:
        return 1
    elif move[4] == move[5] == move[6]:
        return 1
    elif move[7] == move[8] == move[9]:
        return 1
    elif move[1] == move[4] == move[7]:
        return 1
    elif move[2] == move[5] == move[8]:
        return 1
    elif move[3] == move[6] == move[9]:
        return 1
    elif move[1] == move[5] == move[9]:
        return 1
    elif move[3] == move[5] == move[7]:
        return 1
    elif all(isinstance(move[i], str) for i in range(1, 10)):
        return 0
    else:
        return -1

# Function for playing against a friend
def against_friend():
    move = list(range(10))
    player1 = input("* Enter player-1 name: ")
    print(f"{player1}'s symbol is 'X'.\n")
    delay(1.8)
    clear_screen()
    player2 = input("* Enter player-2 name: ")
    print(f"{player2}'s symbol is 'O'.\n")
    delay(1.8)

    player = 1
    mark = ''
    while True:
        print_board(move)
        name = player1 if player % 2 else player2
        choice = int(input(f"{name}, enter the choice: "))
        mark = 'X' if player % 2 else 'O'

        if move[choice] == choice:
            move[choice] = mark
        else:
            print("Invalid option!")
            player -= 1
            input("Press Enter to continue...")

        result = win_verification(move)
        if result != -1:
            break
        player += 1

    print_board(move)
    if result == 1:
        print(f"{name} won!")
    else:
        print("==>Game draw")

    replay = input("Do you want to play again (y/n)? ").lower()
    if replay == 'y':
        main()
    else:
        end_game()

# End game function
def end_game():
    clear_screen()
    print("Thanks for playing.")
    delay(1)
    print("Hope you enjoyed it.")
    delay(1)

def main():
    while True:
        clear_screen()
        print("GAME:\n")
        delay(1)
        print("1. Start Game.")
        print("2. Rules.")
        print("3. I don't want to play. This is boring.")
        delay(1)

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            against_friend()
        elif choice == 2:
            clear_screen()
            print("1. The game is played on a grid that's 3 squares by 3 squares.")
            delay(0.8)
            print("2. You are X, your friend is O or vice versa. Players take turns putting their marks in empty squares.")
            delay(0.8)
            print("3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.")
            delay(0.8)
            print("4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
            delay(3)
            continue
        elif choice == 3:
            end_game()
            break
        else:
            print("##INVALID CHOICE")
            delay(2)

if __name__ == "__main__":
    main()
