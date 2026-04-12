class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums) # remove dups
        best = 0

        for n in hashset:
            if n-1 not in hashset: # finding the lowest and start the sequence
                length = 1
                while n + length in hashset:
                    print(length)
                    length += 1
                best = max(best, length)

        return best