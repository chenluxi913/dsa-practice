"""
LeetCode 678. Valid Parenthesis String

Topic:
- Greedy
- String

Pattern:
- Track Minimum and Maximum Open Parentheses

Idea:
The '*' character can represent:

- '('
- ')'
- empty string

Instead of tracking one exact number of
unmatched '(' characters, track a range.

minimum_open:
The minimum possible number of unmatched '('.

maximum_open:
The maximum possible number of unmatched '('.

For each character:

'('
- minimum_open += 1
- maximum_open += 1

')'
- minimum_open -= 1
- maximum_open -= 1

'*'
- minimum_open -= 1
  Treat '*' as ')'.

- maximum_open += 1
  Treat '*' as '('.

If maximum_open becomes negative,
there are too many ')' characters,
so the string is invalid.

If minimum_open becomes negative,
reset it to 0 because '*' can also be
treated as an empty string.

The string is valid only if
minimum_open == 0 at the end.

Remember:

Track Open Parenthesis Range

↓

'(' Increase Both

↓

')' Decrease Both

↓

'*' Expand the Range

↓

Maximum Below Zero → Invalid

↓

Minimum Equals Zero → Valid

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:

    def checkValidString(self, s):

        minimum_open = 0
        maximum_open = 0

        for char in s:

            if char == "(":

                minimum_open += 1
                maximum_open += 1

            elif char == ")":

                minimum_open -= 1
                maximum_open -= 1

            else:

                # Treat '*' as ')'.
                minimum_open -= 1

                # Treat '*' as '('.
                maximum_open += 1

            # Even the maximum possible
            # number of unmatched '(' is negative.
            if maximum_open < 0:
                return False

            # '*' can be treated as empty,
            # so minimum cannot be negative.
            minimum_open = max(
                minimum_open,
                0
            )

        return minimum_open == 0


if __name__ == "__main__":

    solution = Solution()

    print(solution.checkValidString("()"))      # True
    print(solution.checkValidString("(*)"))     # True
    print(solution.checkValidString("(*))"))    # True