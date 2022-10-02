'''
An important invariant of a Stack is that when a new number, which we'll call x, is placed on a Stack, the numbers below it will not change for as long as number x remains on the Stack
'''

class MinStack:

    def __init__(self):
        self.s = []
        self.smin = []
        
    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.smin or val<= self.smin[-1]:
            self.smin.append(val)

    def pop(self) -> None:
        x = self.s.pop()
        if x==self.smin[-1]:
            self.smin.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.smin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()