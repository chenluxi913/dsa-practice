"""
LeetCode 1091. Shortest Path in Binary Matrix

Topic:
- Graph
- Breadth-First Search
- Matrix
- Shortest Path

Pattern:
- BFS
- 8-Directional Grid Traversal
- Unweighted Shortest Path

Idea:
Treat every cell with value 0 as a node.

Two cells are connected if they are adjacent
in one of the eight possible directions.

Since every move has the same cost,
Breadth-First Search guarantees that the first
time we reach the destination, we have found
the shortest path.

The path length counts the number of visited
cells, so the starting cell has a distance of 1.

Before starting BFS:

- If the starting cell is blocked,
  return -1.

- If the destination cell is blocked,
  return -1.

Use a queue to store:

(distance, row, column)

For every cell removed from the queue:

1. Check whether it is the destination.
2. Traverse all eight neighboring cells.
3. Ignore cells outside the grid.
4. Ignore blocked or visited cells.
5. Mark the cell as visited.
6. Add it to the queue with distance + 1.

If the destination is never reached,
return -1.

Remember:

Check Start and Destination

↓

Add Start Cell to Queue

↓

Process Cells with BFS

↓

Explore Eight Directions

↓

Skip Invalid or Blocked Cells

↓

Mark as Visited

↓

Reach Destination

↓

Return Distance

Time Complexity: O(n²)
Space Complexity: O(n²)
"""


from collections import deque
from typing import List


class Solution:

    # Delta row and column arrays
    # for all eight directions.
    delRow = [
        -1, -1, -1,
         0,      0,
         1,  1,  1
    ]

    delCol = [
        -1, 0, 1,
        -1,    1,
        -1, 0, 1
    ]

    # Function to check whether
    # a cell is inside the grid.
    def isValid(
        self,
        row,
        col,
        n
    ):

        if row < 0 or row >= n:
            return False

        if col < 0 or col >= n:
            return False

        return True

    def shortestPathBinaryMatrix(
        self,
        grid: List[List[int]]
    ) -> int:

        n = len(grid)

        # A clear path cannot exist if
        # the source or destination is blocked.
        if (
            grid[0][0] == 1
            or grid[n - 1][n - 1] == 1
        ):
            return -1

        # Distance matrix.
        dist = [
            [float("inf")] * n
            for _ in range(n)
        ]

        # Distance of the source
        # from itself is one.
        dist[0][0] = 1

        # Queue stores:
        # distance, row, column.
        queue = deque()

        queue.append(
            (1, 0, 0)
        )

        while queue:

            distance, row, col = queue.popleft()

            # Destination reached.
            if (
                row == n - 1
                and col == n - 1
            ):
                return distance

            # Traverse all neighbors.
            for i in range(8):

                newRow = row + self.delRow[i]
                newCol = col + self.delCol[i]

                if (
                    self.isValid(
                        newRow,
                        newCol,
                        n
                    )
                    and grid[newRow][newCol] == 0
                    and distance + 1
                    < dist[newRow][newCol]
                ):

                    # Update the distance.
                    dist[newRow][newCol] = (
                        distance + 1
                    )

                    # Add the neighbor
                    # to the queue.
                    queue.append(
                        (
                            distance + 1,
                            newRow,
                            newCol
                        )
                    )

        # No clear path exists.
        return -1


if __name__ == "__main__":

    solution = Solution()

    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]

    print(
        solution.shortestPathBinaryMatrix(
            grid
        )
    )

    # Output:
    # 4