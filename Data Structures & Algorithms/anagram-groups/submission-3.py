class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            target = "".join(sorted(s))
            if target in dic:
                dic.get(target).append(s)
            else:
                dic[target] = [s]

        return [*dic.values()]