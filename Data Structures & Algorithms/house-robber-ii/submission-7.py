class Solution:
    def rob(self, nums: List[int]) -> int:
            
        def rob_max(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                tmp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = tmp

            return rob2

        if len(nums) < 3:
            return rob_max(nums)

        skip_first = rob_max(nums[1:])
        skip_last = rob_max(nums[:-1])

        return max(skip_first, skip_last)