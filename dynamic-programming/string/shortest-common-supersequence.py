"""
LeetCode 1092. Shortest Common Supersequence

Topic:
- Dynamic Programming
- String
- Longest Common Subsequence
- Backtracking

Pattern:
- LCS
- Build Answer from DP Table

Idea:
We need the shortest string that contains both
str1 and str2 as subsequences.

The common characters between the two strings
should only be included once.

Therefore, first find the Longest Common
Subsequence using a DP table.

Then backtrack through the DP table to build
the Shortest Common Supersequence.

If the characters match:

Add the character once and move diagonally.

If the characters do not match:

Compare the LCS values from:

dp[i - 1][j]

and

dp[i][j - 1]

Move in the direction with the larger LCS value
and add the corresponding character.

After one string is exhausted, add all remaining
characters from the other string.

Since the answer is built backwards,
reverse it before returning.

Remember:

Build LCS DP Table

↓

Start from Bottom-Right

↓

Characters Match?

↓

Add Once + Move Diagonal

↓

Characters Different?

↓

Follow Larger LCS Value

↓

Add Remaining Characters

↓

Reverse the Result

Time Complexity: O(n * m)

Space Complexity: O(n * m)
"""


class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n = len(str1)
        m = len(str2)

        # dp[i][j] stores the length of the
        # LCS between str1[:i] and str2[:j].
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Build the LCS DP table.
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):

                if str1[ind1 - 1] == str2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]

                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        i = n
        j = m

        result = []

        # Build the shortest common supersequence.
        while i > 0 and j > 0:

            # Characters match.
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1

            # Take from str1.
            elif dp[i - 1][j] > dp[i][j - 1]:
                result.append(str1[i - 1])
                i -= 1

            # Take from str2.
            else:
                result.append(str2[j - 1])
                j -= 1

        # Add remaining characters from str1.
        while i > 0:
            result.append(str1[i - 1])
            i -= 1

        # Add remaining characters from str2.
        while j > 0:
            result.append(str2[j - 1])
            j -= 1

        # The result was built backwards.
        result.reverse()

        return "".join(result)


if __name__ == "__main__":

    solution = Solution()

    str1 = "abac"
    str2 = "cab"

    print(solution.shortestCommonSupersequence(str1, str2))

    # Output:
    # "cabac"