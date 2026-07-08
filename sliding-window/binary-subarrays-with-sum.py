"""
LeetCode 930. Binary Subarrays With Sum

Topic:
- Array
- Sliding Window

Pattern:
- Exactly K = AtMost(K) - AtMost(K - 1)

Idea:
Count subarrays with sum exactly equal to goal.

Since nums is binary:

Exactly(goal)
=
AtMost(goal)
-
AtMost(goal - 1)

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        return (
            self.atMost(nums, goal)
            - self.atMost(nums, goal - 1)
        )

    def atMost(self, nums: List[int], goal: int) -> int:

        if goal < 0:
            return 0

        left = 0
        current_sum = 0
        count = 0

        for right in range(len(nums)):

            current_sum += nums[right]

            while current_sum > goal:
                current_sum -= nums[left]
                left += 1

            count += right - left + 1

        return count
    
if __name__ == "__main__":
    nums = [1, 0, 1, 0, 1]
    goal = 2
    solution = Solution()
    result = solution.numSubarraysWithSum(nums, goal)
    print(result)  # Output: 4