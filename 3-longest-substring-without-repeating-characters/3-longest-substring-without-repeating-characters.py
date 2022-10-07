class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        sub = set()
        maxC = 0
        start = 0
        
        for i in range(len(s)):  # O(n)
            
            while s[i] in sub:  # O(1)
                sub.remove(s[start])
                start+=1
                
            
            sub.add(s[i])
            maxC = max(maxC,i-start+1)  
            
            
        return maxC