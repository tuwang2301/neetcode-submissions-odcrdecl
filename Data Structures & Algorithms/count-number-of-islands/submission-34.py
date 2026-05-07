class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs

        count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        def bfs(r,c):
            queue = collections.deque()
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                print(row, col)
                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr, dc in directions:
                    rdr, rdc = row + dr, col + dc
                    if (rdr in range(rows) and
                        rdc in range(cols) and
                        grid[rdr][rdc] == "1"):
                        queue.append((rdr, rdc))
                        grid[rdr][rdc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    count += 1

        return count