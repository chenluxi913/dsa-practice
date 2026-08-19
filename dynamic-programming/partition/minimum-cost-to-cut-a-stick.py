"""
LeetCode 1547. Minimum Cost to Cut a Stick

Topic:
- Dynamic Programming
- Recursion
- Memoization
- Interval DP
- Partition DP

Pattern:
- Try Every Possible Cut
- Solve Left and Right Intervals

Idea:
The cost of each cut is the length of the
current stick segment being cut.

Because the order of cuts changes the segment
lengths, we must try different cut orders.

Add the two boundaries:

0
n

to the cuts array and sort it.

For a current interval from i to j:

cuts[i - 1]

is the left boundary.

cuts[j + 1]

is the right boundary.

Try every possible cut ind between i and j.

If we cut at ind:

Current cut cost:

cuts[j + 1] - cuts[i - 1]

Then solve:

Left interval:
i to ind - 1

Right interval:
ind + 1 to j

Total cost:

current cut cost
+
left cost
+
right cost

Take the minimum among all possible cuts.

Base Case:

If i > j:

There are no cuts left to perform.

Return 0.

Remember:

Add 0 and n

↓

Sort Cuts

↓

Choose Interval i ... j

↓

Try Every Cut ind

↓

Current Cost =
cuts[j + 1] - cuts[i - 1]

↓

Solve Left

+

Solve Right

↓

Take Minimum

Time Complexity: O(c^3)

Space Complexity:
O(c^2) + O(c)

c = number of cuts
"""


from typing import List


class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:

        c = len(cuts)

        # Add the two boundaries and
        # sort all cut positions.
        cuts = [0] + sorted(cuts) + [n]

        # dp[i][j] stores the minimum cost
        # to perform all cuts from i to j.
        dp = [[-1] * (c + 2) for _ in range(c + 2)]

        return self.func(1, c, cuts, dp)

    # Function to calculate the minimum
    # cost for the current interval.
    def func(self, i, j, cuts, dp):

        # Base case.
        if i > j:
            return 0

        # Return the memoized result.
        if dp[i][j] != -1:
            return dp[i][j]

        minimum = float("inf")

        # Try every possible cut
        # in the current interval.
        for ind in range(i, j + 1):

            cost = cuts[j + 1] - cuts[i - 1] + self.func(i, ind - 1, cuts, dp) + self.func(ind + 1, j, cuts, dp)

            minimum = min(minimum, cost)

        dp[i][j] = minimum

        return dp[i][j]


if __name__ == "__main__":

    solution = Solution()

    n = 7
    cuts = [1, 3, 4, 5]

    print(solution.minCost(n, cuts))

    # Output:
    # 16