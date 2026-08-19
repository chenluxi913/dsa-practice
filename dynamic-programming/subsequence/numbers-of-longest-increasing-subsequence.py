"""
LeetCode 673. Number of Longest Increasing Subsequence

Topic:
- Dynamic Programming
- Array
- Longest Increasing Subsequence

Pattern:
- LIS
- Count Number of Optimal Subsequences

Idea:
We need to find not only the length of the
Longest Increasing Subsequence, but also how
many LIS sequences exist.

Use two arrays:

dp[i]

stores the length of the longest increasing
subsequence ending at index i.

count[i]

stores the number of longest increasing
subsequences ending at index i.

dp[i]
= 以 nums[i] 结尾的 LIS 最大长度

count[i]
= 以 nums[i] 结尾、长度为 dp[i] 的 LIS 有多少个

Initially:

dp[i] = 1

because every element itself forms an increasing
subsequence of length 1.

count[i] = 1

because there is one way to form that
subsequence.

For every index i, check all previous indices.

If:

nums[prev] < nums[i]

then nums[i] can extend the increasing
subsequence ending at prev.

There are two cases:

1. A longer subsequence is found:

dp[prev] + 1 > dp[i]

Update:

dp[i] = dp[prev] + 1

count[i] = count[prev]

2. Another subsequence with the same
maximum length is found:

dp[prev] + 1 == dp[i]

Add the number of ways:

count[i] += count[prev]

After filling the arrays, find the maximum
LIS length.

Then add count[i] for every index where:

dp[i] == max_len

Remember:

Initialize

dp[i] = 1
count[i] = 1

↓

Check All Previous Indices

↓

nums[prev] < nums[i] ?

↓

Longer LIS Found?

↓

Copy count[prev]

↓

Same Length LIS Found?

↓

Add count[prev]

↓

Find Maximum LIS Length

↓

Sum Counts of All LIS Endings

Time Complexity: O(n²)

Space Complexity: O(n)
"""


from typing import List


class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        # dp[i] stores the length of the LIS
        # ending at index i.
        dp = [1] * n

        # count[i] stores the number of LIS
        # ending at index i.
        count = [1] * n

        max_len = 1

        # Compute the LIS length and count.
        for i in range(n):

            for prev in range(i):

                if nums[prev] < nums[i]:

                    # A longer LIS is found.
                    if dp[prev] + 1 > dp[i]:
                        dp[i] = dp[prev] + 1
                        count[i] = count[prev]

                    # Another LIS with the
                    # same length is found.
                    elif dp[prev] + 1 == dp[i]:
                        count[i] += count[prev]

            max_len = max(max_len, dp[i])

        result = 0

        # Count all subsequences with
        # the maximum LIS length.
        for i in range(n):

            if dp[i] == max_len:
                result += count[i]

        return result


if __name__ == "__main__":

    solution = Solution()

    nums = [1, 3, 5, 4, 7]

    print(solution.findNumberOfLIS(nums))

    # Output:
    # 2