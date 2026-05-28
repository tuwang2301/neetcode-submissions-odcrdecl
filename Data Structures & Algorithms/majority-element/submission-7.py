class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        
        for k, v in count.items():
            if v > len(nums) / 2:
                return k

        return 0