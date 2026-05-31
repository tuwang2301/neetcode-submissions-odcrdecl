class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        already = [[False for _ in range(n)] for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if already[r][c]:
                    continue
                first_key = (r, c)
                check = [first_key]

                i, j = r, c
                while True:
                    i, j = j, n - i - 1
                    key = (i, j)
                    if key in check:
                        break
                    check.append(key)

                (tmp_r, tmp_c) = check[-1]
                tmp = matrix[tmp_r][tmp_c]
                print(check, )
                while check and len(check) > 1:
                    (t_row, t_col) = check.pop()
                    (row, col) = check[-1]

                    matrix[t_row][t_col] = matrix[row][col]
                    already[t_row][t_col] = True

                (t_row, t_col) = check.pop()
                print((row, col), (t_row, t_col))
                matrix[t_row][t_col] = tmp
                already[t_row][t_col] = True
                
