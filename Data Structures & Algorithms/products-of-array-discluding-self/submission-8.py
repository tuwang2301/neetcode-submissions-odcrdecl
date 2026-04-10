class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [], []
        pre, post = 1, 1
        res = []
        l = len(nums)

        for i in range(l):
            if i > 0:
                pre *= nums[i-1]
            prefix.append(pre)

        for i in range(l - 1, -1, -1):
            if i < l - 1:
                post *= nums[i+1]
            postfix.insert(0, post)

        for i in range(l):
            n = prefix[i] * postfix[i]
            res.append(n)

        return res