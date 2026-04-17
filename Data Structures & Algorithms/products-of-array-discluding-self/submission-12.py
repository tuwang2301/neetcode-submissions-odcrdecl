class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        l = len(nums)
        prefix, postfix = [1] * l, [1] * l
        res = [1] * l

        for i in range(l):
            if i != 0:
                pre *= nums[i-1]
            prefix[i] = pre

        for i in range(l-1, -1, -1):
            if i != l-1:
                post *= nums[i+1]
            postfix[i] = post

        for i in range(l):
            res[i] = prefix[i] * postfix[i]

        return res
