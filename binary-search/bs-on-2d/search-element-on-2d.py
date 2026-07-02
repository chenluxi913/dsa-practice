"""
LeetCode 240. Search a 2D Matrix II

Topic:
- Array
- Matrix
- Binary Search

Pattern:
- Staircase Search

Idea:
Start from the top-right corner.

If current value == target:
Return True.

If current value > target:
Move left.

If current value < target:
Move down.

Remember:
Top Right

↓

Too Big → Left

↓

Too Small → Down

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        row = 0
        col = n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False
    
if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    solution = Solution()
    print(solution.searchMatrix(matrix, target)) # Output: True