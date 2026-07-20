"""
LeetCode 37. Sudoku Solver

Topic:
- Backtracking
- Recursion
- Matrix

Pattern:
- Fill One Empty Cell at a Time

Idea:
Scan the board from left to right,
top to bottom.

When an empty cell is found:

1. Try every digit from 1 to 9.
2. Check whether the digit satisfies:
   - Row rule
   - Column rule
   - 3 x 3 box rule
3. Place the digit.
4. Recursively solve the remaining board.
5. If the recursion fails, reset the cell
   and try another digit.

If no empty cells remain,
the Sudoku is solved.

Remember:

Find Empty Cell

↓

Try Digits 1 to 9

↓

Check Row, Column, and Box

↓

Place Digit

↓

Solve Remaining Board

↓

Reset If It Fails

Time Complexity: O(9^E)

Space Complexity: O(E)

where E is the number of empty cells.
"""


class Solution:

    def solveSudoku(self, board):

        self.solve(board)

    def solve(self, board):

        for row in range(9):
            for col in range(9):

                # Find the first empty cell.
                if board[row][col] == ".":

                    for digit in "123456789":

                        if self.isValid(
                            board,
                            row,
                            col,
                            digit
                        ):
                            # Place the digit.
                            board[row][col] = digit

                            # Solve the remaining board.
                            if self.solve(board):
                                return True

                            # Backtrack.
                            board[row][col] = "."

                    # No valid digit works for this cell.
                    return False

        # No empty cells remain.
        return True

    def isValid(
        self,
        board,
        row,
        col,
        digit
    ):

        # Check the row.
        for index in range(9):

            if board[row][index] == digit:
                return False

        # Check the column.
        for index in range(9):

            if board[index][col] == digit:
                return False

        # Find the top-left corner
        # of the current 3 x 3 box.
        start_row = 3 * (row // 3)
        start_col = 3 * (col // 3)

        # Check the 3 x 3 box.
        for current_row in range(
            start_row,
            start_row + 3
        ):
            for current_col in range(
                start_col,
                start_col + 3
            ):
                if board[current_row][current_col] == digit:
                    return False

        return True


if __name__ == "__main__":

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    solution = Solution()
    solution.solveSudoku(board)

    for row in board:
        print(row)