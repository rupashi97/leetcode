class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        sub = set()
        l = 0
        maxC = 0
        start = 0
        
        for i in range(len(s)):
            
            while s[i] in sub:
                sub.remove(s[start])
                start+=1
                
            
            sub.add(s[i])
            l = len(sub)
            maxC = max(maxC,l)  
            
            
        return maxC