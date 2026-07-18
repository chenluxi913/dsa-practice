"""
LeetCode 51. N-Queens

Topic:
- Backtracking
- Recursion
- Matrix

Pattern:
- Place One Queen in Each Row
- Check Previous Rows

Idea:
Place one queen in every row.

For the current row:

1. Try every column.
2. Check whether the current position is safe.
3. Place the queen.
4. Recur to the next row.
5. Remove the queen and backtrack.

Because queens are placed from top to bottom,
only previously processed rows need to be checked.

For board[row][col], check:

- Upper-left diagonal
- Directly above
- Upper-right diagonal

There is no need to check:

- The current row, because only one queen is placed per row.
- The rows below, because they have not been processed yet.

Remember:

Current Row

↓

Try Every Column

↓

Check Upper Three Directions

↓

Place Queen

↓

Move to Next Row

↓

Remove Queen

Time Complexity: O(n! * n)
Space Complexity: O(n^2)
"""


class Solution:

    def solveNQueens(self, n):

        result = []

        board = [
            ["."] * n
            for _ in range(n)
        ]

        self.backtrack(
            0,
            board,
            result
        )

        return result

    def backtrack(
        self,
        row,
        board,
        result
    ):

        # All rows contain one queen.
        if row == len(board):

            solution = [
                "".join(row)
                for row in board
            ]

            result.append(solution)
            return

        for col in range(len(board)):

            if self.isSafe(
                board,
                row,
                col
            ):
                # Place the queen.
                board[row][col] = "Q"

                self.backtrack(
                    row + 1,
                    board,
                    result
                )

                # Remove the queen.
                board[row][col] = "."

    def isSafe(
        self,
        board,
        row,
        col
    ):

        n = len(board)

        # Check directly above.
        current_row = row - 1

        while current_row >= 0:

            if board[current_row][col] == "Q":
                return False

            current_row -= 1

        # Check upper-left diagonal.
        current_row = row - 1
        current_col = col - 1

        while current_row >= 0 and current_col >= 0:

            if board[current_row][current_col] == "Q":
                return False

            current_row -= 1
            current_col -= 1

        # Check upper-right diagonal.
        current_row = row - 1
        current_col = col + 1

        while current_row >= 0 and current_col < n:

            if board[current_row][current_col] == "Q":
                return False

            current_row -= 1
            current_col += 1

        return True


if __name__ == "__main__":

    solution = Solution()

    print(solution.solveNQueens(4))

    # Output:
    # [
    #   [".Q..", "...Q", "Q...", "..Q."],
    #   ["..Q.", "Q...", "...Q", ".Q.."]
    # ]