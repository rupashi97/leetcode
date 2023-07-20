class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)
                
        left, right = 0, n-1
        switch = 0
        
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