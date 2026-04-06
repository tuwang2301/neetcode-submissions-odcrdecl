class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def eat_time_with_k(piles: List[int], k: int) -> int:
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            return time

        res = float('inf')
        while l <= r:
            mid = l + (r - l) // 2
            if eat_time_with_k(piles, mid) > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        
        return res

