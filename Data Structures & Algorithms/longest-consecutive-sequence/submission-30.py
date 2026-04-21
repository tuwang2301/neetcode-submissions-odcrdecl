class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in hash_set:
                sequence = 1
                while n + sequence in hash_set:
                    sequence += 1

                longest = max(longest, sequence)

        return longest