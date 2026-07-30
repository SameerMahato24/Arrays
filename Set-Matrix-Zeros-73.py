def setZeroes( matrix):
        r = len(matrix)
        c = len(matrix[0])
        row = [0 for _ in range(r)]
        col = [0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if(matrix[i][j] == 0):
                    row[i] = -1
                    col[j] = -1

        for i in range(r):
            for j in range(c):
                if(row[i] == -1 or col[j] == -1):
                    matrix[i][j] = 0

        return matrix

#Input: 
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(setZeroes( matrix))