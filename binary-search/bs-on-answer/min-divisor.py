"""
LeetCode 1283. Find the Smallest Divisor Given a Threshold

Topic:
- Array
- Binary Search

Pattern:
- Binary Search on Answer
- Minimum Valid Answer

Idea:
Search the smallest divisor.

For each divisor:
Calculate the sum of ceil(num / divisor).

If total <= threshold:
This divisor works.
Try a smaller divisor.

Otherwise:
The divisor is too small.
Try a larger divisor.

Remember:

Binary Search on Divisor
↓
Calculate Sum
↓
Minimum Valid Answer

Time Complexity: O(n log M)

n = len(nums)
M = max(nums)

Space Complexity: O(1)
"""

class Solution:
    def calculateSum(self, nums: list[int], divisor: int) -> int:
        total = 0

        for num in nums:
            total += (num + divisor - 1) // divisor  # ceil(num / divisor)

        return total
    
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left, right = 1, max(nums) #start from 1

        while left < right:
            mid = (left + right) // 2

            total = self.calculateSum(nums, mid)

            if total <= threshold:
                right = mid
            else:
                left = mid + 1

        return left
    
if __name__ == "__main__":
    nums = [1, 2, 5, 9]
    threshold = 6

    solution = Solution()
    result = solution.smallestDivisor(nums, threshold)
    print(result)  # Output: 5