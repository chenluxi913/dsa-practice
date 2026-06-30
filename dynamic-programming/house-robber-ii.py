"""
LeetCode 213. House Robber II

Topic:
- Array
- Dynamic Programming

Pattern:
- House Robber
- Circular Array

Idea:
Same as House Robber I, but houses are in a circle.

Because first and last houses are adjacent,
we cannot rob both.

So split into two cases:

1. Exclude last house
2. Exclude first house

Then run the same House Robber I function.

Remember:
Circle
↓
Break into two lines
↓
Use House Robber I twice

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:

    # Solution 1: Recursion
    def rob_recursion(self, nums):

        if len(nums) == 1:
            return nums[0]

        return max(
            self.rob_line_recursion(nums[:-1]),
            self.rob_line_recursion(nums[1:])
        )

    # Solution 2: Memoization
    def rob_memoization(self, nums):

        if len(nums) == 1:
            return nums[0]

        return max(
            self.rob_line_memoization(nums[:-1]),
            self.rob_line_memoization(nums[1:])
        )

    # Solution 3: Tabulation
    def rob_tabulation(self, nums):

        if len(nums) == 1:
            return nums[0]

        return max(
            self.rob_line_tabulation(nums[:-1]),
            self.rob_line_tabulation(nums[1:])
        )

    # Solution 4: Space Optimized
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        return max(
            self.rob_line(nums[:-1]),
            self.rob_line(nums[1:])
        )
    
    from typing import List

    def rob_line_recursion(self, nums: List[int]) -> int:

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


    def rob_line_memoization(self, nums: List[int]) -> int:

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


    def rob_line_tabulation(self, nums: List[int]) -> int:

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
    def rob_line(self, nums: List[int]) -> int:

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
    nums = [2, 3, 2]
    print(Solution().rob(nums))  # Output: 3

    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))  # Output: 4

    nums = [0]
    print(Solution().rob(nums))  # Output: 0