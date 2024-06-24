# nxn 2D matrix and rotate 90 degrees
# do not allocate a new matrix to do this, rotation should be done in place

def rotate90CW(matrix):
    n = len(matrix)
    
    #first transpose matrix in place
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix [j],[i] = matrix[j][i], matrix[i][j]

    #reverse each row
    for row in matrix:
        row.reverse()
        
