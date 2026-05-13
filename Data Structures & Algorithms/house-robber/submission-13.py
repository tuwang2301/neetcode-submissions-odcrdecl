class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        arr = [nums[0], nums[1]]
        for i, n in enumerate(nums[2::]):
            if i == 0:
                arr.append(n + arr[0])
            else:
                print(arr[:-1:])
                arr.append(n + max(arr[:-1:]))

        return max(arr)


