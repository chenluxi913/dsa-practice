"""
LeetCode 1004. Max Consecutive Ones III

Topic:
- Array
- Sliding Window

Pattern:
- Variable Size Sliding Window

Idea:
Maintain a window with at most k zeros.

Expand right.

If the number of zeros is greater than k,
shrink from the left.

Update the maximum valid window length.

Remember:

Expand Right
↓

Count Zeros
↓

Shrink if zeros > k
↓

Update Answer

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1

            while zeros > k:

                if nums[left] == 0:
                    zeros -= 1

                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
    
if __name__ == "__main__":
    nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
    k = 2
    solution = Solution()
    result = solution.longestOnes(nums, k)
    print(result)  # Output: 6