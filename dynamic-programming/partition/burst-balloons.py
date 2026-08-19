"""
LeetCode 312. Burst Balloons

Topic:
- Dynamic Programming
- Recursion
- Memoization
- Interval DP
- Partition DP

Pattern:
- Choose the Last Balloon
- Solve Left and Right Intervals

Idea:
The coins gained from bursting a balloon depend
on its current left and right neighbors.

Instead of choosing which balloon to burst first,
choose which balloon is burst last in the current
interval.

Add two virtual balloons with value 1:

[1] + nums + [1]

For the current interval from i to j:

nums[i - 1]

is the fixed left boundary.

nums[j + 1]

is the fixed right boundary.

Try every balloon k between i and j as the
last balloon to burst.

If k is burst last:

Current coins:

nums[i - 1] * nums[k] * nums[j + 1]

The remaining balloons are divided into:

Left interval:
i to k - 1

Right interval:
k + 1 to j

Total coins:

current coins
+
left coins
+
right coins

Take the maximum among all possible choices.

Base Case:

If i > j:

There are no balloons left to burst.

Return 0.

Remember:

Add 1 to Both Ends

↓

Choose Interval i ... j

↓

Try Every Balloon k

↓

Treat k as the Last Balloon

↓

Current Coins =
nums[i - 1] * nums[k] * nums[j + 1]

↓

Solve Left

+

Solve Right

↓

Take Maximum

Time Complexity: O(n^3)

Space Complexity:
O(n^2) + O(n)
"""


from typing import List


class Solution:

    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)

        # Add virtual balloons with value 1
        # to both ends.
        nums = [1] + nums + [1]

        # dp[i][j] stores the maximum coins
        # obtained from interval i to j.
        dp = [[-1] * (n + 2) for _ in range(n + 2)]

        return self.func(1, n, nums, dp)

    # Function to calculate the maximum coins
    # for the current interval.
    def func(self, i, j, nums, dp):

        # Base case.
        if i > j:
            return 0

        # Return the memoized result.
        if dp[i][j] != -1:
            return dp[i][j]

        max_coins = float("-inf")

        # Try every balloon as the last
        # balloon to burst.
        for k in range(i, j + 1):

            # Coins obtained by bursting
            # the k-th balloon last.
            coins = nums[i - 1] * nums[k] * nums[j + 1]

            # Maximum coins from the
            # left and right intervals.
            remaining_coins = self.func(i, k - 1, nums, dp) + self.func(k + 1, j, nums, dp)

            max_coins = max(max_coins, coins + remaining_coins)

        dp[i][j] = max_coins

        return dp[i][j]


if __name__ == "__main__":

    solution = Solution()

    nums = [3, 1, 5, 8]

    print(solution.maxCoins(nums))

    # Output:
    # 167