"""
LeetCode 115. Distinct Subsequences

Topic:
- Dynamic Programming
- Recursion
- Memoization
- String
- Subsequence

Pattern:
- Match or Skip
- Count Subsequences

Idea:
We need to count how many distinct subsequences
of s can form t.

Use two indices:

ind1 = current index in s
ind2 = current index in t

At every state:

If the current characters match:

There are two choices:

1. Use s[ind1] to match t[ind2].
   - Move both indices backward.

2. Skip s[ind1].
   - Move only ind1 backward.

The total number of ways is the sum of both
choices.

If the characters do not match:

We cannot use s[ind1].

The only choice is to skip it and move ind1
backward.

Base Cases:

If ind2 < 0:

All characters of t have been matched.

Return 1.

If ind1 < 0:

s is exhausted before t is fully matched.

Return 0.

Remember:

Characters Match?

↓

Take

+

Skip

↓

Characters Different?

↓

Skip

↓

Count All Ways

Time Complexity: O(n * m)

Space Complexity:
O(n * m) + O(n + m)
"""


class Solution:

    def numDistinct(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)

        dp = [[-1] * m for _ in range(n)]

        return self.func(s, t, n - 1, m - 1, dp)

    # Function to count the number of distinct
    # subsequences of s that can form t.
    def func(self, s, t, ind1, ind2, dp):

        # All characters of t have been matched.
        if ind2 < 0:
            return 1

        # s is exhausted before t is matched.
        if ind1 < 0:
            return 0

        # Return the memoized result.
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # Characters match.
        if s[ind1] == t[ind2]:
            take = self.func(s, t, ind1 - 1, ind2 - 1, dp)
            skip = self.func(s, t, ind1 - 1, ind2, dp)

            dp[ind1][ind2] = take + skip

        # Characters do not match.
        else:
            dp[ind1][ind2] = self.func(s, t, ind1 - 1, ind2, dp)

        return dp[ind1][ind2]


if __name__ == "__main__":

    solution = Solution()

    s = "rabbbit"
    t = "rabbit"

    print(solution.numDistinct(s, t))

    # Output:
    # 3