class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        res = 1
        
        for i in range(len(s)-1):
            maxl=1
            sub = set({s[i]})
            for j in range(i+1, len(s)):
                if s[j] in sub:
                    break
                sub.add(s[j])
                maxl+=1
                    
            res = max(res, maxl)            
        
        if not s: return 0
        
        return res