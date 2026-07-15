"""
LeetCode 22. Generate Parentheses

Topic:
- Backtracking
- Recursion
- String

Pattern:
- Build Valid Combinations

Idea:
Generate the parentheses string one
character at a time.

Maintain two counters:

- open_count:
  Number of "(" used.

- close_count:
  Number of ")" used.

Rules:

1. Add "(" if open_count < n.

2. Add ")" only if
   close_count < open_count.

3. When both open_count and close_count
   equal n, a valid combination is formed.

The second rule guarantees that
the current string is always valid,
so no invalid strings are generated.

Remember:

Add "("

↓

open_count < n

↓

Add ")"

↓

close_count < open_count

↓

open_count == close_count == n

↓

Save Answer

Time Complexity: O(Cn * n)
Space Complexity: O(n)

where Cn is the nth Catalan number.
"""


class Solution:

    def generateParenthesis(self, n):

        result = []

        self.backtrack(
            0,
            0,
            n,
            "",
            result
        )

        return result

    def backtrack(
        self,
        open_count,
        close_count,
        n,
        current,
        result
    ):

        if open_count == close_count == n:

            result.append(current)
            return

        if open_count < n:

            self.backtrack(
                open_count + 1,
                close_count,
                n,
                current + "(",
                result
            )

        if close_count < open_count:

            self.backtrack(
                open_count,
                close_count + 1,
                n,
                current + ")",
                result
            )


if __name__ == "__main__":

    solution = Solution()

    print(solution.generateParenthesis(3))

    # Output:
    # [
    #   "((()))",
    #   "(()())",
    #   "(())()",
    #   "()(())",
    #   "()()()"
    # ]