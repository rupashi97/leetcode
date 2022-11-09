import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freqs = [0]*26
        freqt = [0]*26
        
        for c in s:
            i = ord(c) - ord('a')
            freqs[i] += 1
            
        for c in t:
            i = ord(c) - ord('a')
            freqt[i] += 1
        
        return freqs == freqt
             