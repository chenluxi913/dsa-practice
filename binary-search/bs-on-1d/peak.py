"""
LeetCode 162. Find Peak Element

Topic:
- Array
- Binary Search

Pattern:
- Binary Search on Slope

Idea:
A peak is greater than both neighbors.

Handle edge cases first:
- If n == 1, index 0 is peak.
- If nums[0] > nums[1], index 0 is peak.
- If nums[n-1] > nums[n-2], index n-1 is peak.

Then binary search inside the array.

If nums[mid] is a peak:
Return mid.

If nums[mid] < nums[mid - 1]:
We are going down from left to right,
so a peak must exist on the left.

Otherwise:
A peak must exist on the right.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:

    def findPeakElement(self, nums: list[int]) -> int:

        n = len(nums)

        # Handle edge cases first.
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        left = 1
        right = n - 2

        while left <= right:

            mid = (left + right) // 2

            # Found a peak.
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            # We are going down from left to right,
            # so a peak must exist on the left.
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1

            # A peak must exist on the right.
            else:
                left = mid + 1

        return -1  # This line should never be reached if input is valid.
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1]
    print(solution.findPeakElement(nums))  # Output: 2