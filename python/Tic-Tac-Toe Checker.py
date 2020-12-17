# A program to check if a board of tic-tac-toe is correct or not

DATA = [[0, 0, 1],
        [0, 1, 2],
        [2, 1, 0]]


def is_solved(board):
    return checkForFinished(board)


def checkForFinished(board):
    for i in range(9):
        if board[2-(i//3)][i%3] == 0:
            return -1
        else:
            pass


print(is_solved(DATA))
