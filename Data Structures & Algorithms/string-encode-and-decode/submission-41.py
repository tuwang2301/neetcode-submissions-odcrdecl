class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            count = 0
            for c in s:
                count += 1
            
            res += str(count) + "#" + s

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        scount = ""
        while i < len(s):
            print(scount)
            if s[i] != "#":
                scount += s[i]
            else:
                count = int(scount)
                string = ""
                for k in range(count):
                    string += s[i + k + 1]

                res.append(string)
                i += count
                scount = ""
            
            i += 1

        return res

