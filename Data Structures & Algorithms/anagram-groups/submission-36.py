
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i, s in enumerate(strs):
            a = str(sorted(s))
            res[a].append(s)
     
        return list(res.values())
            