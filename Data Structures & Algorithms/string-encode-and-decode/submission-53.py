class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            count = 0
            for c in s:
                count += 1
            res += str(count) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        print(s)

        countStr = ""
        while i < len(s):
            if s[i] != '#':
                countStr += s[i]
                i += 1
            else:
                i += 1
                count = int(countStr)
                countStr = ""
                res.append(s[i:i+count])

                i += count

        return res
            
