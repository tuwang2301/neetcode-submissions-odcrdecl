from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            sort = str(sorted(s))
            dic[sort].append(s)

        return list(dic.values())