class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        no_dup_nums = list(set(nums))
        sort = sorted(no_dup_nums)

        if len(nums) == 0: return 0

        max_len = 0
        count = 1

        for i in range(len(sort) - 1):
            if sort[i] == sort[i+1] - 1:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 1

        max_len = max(max_len, count)
        
        return max_len