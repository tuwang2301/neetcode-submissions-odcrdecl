class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        candidates.sort()

        def com(start, target, path):
            if target == 0:
                self.result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]: continue

                if candidates[i] > target: break

                path.append(candidates[i])
                com(i + 1, target - candidates[i], path)
                path.pop()

        com(0, target, [])

        return self.result