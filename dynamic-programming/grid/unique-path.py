"""
LeetCode 63. Unique Paths II

Topic:
- Dynamic Programming
- Matrix
- Recursion

Pattern:
- Memoization
- Top-Down DP

Idea:
Let dp[row][col] represent the number of
unique paths from the top-left corner to
(row, col).

Starting from the destination cell,
recursively move:

- Up
- Left

Base Cases:

- If the current cell is outside the grid,
  return 0.

- If the current cell is an obstacle,
  return 0.

- If the current cell is the starting cell,
  return 1.

If the current state has already been
computed, return the stored result.

Otherwise,

paths =
paths from above
+
paths from left

Store the result before returning it.

Remember:

Start from Destination

↓

Move Up and Left

↓

Check Boundary

↓

Check Obstacle

↓

Reach Starting Cell

↓

Memoize Result

↓

Return Total Paths

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""


from typing import List


class Solution:

    # Function to count the number
    # of unique paths recursively.
    def dfs(
        self,
        row,
        col,
        obstacleGrid,
        dp
    ):

        # Outside the grid.
        if row < 0 or col < 0:
            return 0

        # Obstacle.
        if obstacleGrid[row][col] == 1:
            return 0

        # Reach the starting cell.
        if row == 0 and col == 0:
            return 1

        # Return the memoized result.
        if dp[row][col] != -1:
            return dp[row][col]

        # Move upward.
        up = self.dfs(
            row - 1,
            col,
            obstacleGrid,
            dp
        )

        # Move left.
        left = self.dfs(
            row,
            col - 1,
            obstacleGrid,
            dp
        )

        # Store the result.
        dp[row][col] = up + left

        return dp[row][col]

    def uniquePathsWithObstacles(
        self,
        obstacleGrid: List[List[int]]
    ) -> int:

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # DP table.
        dp = [
            [-1] * cols
            for _ in range(rows)
        ]

        return self.dfs(
            rows - 1,
            cols - 1,
            obstacleGrid,
            dp
        )


if __name__ == "__main__":

    solution = Solution()

    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    print(
        solution.uniquePathsWithObstacles(
            obstacleGrid
        )
    )

    # Output:
    # 2