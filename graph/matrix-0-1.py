"""
LeetCode 542. 01 Matrix

Topic:
- Graph
- BFS
- Grid
- Matrix

Pattern:
- Multi-Source BFS
- Shortest Distance

Idea:
Treat every cell as a graph node.

Each cell has up to four neighbors:

- Up
- Right
- Down
- Left

We need the shortest distance from every cell
to the nearest 0.

Instead of starting BFS from every 1,
start BFS from every 0 simultaneously.

Each 0 is a BFS source with distance 0.

During BFS:

1. Pop the current cell.
2. Record its distance.
3. Visit all unvisited neighbors.
4. Neighbor distance = current distance + 1.

Because BFS expands level by level,
the first time a cell is visited,
its distance is already the shortest.

Remember:

Add All 0 Cells

↓

Mark All Sources Visited

↓

Multi-Source BFS

↓

Visit Unvisited Neighbors

↓

Neighbor Distance = Parent Distance + 1

Time Complexity: O(m × n)

Space Complexity: O(m × n)
"""

from collections import deque


class Solution:

    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]

    def isValid(self, row, col, rows, cols):

        return (
            0 <= row < rows
            and 0 <= col < cols
        )

    def updateMatrix(self, mat):

        rows = len(mat)
        cols = len(mat[0])

        visited = [
            [0] * cols
            for _ in range(rows)
        ]

        distance = [
            [0] * cols
            for _ in range(rows)
        ]

        queue = deque()

        # Add every 0 cell as a BFS source.
        for row in range(rows):

            for col in range(cols):

                if mat[row][col] == 0:

                    queue.append(
                        ((row, col), 0)
                    )

                    visited[row][col] = 1

        # Multi-source BFS.
        while queue:

            (row, col), steps = queue.popleft()

            distance[row][col] = steps

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
                    and visited[next_row][next_col] == 0
                ):

                    visited[next_row][next_col] = 1

                    queue.append(
                        (
                            (next_row, next_col),
                            steps + 1
                        )
                    )

        return distance


if __name__ == "__main__":

    solution = Solution()

    print(
        solution.updateMatrix(
            [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ]
        )
    )
    # [
    #   [0,0,0],
    #   [0,1,0],
    #   [0,0,0]
    # ]

    print(
        solution.updateMatrix(
            [
                [0, 0, 0],
                [0, 1, 0],
                [1, 1, 1]
            ]
        )
    )
    # [
    #   [0,0,0],
    #   [0,1,0],
    #   [1,2,1]
    # ]