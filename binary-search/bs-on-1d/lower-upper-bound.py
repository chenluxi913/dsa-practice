"""
LeetCode 35. Search Insert Position
this problem is using lower bound solution
also attached upper bound solution for reference

LeetCode 34. Find First and Last Position of Element in Sorted Array
can also use lower bound and upper bound to find the first and last position of the target in sorted array
make sure to check if the target exists in the array before returning the indices

Topic:
- Array
- Binary Search

Pattern:
- Lower Bound
- Upper Bound

Definitions:

Lower Bound:
First index where nums[index] >= target.

Upper Bound:
First index where nums[index] > target.

Remember:

Lower Bound
nums[mid] >= target
↓
Potential Answer
↓
Move Left

Upper Bound
nums[mid] > target
↓
Potential Answer
↓
Move Left

Time Complexity: O(log n)
Space Complexity: O(1)
"""


from typing import List


class Solution:

    # Lower Bound
    # First index where nums[index] >= target
    def lowerBound(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        ans = len(nums)

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] >= target:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans

    # Upper Bound
    # First index where nums[index] > target
    def upperBound(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        ans = len(nums)

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] > target:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans


if __name__ == "__main__":

    nums = [1, 2, 2, 3]

    target = 2

    sol = Solution()

    print("Lower Bound:", sol.lowerBound(nums, target))
    print("Upper Bound:", sol.upperBound(nums, target))