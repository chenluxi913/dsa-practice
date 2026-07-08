"""
LeetCode 904. Fruit Into Baskets

Topic:
- Array
- Hash Map
- Sliding Window

Pattern:
- Variable Size Sliding Window
- At Most K Distinct

Idea:
Maintain a window with at most
2 distinct fruit types.

Expand the window by moving right.

If the number of fruit types exceeds 2,
shrink the window from the left.

Update the maximum window length.

Remember:

Expand Right
↓

Count Fruit Types
↓

Shrink if Types > 2
↓

Update Answer

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:

    def totalFruit(self, fruits: List[int]) -> int:

        count = {}

        left = 0
        max_length = 0

        for right in range(len(fruits)):

            count[fruits[right]] = count.get(fruits[right], 0) + 1

            while len(count) > 2:

                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
    
if __name__ == "__main__":
    fruits = [1, 2, 1]
    solution = Solution()
    result = solution.totalFruit(fruits)
    print(result)  # Output: 3