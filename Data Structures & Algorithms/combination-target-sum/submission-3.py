class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []

        def combinationSum (index, target, path):
            if index >= len(nums):
                if target == 0:
                    self.result.append(path[:])
                return

            num = nums[index]
            if num <= target:
                path.append(num)
                combinationSum(index, target - num, path)
                back = path.pop()
            combinationSum(index + 1, target, path)
            
        combinationSum(0, target, [])

        return self.result