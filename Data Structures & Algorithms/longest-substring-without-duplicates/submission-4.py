class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        l, r = 0, 0
        check = set()
        while r < len(s):
            if s[r] not in check:
                check.add(s[r])
                r += 1
                max_count = max(max_count, len(check))
            else:
                check.remove(s[l])
                l += 1
            
        return max_count
            
