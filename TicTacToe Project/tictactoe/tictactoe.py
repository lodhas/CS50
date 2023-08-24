"""
Tic Tac Toe Player
"""

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
    new_board = board
    i, j = action
    if board[i][j] != EMPTY:
        raise NameError("Invalid Action")
        return
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    if board[0][0] == X and board[1][1] == X and board[2][2]:
        
    raise NotImplementedError


def terminal(board):

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
