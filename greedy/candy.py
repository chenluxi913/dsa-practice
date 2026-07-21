"""
LeetCode 135. Candy

Topic:
- Greedy
- Array

Pattern:
- Peak and Valley

Idea:
Every child receives at least one candy.

Process the ratings as three types of segments:

1. Equal ratings
   Give one candy.

2. Increasing ratings
   Increase the candy count by one each step.

3. Decreasing ratings
   Count the downhill length.

The peak child belongs to both the increasing
and decreasing sequences.

If the decreasing sequence is longer than
the increasing sequence, the peak child does
not have enough candies.

Add the difference:

down - peak

to fix the peak.

Remember:

Start with One Candy

↓

Equal Rating → One Candy

↓

Increasing Sequence

↓

Decreasing Sequence

↓

Adjust Peak If Needed

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:

    def candy(self, ratings):

        n = len(ratings)

        index = 1

        # First child receives one candy.
        total = 1

        while index < n:

            # Equal ratings.
            if ratings[index] == ratings[index - 1]:

                total += 1
                index += 1
                continue

            # Increasing sequence.
            peak = 1

            while (
                index < n
                and ratings[index] > ratings[index - 1]
            ):

                peak += 1
                total += peak
                index += 1

            # Decreasing sequence.
            down = 1

            while (
                index < n
                and ratings[index] < ratings[index - 1]
            ):

                total += down
                down += 1
                index += 1

            # The peak belongs to both sequences.
            # Increase its candies if necessary.
            if down > peak:

                total += down - peak

        return total


if __name__ == "__main__":

    solution = Solution()

    print(solution.candy([1, 0, 2]))     # 5
    print(solution.candy([1, 2, 2]))     # 4