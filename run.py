from random import randint

board = []

for x in range(9):
    board.append(["O"] * 9)


def print_board(board):
    for row in board:
        print((" ").join(row))


print_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)


def game():
    '''Game will start running'''
    for turn in range(10):
        print("Turn"), turn

        """ Validites if player has entered number from 0-8 """
        valid_input = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        valid_row = False
        while not valid_row:
            try:
                guess_row = int(input("Guess Row (0-8):"))
                while guess_row not in valid_input:
                    print("Invalid Input. Please enter a number between 0-8")
                    valid_row = True
            except ValueError as error:
                print("Invalid Input. Please enter a number between 0-8")
                break

        valid_col = False
        while not valid_col:
            try:
                guess_col = int(input("Guess Col (0 - 8):"))
                while guess_col not in valid_input:
                    print("Invalid Input. Please enter a number between 0-8")
                    valid_col = True
            except ValueError as error:
                print("Invalid Input. Please enter a number between 0-8")
                break

            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sunk my battleship!")
                break

            if(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.")
            else:
                (board[guess_row][guess_col] == "X")
                print("You missed my battleship!")
                break

    while True:
        answer = input("Do you want to play again?")
        if answer == 'yes':
            game()
        elif answer == 'no':
            break
        else:
            print("Do not understand. Please type 'yes' or 'no'")


""" Player's turn """


def game_turn():
    if turn == 9:
        print("Game Over")
        turn = + 1
        print_board(board)


def main():
    print("WELCOME TO BATTLESHIP GAME!")
    print("You have 8 turns to try and sink my ship 😈")
    game()
    game_turn()


main()
