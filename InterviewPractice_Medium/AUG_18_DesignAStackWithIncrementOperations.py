# https://leetcode.com/problems/design-a-stack-with-increment-operation/

"""
Design a Stack with Increment Operations 

Faster Approach: 
https://leetcode.com/problems/design-a-stack-with-increment-operation/discuss/843182/lee215's-solution-with-more-explanation

복습 요 
"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k >= len(self.stack):
            k = len(self.stack)

        for i in range(k):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


# fastest solution, 60ms
class CustomStack1:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stk = []

    def push(self, x: int) -> None:
        if len(self.stk) < self.max_size:
            self.stk.append([x, 0])

    def pop(self) -> int:
        if not self.stk:
            return -1
        if len(self.stk) > 1:
            self.stk[-2][1] += self.stk[-1][1]
        return sum(self.stk.pop())

    def increment(self, k: int, val: int) -> None:
        if not self.stk:
            return
        self.stk[min(len(self.stk)-1, k-1)][1] += val
