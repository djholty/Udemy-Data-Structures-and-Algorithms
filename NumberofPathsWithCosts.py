# GIven a 2D array, find the number of paths available
# to get a given cost

def numberOfPaths(twoDarray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoDarray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return numberOfPaths(twoDarray, 0, col-1, cost-twoDarray[row][col])
    elif col == 0:
        return numberOfPaths(twoDarray, row-1, 0, cost-twoDarray[row][col])
    else:
        op1 = numberOfPaths(twoDarray, row, col -1, cost-twoDarray[row][col])
        op2 = numberOfPaths(twoDarray, row -1, col, cost-twoDarray[row][col])
        return op1 + op2

matrix1 = [
    [4,7,1,6],
    [5,7,3,9],
    [3,2,1,2],
    [7,1,6,3],
]

print(numberOfPaths(matrix1, 3,3,25))