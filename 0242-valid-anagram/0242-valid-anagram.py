import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freqs = [0]*26
        
        if len(s)!=len(t): return False
        
        for c in s:
            i = ord(c) - ord('a')
            freqs[i] += 1
            
        for c in t:
            i = ord(c) - ord('a')
            freqs[i] -= 1
            if freqs[i]<0: return False
        
        
        return True
             