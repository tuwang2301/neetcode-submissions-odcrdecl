class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for num, cnt in count.items():
            print(num, cnt)
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i] != []:
                for r in freq[i]:
                    res.append(r)
                    if len(res) == k:
                        return res
        