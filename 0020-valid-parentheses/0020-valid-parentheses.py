class Solution:
    def isValid(self, s: str) -> bool:
        
        bracks = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        openBracs = {'(', '{', '['}
        stack = []
        
        for c in s:
            if c in openBracs:
                stack.append(c)
                continue
            
            if not stack: return False
            openb = stack.pop()
            if bracks[c] != openb: return False
            
        return stack==[]    