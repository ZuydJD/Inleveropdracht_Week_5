import math

pos_infinity = float('inf')
neg_infinity = float('-inf')

# const variables
rows = 4
cols = 4

#Create maakt het spelbord. Bestaat uit een lijst van lijsten
def create():
    list = [[0] * cols for i in range(rows)]
    for r in range(rows):
        for c in range(cols):
            list[r][c] = ' '

    return list

#Show board laat de status van het spelbord zien
def show_board(board):
    for r in board:
        print(str(r))

#Get piece zoekt de gegeven pion "W" of "B"
def get_piece(board, piece):
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == piece:
                return r, c
    return False

#Maakt veranderingen in de posities van het bord. De init_row en init_col zijn de rijen en kolommen waar de pion eerst stond.
#De target row en target col zijn de gekozen rijen en kolommen waar de pion wilt staan.
#De move functie update het spelbord om de veranderingen te reflecteren
def move(board, init_row, init_col, target_row, target_col, piece):
    board[init_row][init_col] = 'X'
    board[target_row][target_col] = piece
    return board

#Evaluate berekent een score voor de huidige status van het spel afhankelijk van de pionnen "W" en "B"
def evaluate(board):
    score = 0
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'W':
                score += 1
            elif board[r][c] == 'B':
                score -= 1
    return score

#Get children maakt een lijst met alle mogelijke zetten dat elk pion kan zetten vanaf de plaats op dat moment
def get_children(board, piece):
    children = []
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == piece:
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if dr == 0 and dc == 0:
                            continue
                        if r+dr < 0 or r+dr >= rows or c+dc < 0 or c+dc >= cols:
                            continue
                        if board[r+dr][c+dc] == ' ':
                            child = [row[:] for row in board]
                            child[r][c] = ' '
                            child[r+dr][c+dc] = piece
                            children.append(child)

    return children

#Game over checkt of het spel over is of niet door het bekijken van de status van het bord
def game_over(board):
    w_row, w_col = get_piece(board, 'W')
    b_row, b_col = get_piece(board, 'B')

    w_moves = get_children(board, 'W')
    b_moves = get_children(board, 'B')

    if not w_moves:
        print("Black wins!")
        return True

    if not b_moves:
        print("White wins!")
        return True

    if w_row == b_row and w_col == b_col:
        print("Black wins!")
        return True

    return False

def minimax(board, depth, max_player):
    if depth == 0 or game_over(board):
        return evaluate(board)

    if max_player:
        max_eval = neg_infinity
        for child in get_children (board, 'W'):
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = pos_infinity
        for child in get_children(board, 'B'):
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

if __name__ == '__main__':
    game_board = create()

    # adding pieces to board
    game_board[0][0] = 'B'
    game_board[3][3] = 'W'

    running = True
    turn = True
    while running:
        show_board(game_board)
        print('\n')

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

                if game_over(game_board):
                    print("Game Over!")
                    running = False
                    break

        # Black's (Agent's) turn
        else:
            best_move = None
            best_score = neg_infinity

            for child in get_children(game_board, 'B'):
                score = minimax(child, 4, False)
                if score > best_score:
                    best_move = child
                    best_score = score


            initial_row, initial_col = get_piece(game_board, 'B')
            target_row, target_col = get_piece(best_move, 'B')
            game_board = move(game_board, initial_row, initial_col, target_row, target_col, 'B')

            turn = True

            if game_over(game_board):
                print("Game Over!")
                running = False
                break








