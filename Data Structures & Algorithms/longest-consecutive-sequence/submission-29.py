class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxCount = 0

        for n in nums:
            if n - 1 not in hashSet:
                length = 1
                while n + length in hashSet:
                    length += 1
                maxCount = max(length, maxCount)

        return maxCount
                