class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        stack = []   
        op = { 
            "+" : (lambda x,y: x+y),
            "-" : (lambda x,y: x-y),
            "*" : (lambda x,y: x*y),
            "/" : (lambda x,y: int(x/y))            
        }
        
        
        for t in tokens:
            if t not in op:
                stack.append(t)
                
            else:
                b = stack.pop()
                a = stack.pop()
                res = op[t](int(a),int(b))
                stack.append(res)
                       
        return stack.pop()
                   