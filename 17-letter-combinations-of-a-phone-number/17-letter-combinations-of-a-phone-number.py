import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:  return []
        
        combos, letter_list = [], []
        
        mp = { '2': 'abc',
              '3':'def', 
              '4': 'ghi',
              '5':'jkl',
              '6':'mno',
              '7':'pqrs',
              '8':'tuv',
              '9':'wxyz'}
        
        if len(digits)==1: return list(mp[digits])
        
        for d in digits[::-1]: letter_list.append(mp[d])
            
            
        while len(letter_list) > 1:
            l1 = letter_list.pop()
            l2 = letter_list.pop()
            combos = []
            for x in list(l1):
                for y in list(l2):
                    combos.append(x+y)
                    
            letter_list.append(combos)
            
        return letter_list[0]
                    