class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        count = 0
        dic = dict()

        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            while (r - l + 1) - max(dic.values()) > k:
                dic[s[l]] = dic.get(s[l], 0) - 1
                l += 1

            max_len = max(max_len, r-l + 1)
        
        return max_len

        
            
            

