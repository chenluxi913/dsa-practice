"""
LeetCode 56. Merge Intervals

Topic:
- Array
- Sorting
- Intervals

Pattern:
- Sort + Merge Intervals

Idea:
1. Sort intervals by start time.
2. Add the first interval to the result.
3. Compare each interval with the last merged interval.
4. If they overlap, merge them.
5. Otherwise, add the current interval.

Overlap:
current_start <= previous_end

Remember:

Sort
↓

Compare

↓

Merge

or

Append

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        merged = []

        for interval in intervals:
            # no overlap: last merged interval's end < current interval's start
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # update the end of the last merged interval
                merged[-1][1] = max(
                    merged[-1][1],
                    interval[1]
                )

        return merged
    
if __name__ == "__main__":
    solution = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution.merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]