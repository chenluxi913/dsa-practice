"""
LeetCode 132. Palindrome Partitioning II

Topic:
- Dynamic Programming
- Recursion
- Memoization
- String
- Partition DP

Pattern:
- Try Every Partition
- Palindrome Check

Idea:
We need to partition the string so that every
substring in the partition is a palindrome.

Instead of directly counting cuts, count the
minimum number of palindrome partitions.

For every starting index i:

Try every ending index j.

If:

s[i..j]

is a palindrome, then we can make one partition
and recursively solve the remaining string:

j + 1 ... n - 1

So:

cost =
1 + solve(j + 1)

Take the minimum among all possible palindrome
substrings starting at i.

Finally:

Minimum Cuts
=
Minimum Partitions - 1

because k partitions require k - 1 cuts.

Base Case:

If i == n:

There are no characters left.

Return 0.

Remember:

Start at Index i

↓

Try Every End Index j

↓

Is s[i..j] Palindrome?

↓

1 + Solve(j + 1)

↓

Take Minimum Partitions

↓

Answer = Partitions - 1

Time Complexity: O(n^3)

Space Complexity:
O(n) + O(n)
"""


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # palindrome[i][j] = whether s[i:j+1] is palindrome
        palindrome = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = True

        dp = [-1] * n

        return self.minPartitions(0, n, palindrome, dp) - 1

    def minPartitions(self, i, n, palindrome, dp):

        if i == n:
            return 0

        if dp[i] != -1:
            return dp[i]

        min_cost = float("inf")

        for j in range(i, n):

            if palindrome[i][j]:

                cost = 1 + self.minPartitions(j + 1, n, palindrome, dp)

                min_cost = min(min_cost, cost)

        dp[i] = min_cost

        return dp[i]


if __name__ == "__main__":

    solution = Solution()

    s = "aab"

    print(solution.minCut(s))

    # Output:
    # 1