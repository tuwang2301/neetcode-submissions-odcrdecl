class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in dic:
                dic.get(sortedS).append(s)
            else:
                dic[sortedS] = [s]
        
        res = []
        for a in dic.values():
            res.append(a)

        return res