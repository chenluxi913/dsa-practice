"""
LeetCode 70. Climbing Stairs

Topic:
- Dynamic Programming

Pattern:
- Fibonacci
- Recursion
- Memoization
- Tabulation
- Space Optimization

Idea:
To reach step n:

Option 1:
Come from step n-1

Option 2:
Come from step n-2

Therefore:

ways(n) = ways(n-1) + ways(n-2)

Base Case:
ways(1) = 1
ways(2) = 2

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
    def climbStairs_recursion(self, n: int) -> int:

        if n <= 2:
            return n

        return (
            self.climbStairs_recursion(n - 1)
            + self.climbStairs_recursion(n - 2)
        )

    # Solution 2: Memoization
    # Time: O(n)
    # Space: O(n)
    def climbStairs_memoization(self, n: int) -> int:

        memo = {}

        def dfs(n):

            if n <= 2:
                return n

            if n in memo:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2)

            return memo[n]

        return dfs(n)

    # Solution 3: Tabulation
    # Time: O(n)
    # Space: O(n)
    def climbStairs_tabulation(self, n: int) -> int:

        if n <= 2:
            return n

        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    # Solution 4: Space Optimized (Best)
    # Time: O(n)
    # Space: O(1)
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        prev2 = 1
        prev1 = 2

        for _ in range(3, n + 1):

            current = prev1 + prev2

            prev2 = prev1
            prev1 = current

        return prev1


if __name__ == "__main__":

    sol = Solution()

    n = 5

    print("Recursion        :", sol.climbStairs_recursion(n))
    print("Memoization      :", sol.climbStairs_memoization(n))
    print("Tabulation       :", sol.climbStairs_tabulation(n))
    print("Space Optimized  :", sol.climbStairs(n))