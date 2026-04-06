class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0

        arr = []

        for right in range(len(s)):
            
            arr.append(s[right])

            while len(arr) > len(set(arr)):
                arr.remove(s[left])
                left += 1

            max_len = max(max_len, len(arr))

        return max_len