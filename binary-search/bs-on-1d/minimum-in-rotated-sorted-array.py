"""
LeetCode 153. Find Minimum in Rotated Sorted Array

Topic:
- Array
- Binary Search

Pattern:
- Rotated Binary Search
- Answer Tracking

Idea:
One half of the array is always sorted.

If the left half is sorted:
The minimum in this half is arr[left].
Record it and search the right half.

Otherwise:
The pivot is in the left half.
Record arr[mid] and search the left half.

Remember:
Left Half Sorted
↓

Record Left

↓

Search Right

Otherwise

↓

Record Mid

↓

Search Left

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:

    def findMin(self, nums: list[int]) -> int:

        left = 0
        right = len(nums) - 1
        ans = float("inf")

        while left <= right:

            mid = (left + right) // 2

            # Left half is sorted.
            # Record the minimum in this half and search the right half.
            if nums[left] <= nums[mid]:
                ans = min(ans, nums[left])
                left = mid + 1

            # Right half is sorted meaning the pivot is in the left half.
            else:
                ans = min(ans, nums[mid])
                right = mid - 1

        return ans
    
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 4, 5, 1, 2]
    print(solution.findMin(nums))  # Output: 1