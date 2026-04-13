class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l, r = 0, 1

        while l < r <= len(s):
            if len(set(s[l:r])) < len(s[l:r]):
                l += 1
            else:
                print(max(longest, r - l))
                longest = max(longest, r - l)
                r += 1

        return longest
