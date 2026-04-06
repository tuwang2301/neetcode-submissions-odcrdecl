class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0 for _ in range(n)]
        stack = [] #[temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                [temp, index] = stack.pop()
                res[index] = i - index
            
            stack.append([t, i])

        return res


            
            
