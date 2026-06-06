class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def subsequents(index, path):
            if index >= len(nums):
                res.append(path[:])
                return
            
            path.append(nums[index])
            index += 1
            subsequents(index, path)
            path.pop()
            subsequents(index, path)

        subsequents(0, [])
        return res