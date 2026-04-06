class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        _min = float('inf')
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > nums[mid + 1]:
                _min = nums[mid+1]
                break
            elif nums[mid] > nums[0] > nums[-1]:
                l = mid
            elif nums[mid] < nums[-1] < nums[0]:
                r = mid
        
        return _min