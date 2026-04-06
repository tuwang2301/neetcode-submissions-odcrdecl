class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = result = [[] for _ in range(len(nums))]
        dic = {}

        for i, n in enumerate(nums):
            dic[n] = dic.get(n,0) + 1

        for key, value in dic.items():
            result[value-1].append(key)

        res = []

        for r in result[::-1]:
            if len(r) > 0:
                for n in r:
                    res.append(n)
            if len(res) == k:
                        break

        return res
            