"""
LeetCode 1277. Count Square Submatrices with All Ones

Topic:
- Dynamic Programming
- Matrix
- 2D DP
- Tabulation

Pattern:
- Largest Square Ending at Each Cell
- Count All Squares

Idea:
Let:

dp[i][j]

represent the side length of the largest square
of all ones ending at cell (i, j).

First, initialize the first row and first column
because no larger square can be formed there.

For every other cell:

If:

matrix[i][j] == 0

then:

dp[i][j] = 0

because no square of ones can end there.

If:

matrix[i][j] == 1

look at three neighboring cells:

Top:
dp[i - 1][j]

Top-Left:
dp[i - 1][j - 1]

Left:
dp[i][j - 1]

Then:

dp[i][j] =
1 + min(top, top-left, left)

The minimum is used because all three directions
must support the larger square.

If:

dp[i][j] = 3

then three squares end at this cell:

1 x 1
2 x 2
3 x 3

Therefore, the total number of squares is the
sum of all values in the DP table.

Remember:

Initialize First Row

↓

Initialize First Column

↓

matrix[i][j] == 0?

↓

dp[i][j] = 0

Otherwise:

↓

1 + min(Top, Top-Left, Left)

↓

Sum Entire DP Table

Time Complexity: O(n * m)

Space Complexity: O(n * m)
"""


from typing import List


class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        # DP table to store the size of the
        # largest square ending at (i, j).
        dp = [[0] * m for _ in range(n)]

        # Initialize the first row.
        for j in range(m):
            dp[0][j] = matrix[0][j]

        # Initialize the first column.
        for i in range(n):
            dp[i][0] = matrix[i][0]

        # Fill the rest of the DP table.
        for i in range(1, n):

            for j in range(1, m):

                # No square of ones can
                # end at the current cell.
                if matrix[i][j] == 0:
                    dp[i][j] = 0

                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])

        # Sum all values in the DP table.
        total = sum(sum(row) for row in dp)

        return total


if __name__ == "__main__":

    solution = Solution()

    matrix = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]

    print(solution.countSquares(matrix))

    # Output:
    # 15