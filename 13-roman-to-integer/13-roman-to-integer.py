class Solution:
    def romanToInt(self, s: str) -> int:
        
        sub = {'V', 'X', 'L', 'C', 'D', 'M'}
        res = 0
        
        hash_table = {
            
            'I': 1,
            'IV':4, 
            'V': 5, #
            'IX':9,
            'X':10, #
            'XL':40,
            'L':50, #
            'XC':90,
            'C':100, #
            'CD':400,
            'D':500, #
            'CM':900,
            'M':1000 #
        }

        i = len(s)-1 
        while i >=0:
            if s[i] in sub and (s[i-1]+s[i]) in hash_table and i>0:
                    res +=hash_table[s[i-1]+s[i]]
                    i -=2
            else:
                res += hash_table[s[i]]
                i -=1
            
        return res
            