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
    for turn in range(10):
        print("Turn"), turn
        guess_row = int(input("Guess Row:"))
        guess_col = int(
            input("Guess Col:"))
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 8) or (guess_col < 0 or guess_col > 8):
                print("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
    print_board(board)               


def game_turn():
    if turn == 9:
        print("Game Over")
        turn = + 1
        print_board(board)


def valid_input(input):
    if guess_col != int(input):
        print("Wrong input. Only use numbers")
    if guess_row != int(input):
        print("Wrong input. Only use numbers")


def main():
    print("WELCOME TO BATTLESHIP GAME!")
    print("You have 8 turns to try and sink my ship 😈")
    game()
    game_turn()


main()
