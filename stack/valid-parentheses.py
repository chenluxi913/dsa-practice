"""
LeetCode 20. Valid Parentheses

Topic:
- Stack

Pattern:
- Matching Parentheses

Idea:
Use a stack to store opening brackets.

When encountering a closing bracket:
- Check whether the stack is empty.
- Check whether the top of the stack matches.
- If not, return False.

After processing all characters,
the stack must be empty.

Remember:
Open -> Push
Close -> Match & Pop

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs:
                top_element = stack.pop() if stack else '#'
                if pairs[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))        # Output: True
    print(solution.isValid("()[]{}"))    # Output: True
    print(solution.isValid("(]"))        # Output: False
    print(solution.isValid("([)]"))      # Output: False
    print(solution.isValid("{[]}"))      # Output: True