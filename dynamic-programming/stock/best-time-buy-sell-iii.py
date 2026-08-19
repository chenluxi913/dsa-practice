"""
LeetCode 123. Best Time to Buy and Sell Stock III

Topic:
- Dynamic Programming
- Recursion
- Memoization
- Stock

Pattern:
- Buy or Skip
- Sell or Hold
- Limited Transactions

Idea:
We can complete at most two transactions.

Use three states:

ind:
Current day.

buy:
Whether we can buy or sell.

buy = 0:
We can buy the stock.

buy = 1:
We can sell the stock.

cap:
Number of transactions still available.

If buy == 0:

1. Skip:
   - Move to the next day.
   - Keep buy = 0.
   - Keep cap unchanged.

2. Buy:
   - Subtract prices[ind].
   - Move to the next day.
   - Change buy to 1.
   - Keep cap unchanged.

If buy == 1:

1. Hold:
   - Move to the next day.
   - Keep buy = 1.
   - Keep cap unchanged.

2. Sell:
   - Add prices[ind].
   - Move to the next day.
   - Change buy to 0.
   - Decrease cap by 1.

A transaction is completed when we sell,
so cap decreases only after selling.

Base Case:

If ind == n or cap == 0:

Return 0.

Remember:

buy == 0
→ Skip OR Buy

buy == 1
→ Hold OR Sell

Buy:
cap stays the same

Sell:
cap decreases by 1

Initial State:

ind = 0
buy = 0
cap = 2

Time Complexity: O(n * 2 * 3)

Space Complexity:
O(n * 2 * 3) + O(n)
"""


from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]

        return self.func(0, 0, 2, n, prices, dp)

    # Function to find the maximum profit
    # using recursion and memoization.
    def func(self, ind, buy, cap, n, prices, dp):

        # Base case.
        if ind == n or cap == 0:
            return 0

        # Return the memoized result.
        if dp[ind][buy][cap] != -1:
            return dp[ind][buy][cap]

        # We can buy the stock.
        if buy == 0:
            skip = self.func(ind + 1, 0, cap, n, prices, dp)
            buy_stock = -prices[ind] + self.func(ind + 1, 1, cap, n, prices, dp)

            profit = max(skip, buy_stock)

        # We can sell the stock.
        else:
            hold = self.func(ind + 1, 1, cap, n, prices, dp)
            sell_stock = prices[ind] + self.func(ind + 1, 0, cap - 1, n, prices, dp)

            profit = max(hold, sell_stock)

        dp[ind][buy][cap] = profit

        return dp[ind][buy][cap]


if __name__ == "__main__":

    solution = Solution()

    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    print(solution.maxProfit(prices))

    # Output:
    # 6