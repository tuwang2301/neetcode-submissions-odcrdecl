class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxCount = 0

        for n in nums:
            if n - 1 not in hashSet:
                count = 1
                start = n
                while start + 1 in hashSet:
                    count += 1
                    start += 1
                maxCount = max(count, maxCount)

        return maxCount
                