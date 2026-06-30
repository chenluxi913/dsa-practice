"""
LeetCode 34. Find First and Last Position of Element

Topic:
- Array
- Binary Search

Pattern:
- First Occurrence
- Last Occurrence

Idea:
Run Binary Search twice.

First Occurrence:
Keep searching the left half after finding target.

Last Occurrence:
Keep searching the right half after finding target.

Remember:

Find Target
↓

Record Answer

↓

Continue Searching

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:

    # First Occurrence
    # Time: O(log n)
    # Space: O(1)
    def firstOccurrence(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            # Record the current index and continue searching left
            # for an earlier occurrence.
            if nums[mid] == target:
                ans = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return ans

    # Last Occurrence
    # Time: O(log n)
    # Space: O(1)
    def lastOccurrence(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:

            mid = (left + right) // 2

            # Record the current index and continue searching right
            # for a later occurrence.
            if nums[mid] == target:
                ans = mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return ans
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOccurrence(nums, target)

        # if first is -1, it means the target is not found in the array, so we can return [-1, -1] immediately
        if first == -1:
            return [-1, -1]
        
        last = self.lastOccurrence(nums, target)

        return [first, last]
    
if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    solution = Solution()
    print(solution.searchRange(nums, target))  # Output: [3, 4]