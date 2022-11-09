# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        b, l = 1, n
        bad = -1
        
        while b<=l:
            m = (b+l)//2
            if isBadVersion(m):
                l = m-1
                bad = m 
            else: b = m+1
        
        return bad