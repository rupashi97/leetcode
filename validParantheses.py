'''
Using stacks to find valid parentheses string
valid:  () [] {}
invalid: (] , [}, [[
'''

class Solution:
    def isValid(self, s: str) -> bool:

        p = {')': '(', ']': '[', '}': '{'}

        stack = []

        if len(s) <= 1:
            return False

        for c in list(s):
            if c not in p.keys():
                stack.append(c)
            else:
                if stack and p[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack
