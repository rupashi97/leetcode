import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        track = collections.Counter(magazine)
        
        for r in ransomNote:
            if not track[r]: return False
            track[r] -=1
            
        
        return True