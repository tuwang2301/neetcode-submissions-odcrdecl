class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        already = [[False for _ in range(n)] for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if already[r][c]:
                    continue
                check = [(r,c)]

                i, j = r, c
                while True:
                    i, j = j, n - i - 1
                    key = (i, j)
                    if key in check:
                        break
                    check.append(key)

                (tmp_r, tmp_c) = check[-1]
                tmp = matrix[tmp_r][tmp_c]

                while check:
                    l = len(check)
                    (t_row, t_col) = check.pop()
                    (row, col) = check[-1] if l > 1 else (0,0)

                    matrix[t_row][t_col] = matrix[row][col] if l > 1 else tmp
                    already[t_row][t_col] = True
                
