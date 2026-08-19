"""
LeetCode 518. Coin Change II

Topic:
- Dynamic Programming
- Recursion
- Memoization
- Array
- Unbounded Knapsack

Pattern:
- Pick or Not Pick
- Count Ways
- Unlimited Reuse

Idea:
We need to count how many combinations can
form the given amount.

At every index, there are two choices:

1. Do not take the current coin.
   - Move to the previous index.
   - Keep the amount unchanged.

2. Take the current coin.
   - Subtract the coin value from the amount.
   - Stay at the same index because each coin
     can be used an unlimited number of times.

The total number of combinations is the sum of:

not_taken + taken

Base Case:

When index == 0, only coins[0] is available.

If the remaining amount can be completely divided
by coins[0], there is exactly one way to form it.

Otherwise, there are zero ways.

Remember:

Pick or Not Pick

↓

Not Take

↓

Move to Previous Index

↓

Take

↓

Stay at Same Index

↓

Subtract Coin Value

↓

Add Both Choices

Time Complexity: O(n * amount)

Space Complexity:
O(n * amount) + O(amount)
"""


from typing import List


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        # dp[index][amount] stores the number
        # of combinations to form the amount.
        dp = [[-1] * (amount + 1) for _ in range(n)]

        return self.func(n - 1, amount, coins, dp)

    # Function to count the number of ways
    # to form the given amount.
    def func(self, ind, amount, coins, dp):

        # Base case.
        if ind == 0:

            # Only coins[0] is available.
            if amount % coins[0] == 0:
                return 1

            return 0

        # Return the memoized result.
        if dp[ind][amount] != -1:
            return dp[ind][amount]

        # Do not take the current coin.
        not_taken = self.func(ind - 1, amount, coins, dp)

        # Take the current coin.
        taken = 0

        if coins[ind] <= amount:
            taken = self.func(ind, amount - coins[ind], coins, dp)

        # Store the total number of combinations.
        dp[ind][amount] = not_taken + taken

        return dp[ind][amount]


if __name__ == "__main__":

    solution = Solution()

    amount = 5
    coins = [1, 2, 5]

    print(solution.change(amount, coins))

    # Output:
    # 4