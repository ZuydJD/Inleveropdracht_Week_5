import math
import pygame

pos_infinity = float('inf')
neg_infinity = float('-inf')

# const variables
rows = 4
cols = 4


def create():
    list = [[0] * cols for i in range(rows)]
    for r in range(rows):
        for c in range(cols):
            list[r][c] = ' '

    return list


def show_board(board):
    for r in board:
        print(str(r))


def get_piece(board, piece):
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == piece:
                return r, c
    return False


def move(board, init_row, init_col, target_row, target_col, piece):
    board[init_row][init_col] = 'X'
    board[target_row][target_col] = piece
    return board


if __name__ == '__main__':
    game_board = create()

    # adding pieces to board
    game_board[0][0] = 'B'
    game_board[3][3] = 'W'

    running = True
    turn = True
    while running:
        show_board(game_board)

        # White's turn
        if turn:
            user_move = True
            while user_move:
                move_input = str(input('Give a coordinate: '))

                try:
                    input_row, input_col = move_input.split(',')
                    input_row = int(input_row)
                    input_col = int(input_col)
                    user_move = False
                except:
                    print('That\'s not the correct format, use for example: 0,0')

            # check if move is valid
            valid_move = True
            if valid_move:
                initial_row, initial_col = get_piece(game_board, 'W')
                game_board = move(game_board, initial_row, initial_col, input_row, input_col, 'W')
                turn = False
        # Black's (Agent's) turn
        else:
            user_move = True
            while user_move:
                move_input = str(input('Give a coordinate: '))

                try:
                    input_row, input_col = move_input.split(',')
                    input_row = int(input_row)
                    input_col = int(input_col)
                    user_move = False
                except:
                    print('That\'s not the correct format, use for example: 0,0')

            # check if move is valid
            valid_move = True
            if valid_move:
                initial_row, initial_col = get_piece(game_board, 'B')
                game_board = move(game_board, initial_row, initial_col, input_row, input_col, 'B')
                turn = False
