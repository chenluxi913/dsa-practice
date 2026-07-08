"""
LeetCode 85. Maximal Rectangle

Topic:
- Array
- Matrix
- Stack
- Monotonic Stack

Pattern:
- Matrix to Histogram
- Largest Rectangle in Histogram

Idea:
Convert each row into a histogram.

For each row:
- If matrix[row][col] == "1":
    heights[col] += 1
- Else:
    heights[col] = 0

Then use LeetCode 84 to find the largest
rectangle in the histogram.

Remember:

Matrix Row

↓

Build Heights

↓

Largest Rectangle in Histogram

Time Complexity: O(rows * cols)
Space Complexity: O(cols)
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "0":
                    heights[col] = 0
                else:
                    heights[col] += 1

            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, height * width)
            # out of while loop, push the current index onto the stack
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = n - left - 1
            max_area = max(max_area, height * width)

        return max_area
    
if __name__ == "__main__":
    solution = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(solution.maximalRectangle(matrix))  # Output: 6