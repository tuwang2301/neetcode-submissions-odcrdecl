from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sort = tuple(sorted(s))
            res[sort].append(s)

        return list(res.values())