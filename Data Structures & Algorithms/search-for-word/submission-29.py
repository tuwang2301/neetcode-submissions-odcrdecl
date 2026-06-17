class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])
        visited = set()

        def dfs(row, col, idx):
            if idx == len(word):
                return True

            if (row not in range(row_len) or col not in range(col_len) or
            (row, col) in visited or
            board[row][col] != word[idx]):
                return False

            visited.add((row,col))
            check = (
                dfs(row + 1, col, idx + 1) or
                dfs(row - 1, col, idx + 1) or
                dfs(row, col + 1, idx + 1) or
                dfs(row, col - 1, idx + 1)
            )
            visited.remove((row,col))

            return check

        for r in range(row_len):
            for c in range(col_len):
                if dfs(r,c,0):
                    return True
        
        return False
