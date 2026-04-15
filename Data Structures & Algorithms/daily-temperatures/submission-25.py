class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[-1], 0)] # -> stack of tuples (temp, index)
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures[::-1]):
            print(temp, index, stack)
            while stack and stack[-1][0] <= temp:
                stack.pop()
            if stack:
                res[index] = index - stack[-1][1]
            stack.append((temp, index))

        return res[::-1]