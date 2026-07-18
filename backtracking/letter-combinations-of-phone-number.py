"""
LeetCode 17. Letter Combinations of a Phone Number

Topic:
- Backtracking
- Recursion
- String

Pattern:
- Choose One Letter for Each Digit

Idea:
Each digit maps to several letters
on a telephone keypad.

Process the digits from left to right.

For each digit:

1. Get all letters mapped to it.
2. Choose one letter.
3. Append it to the current string.
4. Recur to process the next digit.

When all digits have been processed,
the current string is one valid combination.

Strings are immutable in Python, so:

current + letter

creates a new string each time.

No backtracking (pop) is needed.

Remember:

Current Digit

↓

Get Letters

↓

Choose One Letter

↓

Move to Next Digit

↓

Save When All Digits Are Used

Time Complexity: O(4^n × n)
Space Complexity: O(n)

where n is the number of digits.
"""


class Solution:

    def __init__(self):

        self.phone = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]

    def letterCombinations(self, digits):

        if not digits:
            return []

        result = []

        self.backtrack(
            digits,
            0,
            "",
            result
        )

        return result

    def backtrack(
        self,
        digits,
        index,
        current,
        result
    ):

        if index == len(digits):

            result.append(current)
            return

        letters = self.phone[int(digits[index])]

        for letter in letters:

            self.backtrack(
                digits,
                index + 1,
                current + letter,
                result
            )


if __name__ == "__main__":

    solution = Solution()

    print(solution.letterCombinations("23"))

    # Output:
    # [
    #   "ad", "ae", "af",
    #   "bd", "be", "bf",
    #   "cd", "ce", "cf"
    # ]