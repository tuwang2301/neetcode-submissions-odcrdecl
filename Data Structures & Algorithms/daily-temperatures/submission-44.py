class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                idx = stack.pop()[1]
                results[idx] = i - idx
            
            stack.append((t,i))

        return results