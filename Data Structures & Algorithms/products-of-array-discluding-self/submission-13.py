class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix, postfix, res = [1] * l, [1] * l, [1] * l

        for i in range(1, l):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(l-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1] 

        for i in range(l):
            res[i] = prefix[i] * postfix[i]

        return res
