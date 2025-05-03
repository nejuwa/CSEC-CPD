matrix = [[1,2,3],[4,5,6],[7,8,9]]
m = len(matrix)
n = len(matrix[0])
mat = [[0] * m for i in range(n)]

for i in range(m):
    for j in range(n):
        mat[j][m - 1 - i] = matrix[i][j]
for i in range(n):
    for j in range(m):
        matrix[i][j] = mat[i][j]
