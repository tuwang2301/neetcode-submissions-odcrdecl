class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        m = 0
        for i in range(k):
            m = max(nums)
            nums.remove(m)

        return m