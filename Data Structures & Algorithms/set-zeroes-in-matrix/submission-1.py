class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        old_zeros = [[False for _ in range(col)] for _ in range(row)]

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    old_zeros[r][c] = True

        for r in range(row):
            for c in range(col):
                 if matrix[r][c] == 0 and old_zeros[r][c]:
                    for i in range(col):
                        matrix[r][i] = 0

                    for i in range(row):
                        matrix[i][c] = 0