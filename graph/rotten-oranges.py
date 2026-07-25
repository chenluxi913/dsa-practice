"""
LeetCode 994. Rotting Oranges

Topic:
- Graph
- BFS
- Grid
- Matrix

Pattern:
- Multi-Source BFS
- Level Order Traversal

Idea:
All initially rotten oranges are BFS sources.

1. Count every orange:
   - fresh oranges
   - rotten oranges

2. Add all initially rotten oranges
   to the queue.

3. Process BFS level by level.

4. Every BFS level represents one minute.

5. When a fresh neighboring orange becomes rotten:
   - Mark it as rotten.
   - Add it to the queue.

During BFS:

count += number of oranges in the current level

At the end:

- If count == total, all oranges became rotten.
- Otherwise, some fresh orange was unreachable.

Remember:

Count All Oranges

↓

Add All Rotten Oranges

↓

Process BFS Level

↓

Rot Fresh Neighbors

↓

Queue Still Has Next Level → Add One Minute

↓

count == total

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""


from collections import deque


class Solution:

    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    def orangesRotting(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        total = 0
        rotten_count = 0
        minutes = 0

        # Count all oranges and add every
        # initially rotten orange to the queue.
        for row in range(rows):

            for col in range(cols):

                if grid[row][col] != 0:
                    total += 1

                if grid[row][col] == 2:
                    queue.append((row, col))

        # Multi-source BFS.
        while queue:

            level_size = len(queue)

            # All oranges in the current queue
            # are rotten at the current minute.
            rotten_count += level_size

            for _ in range(level_size):

                row, col = queue.popleft()

                for row_change, col_change in self.directions:

                    next_row = row + row_change
                    next_col = col + col_change

                    if (
                        self.isValid(
                            next_row,
                            next_col,
                            rows,
                            cols
                        )
                        and grid[next_row][next_col] == 1
                    ):

                        grid[next_row][next_col] = 2

                        queue.append(
                            (next_row, next_col)
                        )

            # The remaining queue contains oranges
            # that will be rotten in the next minute.
            if queue:
                minutes += 1

        if rotten_count == total:
            return minutes

        return -1

    def isValid(self, row, col, rows, cols):

        return (
            0 <= row < rows
            and 0 <= col < cols
        )


if __name__ == "__main__":

    solution = Solution()

    print(
        solution.orangesRotting(
            [
                [2, 1, 1],
                [1, 1, 0],
                [0, 1, 1]
            ]
        )
    )  # 4

    print(
        solution.orangesRotting(
            [
                [2, 1, 1],
                [0, 1, 1],
                [1, 0, 1]
            ]
        )
    )  # -1

    print(
        solution.orangesRotting(
            [
                [0, 2]
            ]
        )
    )  # 0