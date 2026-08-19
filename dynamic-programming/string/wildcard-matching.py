"""
LeetCode 44. Wildcard Matching

Topic:
- Dynamic Programming
- Recursion
- Memoization
- String

Pattern:
- Match or Skip
- Wildcard Matching

Idea:
We need to determine whether the entire string
matches the entire pattern.

The pattern contains two special characters:

'?' matches exactly one character.

'*' matches any sequence of characters,
including the empty sequence.

Use two indices:

ind1 = current index in s
ind2 = current index in p

At every state:

If the characters match, or p[ind2] == '?':

Move both indices backward.

If p[ind2] == '*':

There are two choices:

1. '*' matches one or more characters.
   - Move ind1 backward.
   - Keep ind2 at '*'.

2. '*' matches the empty sequence.
   - Keep ind1 unchanged.
   - Move ind2 backward.

If neither condition is satisfied:

Return False.

Base Cases:

If both s and p are exhausted:

Return True.

If p is exhausted but s is not:

Return False.

If s is exhausted:

The remaining pattern must contain only '*'
characters to match the empty string.

Remember:

Characters Match
or '?'

↓

Move Both Indices

↓

Pattern Is '*'

↓

Match One Character

OR

Match Empty Sequence

↓

Return True if Either Choice Works

Time Complexity: O(n * m)

Space Complexity:
O(n * m) + O(n + m)
"""


class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)

        dp = [[-1] * m for _ in range(n)]

        return self.func(s, p, n - 1, m - 1, dp)

    # Function to check whether the string
    # matches the wildcard pattern.
    def func(self, s, p, ind1, ind2, dp):

        # Both string and pattern are exhausted.
        if ind1 < 0 and ind2 < 0:
            return True

        # Pattern is exhausted but string remains.
        if ind2 < 0 and ind1 >= 0:
            return False

        # String is exhausted.
        if ind1 < 0 and ind2 >= 0:

            # The remaining pattern must
            # contain only '*'.
            for i in range(ind2 + 1):
                if p[i] != '*':
                    return False

            return True

        # Return the memoized result.
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # Characters match or '?' matches
        # any single character.
        if s[ind1] == p[ind2] or p[ind2] == '?':
            dp[ind1][ind2] = self.func(s, p, ind1 - 1, ind2 - 1, dp)

        # '*' can match zero or more characters.
        elif p[ind2] == '*':
            dp[ind1][ind2] = self.func(s, p, ind1 - 1, ind2, dp) or self.func(s, p, ind1, ind2 - 1, dp)

        # Characters do not match.
        else:
            dp[ind1][ind2] = False

        return dp[ind1][ind2]


if __name__ == "__main__":

    solution = Solution()

    s = "aa"
    p = "*"

    print(solution.isMatch(s, p))

    # Output:
    # True