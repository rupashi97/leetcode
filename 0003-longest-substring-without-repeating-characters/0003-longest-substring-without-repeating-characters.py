class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        maxlen = 0
        start = 0
        mp = {}
        
        for i in range(len(s)):
            
            if s[i] in mp:
                start = max(mp[s[i]]+1, start)
                
            mp[s[i]]=i
            maxlen = max(maxlen, i-start+1)
       
        return maxlen