class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l = 0
        count = 0
        dic = dict()

        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            count = (r - l) - max(dic.values()) + 1
            while count > k:
                dic[s[l]] = dic.get(s[l], 0) - 1
                l += 1
                count = (r - l) - max(dic.values())

            max_len = max(max_len, r-l + 1)
        
        return max_len

        
            
            

