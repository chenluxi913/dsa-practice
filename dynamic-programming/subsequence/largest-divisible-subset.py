"""
LeetCode 368. Largest Divisible Subset

Topic:
- Dynamic Programming
- Array
- Sorting
- Longest Increasing Subsequence

Pattern:
- LIS Style DP
- Parent Tracking
- Backtracking

Idea:
We need to find the largest subset where every
pair of elements is divisible by one another.

First, sort the array.

After sorting, if:

nums[i] % nums[prev] == 0

then nums[prev] can come before nums[i]
in the divisible subset.

Use:

dp[i]

to store the length of the largest divisible
subset ending at index i.

Use:

parent[i]

to store the previous index in that subset.

For every index i, check all previous indices.

If nums[i] is divisible by nums[prev] and
including nums[prev] gives a longer subset:

Update dp[i].

Also store prev as the parent of i.

After filling the DP array, find the index where
the largest divisible subset ends.

Then backtrack through the parent array to
reconstruct the subset.

Remember:

Sort the Array

↓

LIS Style DP

↓

Check Divisibility

↓

Update Length

↓

Store Parent

↓

Find Maximum Length

↓

Backtrack

↓

Reverse the Result

Time Complexity: O(n²)

Space Complexity: O(n)
"""


from typing import List


class Solution:

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        n = len(nums)

        nums.sort()

        # To store the result.
        ans = []

        # dp[i] stores the length of the largest
        # divisible subset ending at index i.
        dp = [1] * n

        # parent[i] stores the previous index
        # in the divisible subset.
        parent = [0] * n

        # Index of the last element
        # in the largest subset.
        last_index = 0

        # Maximum length found.
        max_len = 0

        # Compute the DP array.
        for i in range(n):

            parent[i] = i

            # Check all previous indices.
            for prev in range(i):

                if nums[i] % nums[prev] == 0 and dp[i] < dp[prev] + 1:
                    dp[i] = dp[prev] + 1
                    parent[i] = prev

            # Update the largest subset.
            if dp[i] > max_len:
                max_len = dp[i]
                last_index = i

        # Backtrack to reconstruct the subset.
        i = last_index

        while parent[i] != i:
            ans.append(nums[i])
            i = parent[i]

        ans.append(nums[i])

        # The subset was built backwards.
        ans.reverse()

        return ans


if __name__ == "__main__":

    solution = Solution()

    nums = [1, 2, 4, 8]

    print(solution.largestDivisibleSubset(nums))

    # Output:
    # [1, 2, 4, 8]