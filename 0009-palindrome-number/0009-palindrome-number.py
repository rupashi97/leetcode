class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        res = []
        
        if x<0: return False
        
        while x:
            d = x%10
            x = x//10
            res.append(d)
        
        return res == res[::-1]
