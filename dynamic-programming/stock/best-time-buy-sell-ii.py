"""
LeetCode 122. Best Time to Buy and Sell Stock II

Topic:
- Dynamic Programming
- Recursion
- Memoization
- Stock

Pattern:
- Buy or Skip
- Sell or Hold
- Unlimited Transactions

Idea:
We can complete as many transactions as we want,
but we can hold at most one stock at a time.

Use two states:

buy = 0:
We do not currently own a stock,
so we can either buy or skip.

buy = 1:
We currently own a stock,
so we can either sell or hold.

If buy == 0:

1. Skip:
   - Move to the next day.
   - Keep buy = 0.

2. Buy:
   - Subtract prices[ind] from the profit.
   - Move to the next day.
   - Change buy to 1.

If buy == 1:

1. Hold:
   - Move to the next day.
   - Keep buy = 1.

2. Sell:
   - Add prices[ind] to the profit.
   - Move to the next day.
   - Change buy to 0.

Take the maximum profit from the two choices.

Base Case:

If ind == n:

There are no more days left.

Return 0.

Remember:

buy == 0
→ Can Buy
→ Skip OR Buy
→ Buy changes 0 → 1

buy == 1
→ Can Sell
→ Hold OR Sell
→ Sell changes 1 → 0

Time Complexity: O(n * 2)

Space Complexity:
O(n * 2) + O(n)
"""


from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        dp = [[-1] * 2 for _ in range(n)]

        return self.func(0, 0, n, prices, dp)

    # Function to find the maximum profit
    # using recursion and memoization.
    def func(self, ind, buy, n, prices, dp):

        # Base case.
        if ind == n:
            return 0

        # Return the memoized result.
        if dp[ind][buy] != -1:
            return dp[ind][buy]

        # We can buy the stock.
        if buy == 0:
            skip = self.func(ind + 1, 0, n, prices, dp)
            buy_stock = -prices[ind] + self.func(ind + 1, 1, n, prices, dp)

            profit = max(skip, buy_stock)

        # We can sell the stock.
        else:
            hold = self.func(ind + 1, 1, n, prices, dp)
            sell_stock = prices[ind] + self.func(ind + 1, 0, n, prices, dp)

            profit = max(hold, sell_stock)

        dp[ind][buy] = profit

        return dp[ind][buy]


if __name__ == "__main__":

    solution = Solution()

    prices = [7, 1, 5, 3, 6, 4]

    print(solution.maxProfit(prices))

    # Output:
    # 7