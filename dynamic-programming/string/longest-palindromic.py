"""
LeetCode 516. Longest Palindromic Subsequence

Topic:
- Dynamic Programming
- Recursion
- Memoization
- String
- Longest Common Subsequence

Pattern:
- LCS
- String + Reversed String

Idea:
A palindrome reads the same forward and backward.

Reverse the original string.

Then the problem becomes finding the
Longest Common Subsequence (LCS) between:

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

Base Case:

If either index becomes negative,
there are no characters left to match.

Return 0.

Remember:

Reverse the String

↓

Find LCS

↓

Characters Match?

↓

1 + Diagonal

↓

Characters Do Not Match?

↓

Max(Left, Up)

Time Complexity: O(n²)

Space Complexity:
O(n²) + O(n)
"""


class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:

        reverse_s = s[::-1]

        n = len(s)

        dp = [[-1] * n for _ in range(n)]

        return self.func(s, reverse_s, n - 1, n - 1, dp)

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

    s = "bbbab"

    print(solution.longestPalindromeSubseq(s))

    # Output:
    # 4