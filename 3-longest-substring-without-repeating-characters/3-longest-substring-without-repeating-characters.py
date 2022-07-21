class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        M = 1
        sub = set()
        left = 0
        
        for x in s:          
            if x not in sub:            
                sub.add(x)
                continue
    
            m = len(sub)
            M = max(M,m) 
            
            while x in sub:
                sub.remove(s[left])
                left+=1
                
            sub.add(x)
                
        if not s: return 0
        
        return max(M, len(sub))
    