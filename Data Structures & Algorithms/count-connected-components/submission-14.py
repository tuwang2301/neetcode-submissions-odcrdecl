from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        self.count = 0
        def dfs(node):
            if node in visited:
                return False

            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)

            return True

        for i in range(n):
            if dfs(i):
                self.count+=1

        return self.count