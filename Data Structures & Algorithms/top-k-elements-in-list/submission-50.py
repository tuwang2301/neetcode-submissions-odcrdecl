from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        return sorted(dic, key= lambda x: dic[x], reverse = True )[:k]