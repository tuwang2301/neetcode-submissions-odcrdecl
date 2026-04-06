class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCheck = [0 for _ in range(26)]
        tCheck = [0 for _ in range(26)]

        for s1 in s:
            sCheck[ord(s1) - ord('a')] += 1
        for t1 in t:
            tCheck[ord(t1) - ord('a')] += 1

        return sCheck == tCheck
        
