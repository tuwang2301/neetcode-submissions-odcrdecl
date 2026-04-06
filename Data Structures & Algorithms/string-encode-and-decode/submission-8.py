class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        number = set('1234567890')
        i = 0
        total = ''
        while i < len(s):
            if s[i] in number:
                total += s[i]
                i+=1
                continue

            if s[i-1] in number and s[i] == '#':
                string = ''
                for j in range(int(total)):
                    string += s[j + i + 1]
                res.append(string)
                i+=int(total) + 1
                total = ''

        return res