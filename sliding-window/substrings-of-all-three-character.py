"""
LeetCode 1358. Number of Substrings Containing All Three Characters

Topic:
- String
- Last Seen

Pattern:
- Last Occurrence

Idea:
Keep track of the last seen index
of 'a', 'b', and 'c'.

For each position i:

If all three characters have appeared,

the earliest last seen position determines
how many valid substrings end at i.

Contribution:

min(last_seen) + 1

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:

    def numberOfSubstrings(self, s: str) -> int:

        last_seen = [-1, -1, -1]

        answer = 0

        for i in range(len(s)):

            last_seen[ord(s[i]) - ord("a")] = i

            if (
                last_seen[0] != -1
                and last_seen[1] != -1
                and last_seen[2] != -1
            ):

                answer += min(last_seen) + 1

        return answer

if __name__ == "__main__":
    s = "abcabc"
    solution = Solution()
    result = solution.numberOfSubstrings(s)
    print(result)  # Output: 10