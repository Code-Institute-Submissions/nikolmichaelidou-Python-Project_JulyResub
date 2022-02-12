from random import randint

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
GUESS_BOARD = [[" "] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2,
                      'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_board(borad):
    print('A B C D E F G H')
    print("===============")
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def create_ships():
    for ship in range(5):
        ship_row, ship_col = randint(0, 7), randint(0, 7)


def get_ship_location():
    pass


def count_hit_ships():
    pass


create_ships()
turns = 10
while turns > 0:
