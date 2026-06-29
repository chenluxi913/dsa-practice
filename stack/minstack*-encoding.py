"""
LeetCode 155. Min Stack (Encoding Solution)

Topic:
- Stack
- Design

Pattern:
- One Stack
- Value Encoding

Idea:
Use one stack and one variable (min_value).

When pushing a new minimum:
Store an encoded value:

encoded = 2 * value - min_value

Update min_value to the new minimum.

When popping:
If the popped value is smaller than min_value,
it is an encoded value.
Recover the previous minimum:

previous_min = 2 * min_value - encoded

Remember:
Normal value  -> value >= min_value
Encoded value -> value < min_value

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
        self.min_value = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_value = val
        elif val < self.min_value:
            # store encoded value
            encoded = 2 * val - self.min_value
            self.stack.append(encoded)
            # update min_value
            self.min_value = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        top_value = self.stack.pop()
        # Recover previous minimum
        if top_value < self.min_value:
            self.min_value = 2 * self.min_value - top_value

    def top(self) -> int:
        top_value = self.stack[-1]
        if top_value < self.min_value:
            return self.min_value
        return top_value

    def getMin(self) -> int:
        return self.min_value
    
if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())  # Output: -3
    min_stack.pop()
    print(min_stack.top())     # Output: 0
    print(min_stack.getMin())  # Output: -2