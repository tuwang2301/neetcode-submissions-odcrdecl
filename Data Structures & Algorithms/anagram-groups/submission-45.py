class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            dic[key].append(s)

        return list(dic.values())