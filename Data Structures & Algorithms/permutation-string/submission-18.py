class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False

        valid = [0 for _ in range(26)]
        
        for c in s1:
            valid[ord(c) - ord('a')] += 1

        i = 0
        while i <= len2 - len1:
            check = [0 for _ in range(26)]
            for j in range(len1):
                c = s2[i + j]
                print(c, i, j)
                check[ord(c) - ord('a')] += 1

            if check == valid:
                return True

            i += 1

        return False


            
        
            