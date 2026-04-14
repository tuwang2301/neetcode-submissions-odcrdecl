from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict()
        left = 0
        longest = 0

        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            highest = max(counter.values())

            print(highest, right - left - k + 1)

            while highest < right - left - k + 1:
                counter[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
