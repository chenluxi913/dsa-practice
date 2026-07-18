"""
LeetCode 40. Combination Sum II

Topic:
- Backtracking
- Recursion
- Array
- Sorting

Pattern:
- Choose or Skip
- Skip All Duplicates

Idea:
Sort the candidates first so duplicate values
are placed next to each other.

At each index, there are two choices:

1. Choose the current candidate.
   - Add it to the current combination.
   - Subtract it from the remaining target.
   - Move to the next index because each
     candidate can only be used once.

2. Skip the current candidate.
   - Skip all duplicate values.
   - Move directly to the next unique candidate.

Base cases:

- If remaining == 0:
  Save the current combination.

- If remaining < 0 or index reaches the end:
  Stop the current path.

Remember:

Sort Candidates

↓

Choose Current Number

↓

Move to Next Index

↓

Backtrack

↓

Skip All Equal Numbers

↓

Move to Next Unique Number

Time Complexity: O(2^n * n)
Space Complexity: O(n)
"""


class Solution:

    def __init__(self):
        self.result = []

    def combinationSum2(self, candidates, target):

        candidates.sort()

        self.result = []

        self.backtrack(
            0,
            target,
            [],
            candidates
        )

        return self.result

    def backtrack(
        self,
        index,
        remaining,
        current,
        candidates
    ):

        if remaining == 0:
            self.result.append(current.copy())
            return

        if remaining < 0 or index == len(candidates):
            return

        # Choice 1:
        # Include the current candidate.
        current.append(candidates[index])

        self.backtrack(
            index + 1,
            remaining - candidates[index],
            current,
            candidates
        )

        current.pop()

        # Choice 2:
        # Skip the current candidate and
        # all of its duplicate occurrences.
        next_index = index + 1

        while (
            next_index < len(candidates)
            and candidates[next_index] == candidates[index]
        ):
            next_index += 1

        self.backtrack(
            next_index,
            remaining,
            current,
            candidates
        )


if __name__ == "__main__":

    solution = Solution()

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    print(solution.combinationSum2(candidates, target))

    # Output:
    # [
    #   [1, 1, 6],
    #   [1, 2, 5],
    #   [1, 7],
    #   [2, 6]
    # ]