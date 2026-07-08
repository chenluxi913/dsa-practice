"""
LeetCode 402. Remove K Digits

Topic:
- String
- Stack
- Greedy
- Monotonic Stack

Pattern:
- Monotonic Increasing Stack

Idea:
To make the number as small as possible,
remove larger digits before smaller digits.

Use a stack.

For each digit:
while stack top is greater than current digit
and k > 0,
pop the stack.

After processing:
If k is still greater than 0,
remove digits from the end.

Finally:
Remove leading zeros.

Remember:

Bigger Before Smaller
↓

Pop

↓

Build Smallest Number

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for digit in num:

            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        while stack and k > 0:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip("0")

        return result if result else "0"
    
if __name__ == "__main__":
    solution = Solution()
    num = "1432219"
    k = 3
    print(solution.removeKdigits(num, k))  # Output: "1219"