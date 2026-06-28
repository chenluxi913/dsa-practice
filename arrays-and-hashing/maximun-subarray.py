"""
LeetCode 53. Maximum Subarray

Topic:
- Array
- Dynamic Programming

Pattern:
- Kadane's Algorithm

Idea:
At each position, decide whether to:
1. Start a new subarray from current number
2. Extend the previous subarray

If previous sum becomes harmful, start fresh.

Formula:
current_sum = max(num, current_sum + num)
max_sum = max(max_sum, current_sum)

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
    
    
    def maxSubArraywithIndices(self, nums: list[int]) -> int:

        max_sum = float("-inf")
        current_sum = 0

        start = 0
        best_start = 0
        best_end = 0

        for i in range(len(nums)):

            if current_sum == 0:
                start = i

            current_sum += nums[i]

            if current_sum > max_sum:
                max_sum = current_sum
                best_start = start
                best_end = i

            if current_sum < 0:
                current_sum = 0


        return {
            "max_sum": max_sum,
            "start": best_start,
            "end": best_end,
            "subarray": nums[best_start:best_end + 1],
        }
    
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    sol = Solution()
    max_sum = sol.maxSubArray(nums)
    print(f"The maximum subarray sum is: {max_sum}")

    result = sol.maxSubArraywithIndices(nums)
    print(f"Maximum subarray sum: {result['max_sum']}")
    print(f"Start index: {result['start']}, End index: {result['end']}")
    print(f"Maximum subarray: {result['subarray']}")