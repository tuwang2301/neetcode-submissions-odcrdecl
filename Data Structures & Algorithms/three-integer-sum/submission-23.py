class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        sorted_nums = sorted(nums)

        for i, n in enumerate(sorted_nums):
            l, r = i + 1, len(nums) - 1

            while l < r:
                
                if sorted_nums[l] + sorted_nums[r] == -n:
                    s = sorted([n, sorted_nums[l], sorted_nums[r]])
                    if s not in res:
                        res.append(s)
                    l += 1
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] < -n:
                    l += 1
                else:
                    r -= 1

        return list(res)