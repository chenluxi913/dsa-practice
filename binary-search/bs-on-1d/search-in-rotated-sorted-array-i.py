"""
LeetCode 33. Search in Rotated Sorted Array

Topic:
- Array
- Binary Search

Pattern:
- Rotated Binary Search

Idea:
One half of the array is always sorted.

1. Identify the sorted half.
2. Check if the target is inside that half.
3. Search the appropriate half.

Remember:
Find Sorted Half
↓

Check Target Range

↓

Discard Half

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:

    def search(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                # Target is in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # Target is in the right half
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                # Target is in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # Target is in the left half
                else:
                    right = mid - 1

        return -1
    
if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    sol = Solution()
    result = sol.search(nums, target)
    print(f"The index of {target} in the rotated sorted array is: {result}")