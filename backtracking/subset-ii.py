"""
LeetCode 90. Subsets II

Topic:
- Backtracking
- Recursion
- Array

Pattern:
- Choose or Skip
- Skip All Duplicates

Idea:
Sort the array first so duplicate values
are placed next to each other.

At each index, there are two choices:

1. Choose the current number.
   - Add it to the current subset.
   - Move to the next index.

2. Skip the current number.
   - Skip all duplicate occurrences
     of the same value.
   - Move directly to the next unique value.

This prevents generating duplicate subsets.

For example:

nums = [1, 2, 2]

When skipping the first 2,
skip both 2s instead of moving
to the second 2.

Remember:

Choose Current Number

↓

Move to Next Index

↓

Backtrack

↓

Skip All Same Numbers

↓

Move to Next Unique Value

Time Complexity: O(n * 2^n)
Space Complexity: O(n)
"""


class Solution:

    def subsetsWithDup(self, nums):

        nums.sort()

        result = []
        current = []

        self.backtrack(
            0,
            nums,
            current,
            result
        )

        return result

    def backtrack(
        self,
        index,
        nums,
        current,
        result
    ):

        if index == len(nums):
            result.append(current.copy())
            return

        # Choice 1:
        # Include the current number.
        current.append(nums[index])

        self.backtrack(
            index + 1,
            nums,
            current,
            result
        )

        current.pop()

        # Choice 2:
        # Skip the current number and
        # all of its duplicate occurrences.
        next_index = index + 1

        while (
            next_index < len(nums)
            and nums[next_index] == nums[index]
        ):
            next_index += 1

        self.backtrack(
            next_index,
            nums,
            current,
            result
        )


if __name__ == "__main__":

    solution = Solution()

    nums = [1, 2, 2]

    result = solution.subsetsWithDup(nums)

    print(result)

    # Output:
    # [
    #   [1, 2, 2],
    #   [1, 2],
    #   [1],
    #   [2, 2],
    #   [2],
    #   []
    # ]