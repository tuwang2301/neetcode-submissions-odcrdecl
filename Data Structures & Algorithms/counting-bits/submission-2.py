class Solution:
    def countBits(self, n: int) -> List[int]:
        final = []

        for i in range(n+1):
            res = 0
            while i:
                res += 1 if i & 1 else 0
                i >>= 1

            final.append(res)

        return final