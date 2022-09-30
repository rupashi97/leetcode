class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {'+': (lambda a,b: a+b), 
               '-': (lambda a,b: a-b), 
               '*': (lambda a,b: a*b), 
               '/': (lambda a,b: a/b)
              }
        
        stack = []
        
        for t in tokens:
            if t in ops:
                o2, o1 = stack.pop(), stack.pop()
                res = ops[t](o1,o2)
                stack.append(int(res))
                
            else:
                stack.append(int(t))
                
        
        return stack.pop()
                
                