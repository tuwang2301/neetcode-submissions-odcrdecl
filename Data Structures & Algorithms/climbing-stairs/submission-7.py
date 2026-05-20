class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2
        if n == 1: return one

        for i in range(n - 2):
            tmp = two
            two = one + two
            one = tmp

        return two