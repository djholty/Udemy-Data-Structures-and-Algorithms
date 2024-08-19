# find the minimum cost pathway in a 2d array from top
#left corner to bottom right
#added a counter for curiosity as to how many times this is called
count = 0
def findMinCost(twoDarray, row, col):
    global count
    count +=1
    if row == -1 or col == -1:
        return float('inf')

    elif row == 0 and col == 0:
        return twoDarray[0][0]
    else:
        
        op1 = findMinCost(twoDarray, row, col-1)
        op2 = findMinCost(twoDarray, row-1, col)
        return twoDarray[row][col] + min(op1, op2)

matrix1 = [
    [4,7,8,6,4,5],
    [6,7,3,9,2,5],
    [3,8,1,2,4,5],
    [7,1,7,3,7,5],
    [2,9,8,9,3,5],
    [2,9,8,9,3,5],
]

matrix2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

matrix3 = [
    [1,2],
    [3,4],
]

# print(findMinCost(matrix1, 5,5))
# print(count)
# count = 0
# print(findMinCost(matrix2, 2,2))
# print(count)
count = 0
print(findMinCost(matrix3, 1,1))
print(count)
