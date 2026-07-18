class Solution:
    def rob(self, nums: List[int]) -> int:
        max_list  = [0] * len(nums)
        for i, n in enumerate(nums):
            if i < 2:
                max_list[i] = n

            for j in range(i-1):
                max_list[i] = max(max_list[i], n + max_list[j])

        return max(max_list)