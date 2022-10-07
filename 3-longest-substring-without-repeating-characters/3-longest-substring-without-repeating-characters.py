class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        mp = {}
        maxC = 0
        start = 0
        
        for i in range(len(s)):  # O(n)
            
            if s[i] in mp:  # O(1)
                start = max(mp[s[i]]+1, start)
                            
            mp[s[i]]=i
            maxC = max(maxC,i-start+1)  
            
            
        return maxC