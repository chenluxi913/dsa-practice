"""
LeetCode 8. String to Integer (atoi)

Topic:
- String

Pattern:
- Simulation

Idea:
Process the string step by step.

1. Skip leading spaces.
2. Determine the sign.
3. Read consecutive digits.
4. Build the integer.
5. Clamp to 32-bit signed integer range.

Remember:

Skip Spaces

↓

Sign

↓

Digits

↓

Clamp

Time Complexity: O(n)

Space Complexity: O(1)
"""


class Solution:

    def myAtoi(self, s: str) -> int:

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        n = len(s)
        index = 0

        # Skip leading spaces
        while index < n and s[index] == " ":
            index += 1

        # Determine sign
        sign = 1

        if index < n and (s[index] == "+" or s[index] == "-"):
            if s[index] == "-":
                sign = -1
            index += 1

        # Read digits
        number = 0

        while index < n and s[index].isdigit():

            digit = ord(s[index]) - ord("0")

            number = number * 10 + digit

            # Clamp to 32-bit range
            if sign * number <= INT_MIN:
                return INT_MIN

            if sign * number >= INT_MAX:
                return INT_MAX

            index += 1

        return sign * number
    
if __name__ == "__main__":
    solution = Solution()
    s = "   -42"
    print(solution.myAtoi(s))  # Output: -42