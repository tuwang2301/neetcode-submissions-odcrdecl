class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)

        return sorted(count, key = lambda x: count[x], reverse = True)[:k]