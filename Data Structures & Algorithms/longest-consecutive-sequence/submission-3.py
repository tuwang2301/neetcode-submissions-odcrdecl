class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        min_n = []
        check = set(nums)

        for n in nums:
            if n-1 not in check:
                min_n.append(n)

        longest = count = 0
        for m in min_n:
            seq = m
            while seq in check:
                count += 1
                seq += 1
            longest = max(longest, count)
            count = 0

        return longest


        