"""
LeetCode 155. Min Stack

Topic:
- Stack
- Design

Pattern:
- Auxiliary Min Stack

Idea:
Use two stacks:

stack     -> stores all values
min_stack -> stores only new minimum values

Push:
If the new value is smaller than or equal to
the current minimum, push it into min_stack.

Pop:
If the popped value equals the current minimum,
pop it from min_stack as well.

Remember:
stack     -> all values
min_stack -> minimum history

Time Complexity:
push   : O(1)
pop    : O(1)
top    : O(1)
getMin : O(1)

Space Complexity: O(n)
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    
if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())  # Output: -3
    min_stack.pop()
    print(min_stack.top())     # Output: 0
    print(min_stack.getMin())  # Output: -2