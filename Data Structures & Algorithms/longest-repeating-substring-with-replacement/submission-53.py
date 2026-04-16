class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1
            while hash_map and right - left - max(hash_map.values()) + 1> k:
                hash_map[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest