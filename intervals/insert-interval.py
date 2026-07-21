"""
LeetCode 57. Insert Interval

Topic:
- Greedy
- Array
- Intervals

Pattern:
- Add Left Intervals
- Merge Overlapping Intervals
- Add Right Intervals

Idea:
The intervals are already sorted and
do not overlap.

Process the intervals in three stages:

1. Add all intervals completely before
   the new interval.

2. Merge all intervals that overlap
   with the new interval.

3. Add all remaining intervals completely
   after the merged interval.

Two intervals overlap when:

current_start <= new_end

While merging:

new_start = min(new_start, current_start)

new_end = max(new_end, current_end)

Remember:

Add Left Intervals

↓

Merge Overlapping Intervals

↓

Add Merged Interval

↓

Add Remaining Intervals

Time Complexity: O(n)
Space Complexity: O(n)

The extra working space is O(1),
excluding the returned result.
"""


class Solution:

    def insert(self, intervals, newInterval):

        result = []

        index = 0
        n = len(intervals)

        # Add intervals completely before newInterval.
        while (
            index < n
            and intervals[index][1] < newInterval[0]
        ):
            result.append(intervals[index])
            index += 1

        # Merge overlapping intervals.
        while (
            index < n
            and intervals[index][0] <= newInterval[1]
        ):
            newInterval[0] = min(
                newInterval[0],
                intervals[index][0]
            )

            newInterval[1] = max(
                newInterval[1],
                intervals[index][1]
            )

            index += 1

        # Add the merged interval.
        result.append(newInterval)

        # Add the remaining intervals.
        while index < n:
            result.append(intervals[index])
            index += 1

        return result


if __name__ == "__main__":

    solution = Solution()

    print(
        solution.insert(
            [[1, 3], [6, 9]],
            [2, 5]
        )
    )

    # Output:
    # [[1, 5], [6, 9]]

    print(
        solution.insert(
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8]
        )
    )

    # Output:
    # [[1, 2], [3, 10], [12, 16]]