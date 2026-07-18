"""
LeetCode 39. Combination Sum

Topic:
- Backtracking
- Recursion
- Array

Pattern:
- Choose or Skip

Idea:
Use backtracking to build combinations.

At each index, there are two choices:

1. Choose the current candidate.
   - Add it to the current combination.
   - Subtract it from the remaining target.
   - Stay at the same index because the number
     can be used unlimited times.

2. Skip the current candidate.
   - Move to the next index.

Base cases:

- If remaining_target == 0:
  A valid combination is found.

- If remaining_target < 0:
  The current path is invalid.

- If index reaches the end:
  No more candidates are available.

Using the index prevents duplicate combinations
with different orders.

For example:

[2, 2, 3]

is generated, but:

[2, 3, 2]
[3, 2, 2]

are not generated separately.

Remember:

Choose Current Number

↓

Stay at Same Index

↓

Backtrack

↓

Skip Current Number

↓

Move to Next Index

Time Complexity: O(number of valid and explored combinations)
Space Complexity: O(target / minimum candidate)
"""


class Solution:

    def combinationSum(self, candidates, target):

        result = []

        self.backtrack(
            0,
            candidates,
            target,
            [],
            result
        )

        return result

    def backtrack(
        self,
        index,
        candidates,
        remaining,
        current,
        result
    ):

        if remaining == 0:
            result.append(current.copy())
            return

        if remaining < 0 or index == len(candidates):
            return

        current.append(candidates[index])

        self.backtrack(
            index,
            candidates,
            remaining - candidates[index],
            current,
            result
        )

        current.pop()

        self.backtrack(
            index + 1,
            candidates,
            remaining,
            current,
            result
        )


if __name__ == "__main__":

    solution = Solution()

    candidates = [2, 3, 6, 7]
    target = 7

    print(solution.combinationSum(candidates, target))

    # Output:
    # [[2, 2, 3], [7]]