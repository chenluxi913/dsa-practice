"""
LeetCode 198. House Robber

Topic:
- Array
- Dynamic Programming

Pattern:
- Choose / Skip DP
- Recursion
- Memoization
- Tabulation
- Space Optimization

Idea:
At each house:

Skip current house (not take)
or
Rob current house (take)

Formula:
dp[i] = max(dp[i-1], dp[i-2] + nums[i])

Remember:
Skip
or
Rob

Evolution:
Recursion
↓
Memoization
↓
Tabulation
↓
Space Optimization
"""


from typing import List


class Solution:

    # Solution 1: Recursion
    # Time: O(2^n)
    # Space: O(n)
    def rob_recursion(self, nums: List[int]) -> int:

        def dfs(i):

            # Base Case
            if i < 0:
                return 0

            if i == 0:
                return nums[0]

            skip = dfs(i - 1)
            rob = nums[i] + dfs(i - 2)

            return max(skip, rob)

        return dfs(len(nums) - 1)

    # Solution 2: Memoization
    # Time: O(n)
    # Space: O(n)
    def rob_memoization(self, nums: List[int]) -> int:

        memo = {}

        def dfs(i):

            if i < 0:
                return 0

            if i == 0:
                return nums[0]

            if i in memo:
                return memo[i]

            skip = dfs(i - 1)
            rob = nums[i] + dfs(i - 2)

            memo[i] = max(skip, rob)

            return memo[i]

        return dfs(len(nums) - 1)

    # Solution 3: Tabulation
    # Time: O(n)
    # Space: O(n)
    def rob_tabulation(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):

            skip = dp[i - 1]
            rob = nums[i] + dp[i - 2]

            dp[i] = max(skip, rob)

        return dp[-1]

    # Solution 4: Space Optimized
    # Time: O(n)
    # Space: O(1)
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, n):

            skip = prev1
            rob = nums[i] + prev2

            current = max(skip, rob)

            prev2 = prev1
            prev1 = current

        return prev1


if __name__ == "__main__":

    sol = Solution()

    nums = [2, 7, 9, 3, 1]

    print("Recursion        :", sol.rob_recursion(nums))
    print("Memoization      :", sol.rob_memoization(nums))
    print("Tabulation       :", sol.rob_tabulation(nums))
    print("Space Optimized  :", sol.rob(nums))