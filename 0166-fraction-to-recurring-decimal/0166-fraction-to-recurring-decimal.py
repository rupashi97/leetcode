class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        
        prod = numerator * denominator
        sign = '' if prod>=0 else '-'
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        main = sign + str(numerator//denominator) + "."
        
        numerator = numerator%denominator
        
        decimal = ''
        i = 0 
        mp = {numerator: i}
        
        while numerator%denominator:
            
            i = i+1
            numerator = numerator * 10
            res = numerator // denominator
            decimal += str(res)
            
            rem = numerator % denominator
            
            if rem in mp:
                decimal = decimal[:mp[rem]]+"(" + decimal[mp[rem]:]+")"
                return main + decimal
            
            mp[rem] = i
            numerator = rem
            
        out = main+decimal
        return out.strip(".")
            
        