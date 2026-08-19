"""
LeetCode 416. Partition Equal Subset Sum

Topic:
- Dynamic Programming
- Recursion
- Memoization
- Array
- Subset Sum
- 0/1 Knapsack

Pattern:
- Pick or Not Pick
- Top-Down Dynamic Programming

Idea:
To partition the array into two subsets with
equal sums, the total sum of the array must
be even.

If the total sum is odd, it is impossible to
divide the array into two equal subsets.

If the total sum is even, the problem becomes:

Can we find a subset whose sum equals:

total_sum // 2

At every index, there are two choices:

1. Do not take the current number.
   - Move to the previous index.
   - Keep the target unchanged.

2. Take the current number.
   - Only possible when the current number
     does not exceed the remaining target.
   - Subtract it from the target.
   - Move to the previous index.

Use memoization to store the result of each state:

dp[index][target]

A state is uniquely determined by:

- The current index
- The remaining target

Store:

- 1 if the target can be formed
- 0 if the target cannot be formed
- -1 if the state has not been calculated

Base cases:

- If target == 0:
  A valid subset has been found.

- If index == 0:
  Return whether the first number equals
  the remaining target.

Remember:

Calculate Total Sum

↓

Total Sum Is Odd?

↓

Return False

↓

Target = Total Sum // 2

↓

Check Memoized Result

↓

Pick or Not Pick

↓

Store Result in DP

↓

Return Answer

Time Complexity: O(n * target)
Space Complexity: O(n * target) + O(n)
"""


from typing import List


class Solution:

    # Function to determine whether a subset
    # can form the target sum.
    def func(
        self,
        index: int,
        target: int,
        nums: List[int],
        dp: List[List[int]]
    ) -> bool:

        # A target of zero can always
        # be formed by taking no elements.
        if target == 0:
            return True

        # Only the first number remains.
        if index == 0:
            return nums[0] == target

        # Return the stored result if this
        # state has already been calculated.
        if dp[index][target] != -1:
            return dp[index][target] == 1

        # Choice 1:
        # Do not take the current number.
        not_taken = self.func(
            index - 1,
            target,
            nums,
            dp
        )

        # Choice 2:
        # Take the current number if possible.
        taken = False

        if nums[index] <= target:
            taken = self.func(
                index - 1,
                target - nums[index],
                nums,
                dp
            )

        # Store the result.
        dp[index][target] = (
            1
            if not_taken or taken
            else 0
        )

        return dp[index][target] == 1

    def canPartition(
        self,
        nums: List[int]
    ) -> bool:

        total_sum = sum(nums)

        # An odd total sum cannot be divided
        # into two equal integer sums.
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        # dp[index][target] stores:
        #
        # -1 = not calculated
        #  0 = cannot form target
        #  1 = can form target
        dp = [
            [-1] * (target + 1)
            for _ in range(n)
        ]

        return self.func(
            n - 1,
            target,
            nums,
            dp
        )


if __name__ == "__main__":

    solution = Solution()

    nums = [1, 5, 11, 5]

    print(
        solution.canPartition(nums)
    )

    # Output:
    # True