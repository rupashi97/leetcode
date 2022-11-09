class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st = ''.join(c for c in s.lower() if c.isalnum())
        
        return st == st[::-1]
        