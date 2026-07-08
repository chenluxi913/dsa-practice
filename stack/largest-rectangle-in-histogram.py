"""
LeetCode 84. Largest Rectangle in Histogram

Topic:
- Array
- Stack
- Monotonic Stack

Pattern:
- Previous Smaller Element
- Next Smaller Element

Idea:
Maintain an increasing stack of indices.

When current height is smaller than stack top,
the current index becomes the next smaller element
for the popped bar.

After popping:
- previous smaller = new stack top
- next smaller = current index

width = next_smaller - previous_smaller - 1
area = height * width

Remember:

Increasing Stack
↓
Pop when smaller
↓
Calculate Area

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        n = len(heights)

        stack = []
        largest_area = 0

        for i in range(n):

            while stack and heights[stack[-1]] >= heights[i]:

                index = stack.pop()

                previous_smaller = stack[-1] if stack else -1
                next_smaller = i

                width = next_smaller - previous_smaller - 1
                area = heights[index] * width

                largest_area = max(largest_area, area)

            stack.append(i)

        while stack:

            index = stack.pop()

            previous_smaller = stack[-1] if stack else -1
            next_smaller = n

            width = next_smaller - previous_smaller - 1
            area = heights[index] * width

            largest_area = max(largest_area, area)

        return largest_area
    
if __name__ == "__main__":
    solution = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    print(solution.largestRectangleArea(heights))  # Output: 10