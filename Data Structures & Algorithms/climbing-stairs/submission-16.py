class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2

        if n <= 1:
            return 1

        for i in range(n-2):
            one, two = two, one + two

        return two

            