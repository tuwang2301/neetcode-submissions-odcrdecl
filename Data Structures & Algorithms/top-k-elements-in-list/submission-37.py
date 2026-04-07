import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        c = Counter(nums)

        for num, freq in c.items():
            heapq.heappush(heap, (-freq, num))

        res = []

        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)

        return res