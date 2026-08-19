"""
LeetCode 120. Triangle

Topic:
- Dynamic Programming
- Array
- Recursion

Pattern:
- Memoization
- Top-Down DP
- Triangle DP

Idea:
Let dp[row][col] represent the minimum path
sum from the current position to the bottom
of the triangle.

From the current position, there are only
two possible moves:

1. Move directly down.

(row + 1, col)

2. Move diagonally down-right.

(row + 1, col + 1)

Choose the path with the smaller sum.

Transition:

dp[row][col] =
triangle[row][col]
+
min(
    dp[row + 1][col],
    dp[row + 1][col + 1]
)

Base Case:

If the current position is already in the
last row, return its value.

If the current state has already been
computed, return the memoized result.

Remember:

Start from the Top

↓

Move Down

or

Move Diagonally Right

↓

Reach the Last Row

↓

Return Current Value

↓

Choose the Smaller Path

↓

Add Current Value

↓

Memoize the Result

Time Complexity: O(n²)
Space Complexity: O(n²)
"""


from typing import List


class Solution:

    # Function to find the minimum
    # path sum recursively.
    def dfs(
        self,
        row,
        col,
        triangle,
        dp
    ):

        # If the result is already
        # computed, return it.
        if dp[row][col] is not None:
            return dp[row][col]

        # Base case:
        # Reach the last row.
        if row == len(triangle) - 1:
            return triangle[row][col]

        # Move directly down.
        down = self.dfs(
            row + 1,
            col,
            triangle,
            dp
        )

        # Move diagonally down-right.
        diagonal = self.dfs(
            row + 1,
            col + 1,
            triangle,
            dp
        )

        # Store the minimum path sum.
        dp[row][col] = (
            triangle[row][col]
            + min(
                down,
                diagonal
            )
        )

        return dp[row][col]

    def minimumTotal(
        self,
        triangle: List[List[int]]
    ) -> int:

        # Create a DP table with the
        # same shape as the triangle.
        dp = [
            [None] * len(row)
            for row in triangle
        ]

        return self.dfs(
            0,
            0,
            triangle,
            dp
        )


if __name__ == "__main__":

    solution = Solution()

    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    print(
        solution.minimumTotal(
            triangle
        )
    )

    # Output:
    # 11