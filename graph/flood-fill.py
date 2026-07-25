"""
LeetCode 733. Flood Fill

Topic:
- Graph
- DFS
- Grid
- Matrix

Pattern:
- Flood Fill
- Connected Component

Idea:
The image is treated as an implicit graph.

Each pixel is a node, and every pixel has
up to four neighbors:

- Up
- Right
- Down
- Left

Store the starting pixel's original color.

Create a copy of the image called answer.

Run DFS from the starting pixel:

1. Change the current pixel in answer
   to the new color.

2. Visit every valid neighboring pixel.

3. Continue only when:
   - The neighbor has the original color.
   - The neighbor has not already been changed
     to the new color in answer.

Remember:

Store Initial Color

↓

Copy Image

↓

Color Current Pixel

↓

Check Four Neighbors

↓

Same Original Color

↓

Not Already Recolored

↓

Continue DFS

Time Complexity: O(m * n)
Space Complexity: O(m * n)

The copied image and recursion stack can each
use up to O(m * n) space.
"""


class Solution:

    def __init__(self):

        self.row_change = [-1, 0, 1, 0]
        self.col_change = [0, 1, 0, -1]

    def floodFill(self, image, sr, sc, color):

        original_color = image[sr][sc]

        # Copy the original image so that the
        # input image is not modified.
        answer = [row[:] for row in image]

        self.dfs(
            sr,
            sc,
            answer,
            image,
            color,
            original_color
        )

        return answer

    def dfs(
        self,
        row,
        col,
        answer,
        image,
        new_color,
        original_color
    ):

        answer[row][col] = new_color

        rows = len(image)
        cols = len(image[0])

        for direction in range(4):

            next_row = row + self.row_change[direction]
            next_col = col + self.col_change[direction]

            if (
                self.isValid(
                    next_row,
                    next_col,
                    rows,
                    cols
                )
                and image[next_row][next_col] == original_color
                and answer[next_row][next_col] != new_color
            ):
                self.dfs(
                    next_row,
                    next_col,
                    answer,
                    image,
                    new_color,
                    original_color
                )

    def isValid(self, row, col, rows, cols):

        return (
            0 <= row < rows
            and 0 <= col < cols
        )


if __name__ == "__main__":

    solution = Solution()

    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    print(
        solution.floodFill(
            image,
            1,
            1,
            2
        )
    )

    # Output:
    # [
    #   [2, 2, 2],
    #   [2, 2, 0],
    #   [2, 0, 1]
    # ]