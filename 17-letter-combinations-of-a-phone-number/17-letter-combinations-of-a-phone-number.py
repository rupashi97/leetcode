import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        op = []
        ip = []
        
        mp = {
             2: ['a','b','c'],
             3: ['d', 'e', 'f'],
             4: ['g','h','i'],
             5: ['j','k','l'],
             6: ['m','n','o'],
             7: ['p','q','r','s'],
             8: ['t','u','v'],
             9: ['w','x','y','z']
             }
        
        if not digits:  # can combine
            return []
        
        for i in range(len(digits)):
            ip.append(mp[int(digits[i])])
            
        op = itertools.product(*ip) # unpacking list into arg
        op2 = ["".join(x) for x in op]
        return op2