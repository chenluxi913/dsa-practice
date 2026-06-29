"""
LeetCode 232. Implement Queue using Stacks

Topic:
- Stack
- Queue

Pattern:
- Two Stacks
- Lazy Transfer

Idea:
Use two stacks:

in_stack  -> push elements
out_stack -> pop / peek elements

Only transfer elements from in_stack to out_stack
when out_stack is empty.

Remember:
Push -> in_stack
Pop  -> out_stack

Time Complexity:
push  : O(1)
pop   : Amortized O(1)
peek  : Amortized O(1)
empty : O(1)

Space Complexity: O(n)
"""

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()  # Ensure out_stack has the current elements
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
    
if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())  # Output: 1
    print(queue.pop())   # Output: 1
    print(queue.empty()) # Output: False