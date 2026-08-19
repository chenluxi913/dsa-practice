"""
LeetCode 1048. Longest String Chain

Topic:
- Dynamic Programming
- String
- Sorting
- Longest Increasing Subsequence

Pattern:
- LIS Style DP
- Two Pointers
- Predecessor Check

Idea:
A word can be added after another word in the
chain if it contains exactly one extra character
while preserving the order of all characters
from the shorter word.

First, sort the words by length.

Then use LIS-style dynamic programming.

Let:

dp[i]

store the length of the longest string chain
ending at words[i].

For every word words[i], check all previous
words words[j].

If words[j] is a predecessor of words[i],
then words[i] can extend the chain ending
at words[j].

Update:

dp[i] = dp[j] + 1

To check whether one word can follow another:

1. The longer word must have exactly one
   extra character.

2. Use two pointers.

3. If the characters match, move both pointers.

4. If they do not match, move only the pointer
   in the longer word.

5. If all characters of the shorter word are
   matched, it is a valid predecessor.

Remember:

Sort Words by Length

↓

LIS Style DP

↓

Check All Previous Words

↓

Longer Word Has One Extra Character?

↓

Two Pointers

↓

Skip One Character from Longer Word

↓

Update dp[i]

↓

Track Maximum Chain Length

Time Complexity: O(n² * L)

Space Complexity: O(n)

L = maximum word length
"""


from typing import List


class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        n = len(words)

        words.sort(key=len)

        # dp[i] stores the length of the longest
        # string chain ending at words[i].
        dp = [1] * n

        max_len = 0

        for i in range(n):

            for prev in range(i):

                if self.checkPossible(words[i], words[prev]) and dp[i] < dp[prev] + 1:
                    dp[i] = dp[prev] + 1

            max_len = max(max_len, dp[i])

        return max_len

    # Function to check whether the shorter word
    # is a predecessor of the longer word.
    def checkPossible(self, longer, shorter):

        if len(longer) != len(shorter) + 1:
            return False

        i = 0
        j = 0

        while i < len(longer):

            if j < len(shorter) and longer[i] == shorter[j]:
                i += 1
                j += 1

            else:
                i += 1

        return j == len(shorter)


if __name__ == "__main__":

    solution = Solution()

    words = ["a", "b", "ba", "bca", "bda", "bdca"]

    print(solution.longestStrChain(words))

    # Output:
    # 4