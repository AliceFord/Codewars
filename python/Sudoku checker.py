# A program to check if a sudoku is correct

data = [
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 9, 8, 2, 6, 1, 3, 7, 5],
    [7, 5, 6, 3, 8, 4, 2, 1, 9],
    [6, 4, 3, 1, 5, 8, 7, 9, 2],
    [5, 2, 1, 7, 9, 3, 8, 4, 6],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [2, 1, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 5, 8, 1, 7, 9, 2, 4],
    [8, 7, 9, 6, 4, 2, 1, 5, 3]
]

def done_or_not(board):

    for i in range(len(board[0])):

        rowChecker = 0

        for j in range(len(board[0])):
            rowChecker += board[i][j]

        if rowChecker == 45:
            pass
        else:
            return 'Try again!'

    for i in range(len(board[0])):

        columnChecker = 0

        for j in range(len(board[0])):

            columnChecker += board[j][i]

        if columnChecker == 45:
            pass
        else:
            return 'Try again!'

    for i in range(len(board[0])):

        boxChecker = 0

        for j in range(len(board[0])):

            row = j // 3
            column = i // 3

            boxChecker += board[row*3+ i % 3][column*3+i % 3]

        if boxChecker == 45:
            pass
        else:
            return 'Try again!'


    return 'Finished!'



print(done_or_not(data))