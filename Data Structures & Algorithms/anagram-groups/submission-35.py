
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i, s in enumerate(strs):
            a = str(sorted(s))
            if a in res:
                res[a].append(s)
            else:
                res[a] = [s]
        return list(res.values())
            