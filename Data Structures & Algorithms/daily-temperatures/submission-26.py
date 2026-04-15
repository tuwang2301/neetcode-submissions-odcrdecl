class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                t, i = stack.pop()
                res[i] = index - i

            stack.append((temp, index))
        return res