"""
LeetCode 282. Expression Add Operators

Topic:
- Backtracking
- DFS
- String
- Expression Evaluation

Pattern:
- Split Digits
- Try Every Operator

Idea:
Split the string into different operands.

For every operand:

1. If it is the first number:
   - Start the expression directly.
   - Do not place an operator before it.

2. Otherwise, try:
   - Addition
   - Subtraction
   - Multiplication

Track:

- current_value:
  The value of the entire expression.

- previous_operand:
  The most recent operand added to the expression.

Multiplication Precedence:

For:

1 + 2 * 3

Before multiplication:

current_value = 3
previous_operand = 2

Replace the previous operand with:

previous_operand * current_number

Formula:

current_value
- previous_operand
+ previous_operand * current_number

Leading Zero Rule:

"0" is valid.

"05", "00", and "012" are invalid operands.

Remember:

Choose Operand

↓

First Operand Has No Operator

↓

Try +, -, and *

↓

Track Previous Operand

↓

Correct Multiplication Priority

↓

Save When Entire String Is Used
and Value Equals Target

Time Complexity: O(4^n * n)
Space Complexity: O(n)

where n is the length of num.
"""


class Solution:

    def addOperators(self, num, target):

        result = []

        self.dfs(
            num,
            target,
            0,
            0,
            0,
            "",
            result
        )

        return result

    def dfs(
        self,
        num,
        target,
        index,
        current_value,
        previous_operand,
        expression,
        result
    ):

        if index == len(num):

            if current_value == target:
                result.append(expression)

            return

        for end in range(index, len(num)):

            # Prevent operands with leading zeros.
            if end > index and num[index] == "0":
                break

            current_string = num[index:end + 1]
            current_number = int(current_string)

            # First operand:
            # do not add an operator before it.
            if index == 0:

                self.dfs(
                    num,
                    target,
                    end + 1,
                    current_number,
                    current_number,
                    current_string,
                    result
                )

            else:

                # Addition
                self.dfs(
                    num,
                    target,
                    end + 1,
                    current_value + current_number,
                    current_number,
                    expression + "+" + current_string,
                    result
                )

                # Subtraction
                self.dfs(
                    num,
                    target,
                    end + 1,
                    current_value - current_number,
                    -current_number,
                    expression + "-" + current_string,
                    result
                )

                # Multiplication
                multiplied_operand = (
                    previous_operand * current_number
                )

                self.dfs(
                    num,
                    target,
                    end + 1,
                    current_value
                    - previous_operand
                    + multiplied_operand,
                    multiplied_operand,
                    expression + "*" + current_string,
                    result
                )


if __name__ == "__main__":

    solution = Solution()

    print(solution.addOperators("123", 6))

    # Output:
    # [
    #   "1+2+3",
    #   "1*2*3"
    # ]