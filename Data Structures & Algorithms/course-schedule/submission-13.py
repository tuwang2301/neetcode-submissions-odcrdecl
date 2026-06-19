from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {}
        for p in prerequisites:
            if p[0] not in preq:
                preq[p[0]] = []
            preq[p[0]].append(p[1])

        def dfs(c, visited):
            if c not in preq:
                return True
            
            if c in visited:

                return False

            visited.add(c)

            for course in preq[c]:
                if not dfs(course, visited):
                    return False
            
            visited.remove(c)
            
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True


        