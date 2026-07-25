"""
LeetCode 200. Number of Islands

Topic:
- Graph
- BFS
- Grid
- Matrix

Pattern:
- Connected Components
- Grid Traversal

Idea:
Treat every land cell as a graph node.

Two land cells belong to the same island only if
they are connected horizontally or vertically.

Traverse every cell in the grid.

When an unvisited land cell is found:

1. A new island has been discovered.
2. Increase the island count.
3. Run BFS from this cell.
4. Mark the entire connected island as visited.

Each BFS traversal processes exactly one island.

Remember:

Find Unvisited Land

↓

Count One Island

↓

BFS the Entire Island

↓

Mark Connected Land Visited

↓

Continue Searching

Time Complexity: O(m * n)

Space Complexity: O(m * n)
"""

from collections import deque


class Solution:

    def __init__(self):

        # Up, right, down, left
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, row, col, rows, cols):

        return (
            0 <= row < rows
            and 0 <= col < cols
        )

    def bfs(self, start_row, start_col, visited, grid):

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Mark the starting land cell as visited.
        visited[start_row][start_col] = True
        queue.append((start_row, start_col))

        while queue:

            row, col = queue.popleft()

            # Traverse the 4 neighbors.
            for direction in range(4):

                next_row = row + self.delRow[direction]
                next_col = col + self.delCol[direction]

                if (
                    self.isValid(
                        next_row,
                        next_col,
                        rows,
                        cols
                    )
                    and grid[next_row][next_col] == "1"
                    and not visited[next_row][next_col]
                ):

                    # Mark visited before adding to the queue
                    # to prevent duplicate queue entries.
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))

    def numIslands(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        visited = [
            [False] * cols
            for _ in range(rows)
        ]

        islands = 0

        # Find every connected component of land.
        for row in range(rows):

            for col in range(cols):

                if (
                    grid[row][col] == "1"
                    and not visited[row][col]
                ):

                    # Found a new island.
                    islands += 1

                    # Visit the entire island.
                    self.bfs(
                        row,
                        col,
                        visited,
                        grid
                    )

        return islands


if __name__ == "__main__":

    solution = Solution()

    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(solution.numIslands(grid1))
    # Expected output: 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(solution.numIslands(grid2))
    # Expected output: 3

    grid3 = [
        ["1", "0"],
        ["0", "1"]
    ]

    print(solution.numIslands(grid3))
    # Expected output: 2