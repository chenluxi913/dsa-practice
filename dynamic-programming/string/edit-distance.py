"""
LeetCode 72. Edit Distance

Topic:
- Dynamic Programming
- Recursion
- Memoization
- String

Pattern:
- Match or Edit
- Insert / Delete / Replace

Idea:
We want to convert word1 into word2 using the
minimum number of operations.

At every pair of indices:

If the characters match:

No operation is needed.

Move both indices to the previous characters.

If the characters do not match, there are
three possible operations:

1. Insert
   - Insert word2[ind2] into word1.
   - Keep ind1 unchanged.
   - Move ind2 backward.

2. Delete
   - Delete word1[ind1].
   - Move ind1 backward.
   - Keep ind2 unchanged.

3. Replace
   - Replace word1[ind1] with word2[ind2].
   - Move both indices backward.

Take the minimum among the three choices
and add 1 for the current operation.

Base Cases:

If word1 is exhausted:

Insert all remaining characters from word2.

Return ind2 + 1.

If word2 is exhausted:

Delete all remaining characters from word1.

Return ind1 + 1.

Remember:

Characters Match?

↓

Move Both Indices

↓

Characters Different?

↓

Insert

or

Delete

or

Replace

↓

1 + Minimum of Three Choices

Time Complexity: O(n * m)

Space Complexity:
O(n * m) + O(n + m)
"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        dp = [[-1] * m for _ in range(n)]

        return self.func(word1, word2, n - 1, m - 1, dp)

    # Function to find the minimum number of
    # operations to convert s1 into s2.
    def func(self, s1, s2, ind1, ind2, dp):

        # If s1 is exhausted, insert all
        # remaining characters from s2.
        if ind1 < 0:
            return ind2 + 1

        # If s2 is exhausted, delete all
        # remaining characters from s1.
        if ind2 < 0:
            return ind1 + 1

        # Return the memoized result.
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # Characters match.
        if s1[ind1] == s2[ind2]:
            dp[ind1][ind2] = self.func(s1, s2, ind1 - 1, ind2 - 1, dp)

        # Characters do not match.
        else:
            insert = self.func(s1, s2, ind1, ind2 - 1, dp)
            delete = self.func(s1, s2, ind1 - 1, ind2, dp)
            replace = self.func(s1, s2, ind1 - 1, ind2 - 1, dp)

            dp[ind1][ind2] = 1 + min(insert, delete, replace)

        return dp[ind1][ind2]


if __name__ == "__main__":

    solution = Solution()

    word1 = "horse"
    word2 = "ros"

    print(solution.minDistance(word1, word2))

    # Output:
    # 3