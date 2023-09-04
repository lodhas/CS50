"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    e_count = 0
    for r in board:
        for c in r:
            if c == EMPTY:
                e_count += 1
    if e_count % 2 == 1:
        return X
    return O


def actions(board):
    a_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                a_set.add((i, j))
    return a_set


def result(board, action):
    new_board = copy.deepcopy(board)
    i, j = action
    print(i, j)
    if board[i][j] is not None:
        raise NameError("Invalid Action")
        return
    new_board[i][j] = player(board)
    print(new_board)
    print(terminal(new_board))
    return new_board


def winner(board):
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X or
            board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O or
          board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    else:
        for i in range(3):
            if (board[0][i] == X and board[1][i] == X and board[2][i] == X or
                    board[i][0] == X and board[i][1] == X and board[i][2] == X):
                return X
            if (board[0][i] == O and board[1][i] == O and board[2][i] == O or
                    board[i][0] == O and board[i][1] == O and board[i][2] == O):
                return O
    return None

def terminal(board):
    if winner(board) is not None or not any(EMPTY in r for r in board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    a_list = list(actions(board))
    vals = []
    for a in a_list:
        vals.append(value(result(board, a)))
    if player(board) == X:
        i = vals.index(max(vals))
    elif player(board) == O:
        i = vals.index(min(vals))
    return a_list[i]


def value(board):
    if terminal(board):
        print(utility(board))
        return utility(board)
    a_set = actions(board)
    print(board, a_set)
    vals =[]
    for b in a_set:
        vals.append(value(result(board, b)))
    if player(board) == O:
        return min(vals)
    elif player(board) == X:
        return max(vals)



