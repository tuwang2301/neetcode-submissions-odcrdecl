class Solution:
    def isPalindrome(self, s: str) -> bool:
        filterS = []
        for c in s.lower():
            if c.isalnum():
                filterS.append(c)

        l, r = 0, len(filterS) - 1

        while l < r:
            if filterS[l] != filterS[r]:
                return False
            l += 1
            r -= 1

        return True