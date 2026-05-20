class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        check = set(nums)

        for n in nums:
            if n - 1 not in check:
                length = 0
                while n + length in check:
                    length += 1
                longest = max(longest, length)

        return longest