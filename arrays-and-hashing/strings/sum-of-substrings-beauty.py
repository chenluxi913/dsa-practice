"""
LeetCode 1781. Sum of Beauty of All Substrings

Topic:
- String
- Hash Map

Pattern:
- Enumerate Substrings
- Frequency Counting

Idea:

Loop through all possible substrings.

For each starting position:

Maintain a frequency map while extending
the ending position.

For every substring:

1. Update the frequency of the new character.
2. Find the maximum frequency.
3. Find the minimum non-zero frequency.
4. Compute the beauty.

Beauty =
Maximum Frequency
-
Minimum Frequency

Add the beauty to the answer.

Remember:

Fix Start

↓

Extend End

↓

Update Frequency

↓

Calculate Beauty

↓

Add to Answer

Time Complexity: O(n² * 26)

Space Complexity: O(26) = O(1)
"""


class Solution:
    def beautySum(self, s: str) -> int:

        n = len(s)
        total = 0

        for start in range(n):

            freq = {}

            for end in range(start, n):

                freq[s[end]] = freq.get(s[end], 0) + 1

                values = freq.values()

                maximum = max(values)
                minimum = min(values)

                total += maximum - minimum

        return total
    
if __name__ == "__main__":
    solution = Solution()
    s = "aabcb"
    print(solution.beautySum(s))  # Output: 5