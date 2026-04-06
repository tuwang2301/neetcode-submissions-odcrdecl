class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]
        prefix = suffix = 1
        for i in range(n-1):
            prefix *= nums[i]
            res[i+1] *= prefix

        for i in range(n-1, 0, -1):
            suffix *= nums[i]
            res[i-1] *= suffix

        return res