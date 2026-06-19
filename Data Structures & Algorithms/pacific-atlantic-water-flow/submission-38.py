class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    (nr, nc) in visited or
                    heights[nr][nc] < heights[r][c]
                ):
                    continue

                dfs(nr, nc, visited)

        # Pacific
        for c in range(COLS):
            dfs(0, c, pacific)

        for r in range(ROWS):
            dfs(r, 0, pacific)

        # Atlantic
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic)

        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic)

        return list(pacific & atlantic)