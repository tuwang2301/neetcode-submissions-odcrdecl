class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        preMap = collections.defaultdict(list)

        for i in range(len(words) - 1):
            first, second = words[i], words[i+1]
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    preMap[second[j]].append(first[j])
                    break

            if len(first) > len(second) and first.startswith(second):
                return ""

        output = []
        visit, cycle = set(), set()

        def dfs(wrd):
            if wrd in cycle:
                return False

            if wrd in visit:
                return True

            cycle.add(wrd)
            for pre in preMap[wrd]:
                if not dfs(pre):
                    return False

            cycle.remove(wrd)
            visit.add(wrd)
            output.append(wrd)
            return True

        combine = set()
        for w in words:
            combine |= set(w)

        for c in combine:
            if not dfs(c):
                return ""

        return "".join(output)
        
