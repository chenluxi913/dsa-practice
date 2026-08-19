"""
LeetCode 1312. Minimum Insertion Steps to Make a String Palindrome

Topic:
- Dynamic Programming
- Recursion
- Memoization
- String
- Longest Common Subsequence

Pattern:
- Longest Palindromic Subsequence
- LCS with Reversed String

Idea:
To make a string palindrome using insertions,
we want to keep the longest part that is already
palindromic.

The longest part that can remain unchanged is
the Longest Palindromic Subsequence.

Therefore:

Minimum Insertions
=
Length of String
-
Longest Palindromic Subsequence

To find the Longest Palindromic Subsequence,
reverse the string and find the Longest Common
Subsequence between:

s

and

reverse(s)

For every pair of indices:

If the characters match:

1 + solve the previous characters.

Otherwise:

Take the maximum of:

- Skip one character from the first string.
- Skip one character from the second string.

Remember:

Reverse the String

↓

Find LCS

↓

Get Longest Palindromic Subsequence

↓

String Length - LPS

↓

Minimum Insertions

Time Complexity: O(n²)

Space Complexity:
O(n²) + O(n)
"""


class Solution:

    def minInsertions(self, s: str) -> int:

        reverse_s = s[::-1]
        n = len(s)

        dp = [[-1] * n for _ in range(n)]

        lps = self.func(s, reverse_s, n - 1, n - 1, dp)

        return n - lps

    # Function to find the length of the
    # longest common subsequence.
    def func(self, s1, s2, ind1, ind2, dp):

        # Base case.
        if ind1 < 0 or ind2 < 0:
            return 0

        # Return the memoized result.
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # Characters match.
        if s1[ind1] == s2[ind2]:
            dp[ind1][ind2] = 1 + self.func(s1, s2, ind1 - 1, ind2 - 1, dp)

        # Characters do not match.
        else:
            dp[ind1][ind2] = max(self.func(s1, s2, ind1 - 1, ind2, dp), self.func(s1, s2, ind1, ind2 - 1, dp))

        return dp[ind1][ind2]


if __name__ == "__main__":

    solution = Solution()

    s = "mbadm"

    print(solution.minInsertions(s))

    # Output:
    # 2