class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        sufix = [0 for _ in range(n)]
        prefix = [0 for _ in range(n)]

        print(sufix, prefix)

        highest = 0
        for i, a in enumerate(height):
            highest = max(highest, a)
            sufix[i] = highest

        highest = 0
        for i in range(n - 1, -1, -1):
            highest = max(highest, height[i])
            prefix[i] = highest

        total = 0
        for i, water in enumerate(height):
            total += (min(sufix[i], prefix[i]) - water)

        return total
      

