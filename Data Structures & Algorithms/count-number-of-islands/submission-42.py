class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])

        count = 0

        def dfs(r, c):
            if grid[r][c] == "0":
                return

            neighbors = [(0,1), (1,0), (0,-1), (-1,0)]

            grid[r][c] = "0"
            for n in neighbors:
                n_r, n_c = r + n[0], c + n[1]
                if n_r in range(row) and n_c in range(col):
                    dfs(n_r, n_c)


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1

        return count
            
            
