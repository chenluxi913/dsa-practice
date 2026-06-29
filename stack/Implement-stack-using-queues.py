"""
LeetCode 225. Implement Stack using Queues

Topic:
- Queue
- Stack

Pattern:
- Queue Rotation

Idea:
After pushing a new element,
rotate the queue so that the newest element
moves to the front.

This makes the queue behave like a stack.

Time Complexity:
push  : O(n)
pop   : O(1)
top   : O(1)
empty : O(1)

Space Complexity: O(n)
"""

class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
    
if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())  # Output: 2
    print(stack.pop())  # Output: 2
    print(stack.empty())  # Output: False