class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        s = []

        for i, t in enumerate(temperatures):
            while s and t > s[-1][1]:
                index, temp = s.pop()
                res[index] = i - index

            s.append((i,t))

        return res