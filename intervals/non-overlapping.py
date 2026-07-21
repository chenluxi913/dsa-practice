"""
LeetCode 435. Non-overlapping Intervals

Topic:
- Greedy
- Sorting
- Intervals

Pattern:
- Activity Selection

Idea:
Instead of directly counting the intervals
to remove, maximize the number of
non-overlapping intervals kept.

Sort the intervals by their ending times.

Always keep the interval that finishes
earliest because it leaves the most room
for future intervals.

If the next interval starts after or at
the current ending time,
keep it.

Otherwise,
skip it.

The answer is:

total intervals
-
maximum non-overlapping intervals

Remember:

Sort by Ending Time

↓

Keep Earliest Ending Interval

↓

Next Start >= Current End

↓

Keep It

↓

Answer = Total - Kept

Time Complexity: O(n log n)
Space Complexity: O(1)

The sorting space depends on the language implementation.
"""


class Solution:

    def eraseOverlapIntervals(self, intervals):

        intervals.sort(
            key=lambda interval: interval[1]
        )

        kept = 1

        current_end = intervals[0][1]

        for index in range(1, len(intervals)):

            if intervals[index][0] >= current_end:

                kept += 1
                current_end = intervals[index][1]

        return len(intervals) - kept


if __name__ == "__main__":

    solution = Solution()

    print(
        solution.eraseOverlapIntervals(
            [[1, 2], [2, 3], [3, 4], [1, 3]]
        )
    )

    # Output:
    # 1

    print(
        solution.eraseOverlapIntervals(
            [[1, 2], [1, 2], [1, 2]]
        )
    )

    # Output:
    # 2

    print(
        solution.eraseOverlapIntervals(
            [[1, 2], [2, 3]]
        )
    )

    # Output:
    # 0