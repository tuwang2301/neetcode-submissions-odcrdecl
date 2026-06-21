from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # graph = defaultdict(list)

        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # visited = set()
        # count = 0
        # def dfs(node):
        #     visited.add(node)
        #     for n in graph[node]:
        #         if n not in visited:
        #             dfs(n)

        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)
        #         count+=1

        # return count

        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            res = n

            while res != par[res]:
                par[n] = par[par[n]]
                res = par[n]

            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p1] < rank[p2]:
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            else:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            
            return 1

        count = n
        for n1, n2 in edges:
            count -= union(n1,n2)
        
        return count

        