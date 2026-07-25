"""
LeetCode 1020. Number of Enclaves

Topic:
- Graph
- BFS
- Grid
- Matrix

Pattern:
- Multi-Source BFS
- Boundary Traversal
- Connected Components
- Reverse Thinking

Idea:
A land cell is not an enclave if it can reach
the boundary through other land cells.

Instead of checking whether every land cell can escape:

1. Add every boundary land cell to the queue.
2. Start BFS from all boundary land cells simultaneously.
3. Mark all connected land cells as visited.
4. Count the land cells that remain unvisited.

Visited land:
- Can reach the boundary.
- Not an enclave.

Unvisited land:
- Cannot reach the boundary.
- Is an enclave.

Remember:

All Boundary 1s

↓

Add to Queue

↓

Multi-Source BFS

↓

Mark All Reachable Land

↓

Count Unvisited 1s

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from collections import deque


class Solution:

    def __init__(self):

        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, row, col, rows, cols):

        return (
            0 <= row < rows
            and 0 <= col < cols
        )

    def bfs(self, grid, queue, visited):

        rows = len(grid)
        cols = len(grid[0])

        while queue:

            row, col = queue.popleft()

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
                    and grid[next_row][next_col] == 1
                    and not visited[next_row][next_col]
                ):

                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))

    def numEnclaves(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        visited = [
            [False] * cols
            for _ in range(rows)
        ]

        # Add every boundary land cell as a BFS source.
        for row in range(rows):

            for col in range(cols):

                is_boundary = (
                    row == 0
                    or row == rows - 1
                    or col == 0
                    or col == cols - 1
                )

                if is_boundary and grid[row][col] == 1:

                    visited[row][col] = True
                    queue.append((row, col))

        # Mark all land cells connected to the boundary.
        self.bfs(grid, queue, visited)

        enclaves = 0

        # Count land cells that cannot reach the boundary.
        for row in range(rows):

            for col in range(cols):

                if (
                    grid[row][col] == 1
                    and not visited[row][col]
                ):
                    enclaves += 1

        return enclaves


if __name__ == "__main__":

    solution = Solution()

    grid1 = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    print(solution.numEnclaves(grid1))
    # 3

    grid2 = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]

    print(solution.numEnclaves(grid2))
    # 0