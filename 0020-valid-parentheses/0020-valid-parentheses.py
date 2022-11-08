class Solution:
    def isValid(self, s: str) -> bool:
        
        bracks = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack = []
        
        for c in s:
            
            if c in bracks:
                topelement = stack.pop() if stack else '#'
                if bracks[c] != topelement: return False
            else:  
                stack.append(c)
            
        
        return not stack
            