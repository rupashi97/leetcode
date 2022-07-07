class Solution:
    def isValid(self, s: str) -> bool:

        p = {')': '(',
             ']': '[',
             '}': '{'
             }

        stack = []

        if len(s) <= 1:
            return False

        for c in list(s):
            if c not in p.keys():
                stack.append(c)
                continue

            else:
                if len(stack) > 0 and p[c] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True
