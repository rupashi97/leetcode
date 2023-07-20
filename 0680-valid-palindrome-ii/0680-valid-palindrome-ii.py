class Solution:
    def validPalindrome(self, s: str) -> bool:

        left, right, switch = 0, len(s)-1, 0        
        pal = True
        
        while left<=right:
            if s[left] != s[right] and switch==2:
                pal = False
                break
                
            if s[left] != s[right] and switch==1:
                left = l
                right = r-1
                switch+=1
                
            elif s[left] != s[right] and not switch:
                l, r = left, right
                left+=1
                switch+=1
            
            else:
                left+=1
                right-=1
        
        return pal