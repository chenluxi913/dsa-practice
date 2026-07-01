"""
LeetCode 54. Spiral Matrix

Topic:
- Array
- Matrix

Pattern:
- Boundary Traversal

Idea:
Maintain four boundaries:

top
bottom
left
right

Traverse in four directions:

1. Left → Right
2. Top → Bottom
3. Right → Left
4. Bottom → Top

After each traversal,
shrink one boundary.

Remember:

Right
↓

Down
↓

Left
↓

Up

Time Complexity: O(m * n)
Space Complexity: 
Space Complexity:
- Output: O(m × n)
- Extra Space: O(1)
"""


from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        while top <= bottom and left <= right:

            # Left → Right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Top ↓ Bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Right → Left
            # Check if there are still rows to traverse
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Bottom ↑ Top
            # Check if there are still columns to traverse
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result


if __name__ == "__main__":

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    sol = Solution()

    print(sol.spiralOrder(matrix))