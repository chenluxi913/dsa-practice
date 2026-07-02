"""
LeetCode 1901. Find a Peak Element II

Topic:
- Matrix
- Binary Search

Pattern:
- Binary Search on Columns

Idea:
Binary search by column.

For each middle column:
1. Find the row with the maximum value in that column.
2. Compare it with left and right neighbors.
3. If it is greater than both, it is a peak.
4. Otherwise, move toward the larger neighbor.

Remember:

Middle Column
↓
Find Column Max
↓
Compare Left / Right
↓
Move Toward Bigger Side

Time Complexity: O(m log n)
Space Complexity: O(1)
"""

class Solution:
    def findMaxInColumn(self, matrix: list[list[int]], col: int) -> int:
        max_row = 0
        for row in range(len(matrix)):
            if matrix[row][col] > matrix[max_row][col]:
                max_row = row
        return max_row
    
    def findPeakGrid(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return [-1, -1]

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n - 1

        while left <= right:
            mid_col = (left + right) // 2
            max_row = self.findMaxInColumn(matrix, mid_col)

            left_neighbor = matrix[max_row][mid_col - 1] if mid_col - 1 >= 0 else float('-inf')
            right_neighbor = matrix[max_row][mid_col + 1] if mid_col + 1 < n else float('-inf')

            if matrix[max_row][mid_col] > left_neighbor and matrix[max_row][mid_col] > right_neighbor:
                return [max_row, mid_col]
            elif left_neighbor > matrix[max_row][mid_col]:
                right = mid_col - 1
            else:
                left = mid_col + 1

        return [-1, -1]
    
if __name__ == "__main__":
    matrix = [
        [1, 4, 3, 2],
        [3, 2, 1, 4],
        [2, 1, 4, 3],
        [4, 3, 2, 1]
    ]
    solution = Solution()
    peak = solution.findPeakGrid(matrix)
    print(peak)  # Output: [0, 1] or [1, 0] depending on the peak found