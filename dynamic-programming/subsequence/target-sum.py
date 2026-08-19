"""
LeetCode 494. Target Sum

Topic:
- Dynamic Programming
- Recursion
- Memoization
- Array
- Subset Sum

Pattern:
- Pick or Not Pick
- Count Subsets with Given Sum

Idea:
Assign either '+' or '-' to every number.

Suppose:

S1 = sum of numbers assigned '+'
S2 = sum of numbers assigned '-'

Then:

S1 - S2 = target
S1 + S2 = total_sum

Therefore:

S2 = (total_sum - target) / 2

The problem becomes:

Count the number of subsets whose sum equals:

(total_sum - target) // 2

At every index, there are two choices:

1. Do not take the current number.
2. Take the current number.

The total number of ways equals the sum of
both choices.

Special Case:

If nums[0] == 0 and target == 0,
there are two ways:

+0
-0

Remember:

S1 - S2 = Target

↓

S1 + S2 = Total Sum

↓

S2 = (Total Sum - Target) / 2

↓

Count Subsets With Sum S2

↓

Pick or Not Pick

↓

Add Both Choices

Time Complexity: O(n * target)

Space Complexity:
O(n * target) + O(n)
"""


from typing import List


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total_sum = sum(nums)

        # It is impossible to reach the target.
        if total_sum - target < 0:
            return 0

        # The required subset sum
        # must be an integer.
        if (total_sum - target) % 2 != 0:
            return 0

        subset_target = (total_sum - target) // 2

        n = len(nums)

        # dp[index][target] stores the
        # number of ways to form target.
        dp = [[-1] * (subset_target + 1) for _ in range(n)]

        return self.func(n - 1, subset_target, nums, dp)

    # Function to count the number of subsets
    # with the given target sum.
    def func(self, ind, target, nums, dp):

        # Base case.
        if ind == 0:

            # +0 and -0.
            if target == 0 and nums[0] == 0:
                return 2

            # Either choose nothing
            # or choose nums[0].
            if target == 0 or target == nums[0]:
                return 1

            return 0

        # Return the memoized result.
        if dp[ind][target] != -1:
            return dp[ind][target]

        # Do not take the current number.
        not_taken = self.func(ind - 1, target, nums, dp)

        # Take the current number.
        taken = 0

        if nums[ind] <= target:
            taken = self.func(ind - 1, target - nums[ind], nums, dp)

        # Store the total number of ways.
        dp[ind][target] = not_taken + taken

        return dp[ind][target]


if __name__ == "__main__":

    solution = Solution()

    nums = [1, 1, 1, 1, 1]
    target = 3

    print(solution.findTargetSumWays(nums, target))

    # Output:
    # 5