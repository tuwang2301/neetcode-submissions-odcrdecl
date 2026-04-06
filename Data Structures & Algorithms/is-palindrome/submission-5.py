class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = "".join([ch for ch in s if ch.isalnum()]).lower()
        left = 0
        right = len(alphanum) - 1

        while left < right:
            if alphanum[left] != alphanum[right]:
                return False
            left += 1
            right -= 1
        return True