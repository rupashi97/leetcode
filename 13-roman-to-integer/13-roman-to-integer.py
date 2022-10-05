class Solution:
    def romanToInt(self, s: str) -> int:
 
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

        i = 0
        while i < len(s):
            
            if (i+1) < len(s) and s[i:i+2] in hash_table:
                res += hash_table[s[i:i+2]]
                i+=2
            else:
                res += hash_table[s[i]]
                i+=1
                
        return res   