"""
LeetCode 509. Fibonacci Number

Topic:
- Recursion
- Dynamic Programming

Pattern:
- Recursion
- Memoization
- Tabulation
- Space Optimization

Idea:
F(n) = F(n - 1) + F(n - 2)

Base Case:
F(0) = 0
F(1) = 1

Evolution:
Recursion
↓
Memoization
↓
Tabulation
↓
Space Optimization
"""


class Solution:

    # Solution 1: Recursion
    # Time: O(2^n)
    # Space: O(n)
    def fib_recursion(self, n: int) -> int:

        if n <= 1:
            return n

        return self.fib_recursion(n - 1) + self.fib_recursion(n - 2)

    # Solution 2: Memoization / Top-Down DP
    # Time: O(n)
    # Space: O(n)
    def fib_memoization(self, n: int) -> int:

        memo = {}

        def dfs(n):
            if n <= 1:
                return n

            if n in memo:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2)

            return memo[n]

        return dfs(n)

    # Solution 3: Tabulation / Bottom-Up DP
    # Time: O(n)
    # Space: O(n)
    def fib_tabulation(self, n: int) -> int:

        if n <= 1:
            return n

        dp = [0] * (n + 1)

        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    # Solution 4: Space Optimized DP
    # Time: O(n)
    # Space: O(1)
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        prev2 = 0
        prev1 = 1

        for _ in range(2, n + 1):
            current = prev1 + prev2

            prev2 = prev1
            prev1 = current

        return prev1


if __name__ == "__main__":

    sol = Solution()

    n = 4

    print("Recursion        :", sol.fib_recursion(n))
    print("Memoization      :", sol.fib_memoization(n))
    print("Tabulation       :", sol.fib_tabulation(n))
    print("Space Optimized  :", sol.fib(n))