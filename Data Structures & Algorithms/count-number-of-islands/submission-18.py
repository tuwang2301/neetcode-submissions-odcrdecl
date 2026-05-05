class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # BFS
        # rows, cols = len(grid), len(grid[0])
        # islands = 0
        # visit = set()

        # def bfs(r, c):
        #     queue = collections.deque()
        #     queue.append((r, c))
        #     directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        #     while queue:
        #         row, col = queue.popleft()

        #         for dr, dc in directions:
        #             rdr, cdc = row + dr, col + dc

        #             if (rdr in range(rows) and
        #                 cdc in range(cols) and
        #                 grid[rdr][cdc] == "1" and
        #                 (rdr,cdc) not in visit):

        #                 queue.append((rdr, cdc))
        #                 visit.add((rdr, cdc))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visit:
        #             bfs(r,c)
        #             islands += 1

        # return islands

        #DFS
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r > rows - 1 or c > cols - 1 or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count