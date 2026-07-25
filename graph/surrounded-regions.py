"""
LeetCode 130. Surrounded Regions

Topic:
- Graph
- DFS
- Grid
- Matrix

Pattern:
- Boundary DFS
- Connected Component
- Reverse Thinking

Idea:
An 'O' cannot be captured if it is connected
to an 'O' on the boundary.

Start DFS from every boundary 'O' and mark
all connected 'O' cells as visited.

After that:

- Visited 'O' cells are safe.
- Unvisited 'O' cells are surrounded.

Change every unvisited 'O' into 'X'.

Remember:

Boundary O

↓

DFS and Mark Visited

↓

Visited O = Safe

↓

Unvisited O = Surrounded

↓

Change Unvisited O to X

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""


class Solution:

    def __init__(self):

        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]

    def isValid(self, row, col, rows, cols):

        return (
            0 <= row < rows
            and 0 <= col < cols
        )

    def dfs(
        self,
        row,
        col,
        visited,
        board,
        rows,
        cols
    ):

        visited[row][col] = True

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
                and board[next_row][next_col] == "O"
                and not visited[next_row][next_col]
            ):

                self.dfs(
                    next_row,
                    next_col,
                    visited,
                    board,
                    rows,
                    cols
                )

    def solve(self, board):

        rows = len(board)
        cols = len(board[0])

        visited = [
            [False] * cols
            for _ in range(rows)
        ]

        # Check the first and last rows.
        for col in range(cols):

            if (
                board[0][col] == "O"
                and not visited[0][col]
            ):
                self.dfs(
                    0,
                    col,
                    visited,
                    board,
                    rows,
                    cols
                )

            if (
                board[rows - 1][col] == "O"
                and not visited[rows - 1][col]
            ):
                self.dfs(
                    rows - 1,
                    col,
                    visited,
                    board,
                    rows,
                    cols
                )

        # Check the first and last columns.
        for row in range(rows):

            if (
                board[row][0] == "O"
                and not visited[row][0]
            ):
                self.dfs(
                    row,
                    0,
                    visited,
                    board,
                    rows,
                    cols
                )

            if (
                board[row][cols - 1] == "O"
                and not visited[row][cols - 1]
            ):
                self.dfs(
                    row,
                    cols - 1,
                    visited,
                    board,
                    rows,
                    cols
                )

        # Capture every surrounded region.
        for row in range(rows):

            for col in range(cols):

                if (
                    board[row][col] == "O"
                    and not visited[row][col]
                ):
                    board[row][col] = "X"


if __name__ == "__main__":

    solution = Solution()

    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]

    solution.solve(board)

    print(board)

    # Output:
    # [
    #   ["X", "X", "X", "X"],
    #   ["X", "X", "X", "X"],
    #   ["X", "X", "X", "X"],
    #   ["X", "O", "X", "X"]
    # ]