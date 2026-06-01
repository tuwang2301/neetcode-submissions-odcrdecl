class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])

        r, c = row-1, col
        current = [0,-1]
        res = []
        plus = True

        while True:
            if c == 0:
                return res
            for _ in range(c):
                [current_r, current_c] = current
                target_c = current_c + 1 if plus else current_c - 1
                val = matrix[current_r][target_c]
                res.append(val)
                current = [current_r, target_c]

            if r == 0:
                return res
            for _ in range(r):
                [current_r, current_c] = current
                target_r = current_r + 1 if plus else current_r - 1
                val = matrix[target_r][current_c]
                res.append(val)
                current = [target_r, current_c]

            r = max(r-1, 0)
            c = max(c-1, 0)
            plus = not plus
