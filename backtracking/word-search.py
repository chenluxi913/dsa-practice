"""
LeetCode 79. Word Search

Topic:
- Backtracking
- DFS
- Matrix

Pattern:
- Grid DFS
- Mark and Restore

Idea:
Try every cell as the starting point.

From each matching starting cell, use DFS
to match the word one character at a time.

For the current cell:

1. Check boundaries.
2. Check whether the character matches word[index].
3. Temporarily mark the cell as visited.
4. Search four neighboring cells.
5. Restore the original character.

The temporary mark prevents the same cell
from being used more than once in one path.

Remember:

Try Every Cell

↓

Match Current Character

↓

Mark Current Cell

↓

Search Four Directions

↓

Restore Current Cell

Time Complexity: O(m * n * 3^L)
Space Complexity: O(L)

where:
- m and n are the board dimensions
- L is the length of word
"""


class Solution:

    def exist(self, board, word):

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):

                if board[row][col] == word[0]:

                    if self.backtrack(
                        board,
                        row,
                        col,
                        word,
                        0
                    ):
                        return True

        return False

    def backtrack(
        self,
        board,
        row,
        col,
        word,
        index
    ):

        # All characters have been matched.
        if index == len(word):
            return True

        # Invalid position or character mismatch.
        if (
            row < 0
            or row >= len(board)
            or col < 0
            or col >= len(board[0])
            or board[row][col] != word[index]
        ):
            return False

        original = board[row][col]

        # Mark the current cell as visited.
        board[row][col] = "#"

        found = (
            self.backtrack(
                board,
                row + 1,
                col,
                word,
                index + 1
            )
            or self.backtrack(
                board,
                row - 1,
                col,
                word,
                index + 1
            )
            or self.backtrack(
                board,
                row,
                col + 1,
                word,
                index + 1
            )
            or self.backtrack(
                board,
                row,
                col - 1,
                word,
                index + 1
            )
        )

        # Restore the current cell.
        board[row][col] = original

        return found


if __name__ == "__main__":

    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]

    solution = Solution()

    print(solution.exist(board, "ABCCED"))  # True
    print(solution.exist(board, "SEE"))     # True
    print(solution.exist(board, "ABCB"))    # False