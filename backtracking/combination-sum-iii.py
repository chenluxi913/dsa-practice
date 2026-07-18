"""
LeetCode 216. Combination Sum III

Topic:
- Backtracking
- Recursion
- Combination

Pattern:
- Choose or Skip

Idea:
Choose exactly k distinct numbers from 1 to 9
such that their sum equals n.

At each number, there are two choices:

1. Choose the current number.
   - Add it to the current combination.
   - Subtract it from the remaining target.
   - Move to the next number.

2. Skip the current number.
   - Move to the next number.

A combination is valid only when:

- remaining == 0
- len(current) == k

Since numbers are explored from small to large,
every combination is generated in increasing order,
so duplicate combinations are avoided.

Remember:

Start from 1

↓

Choose Current Number

↓

Move to Next Number

↓

Backtrack

↓

Skip Current Number

↓

Save When:
remaining == 0
and length == k

Time Complexity: O(2^9)
Space Complexity: O(k)
"""


class Solution:

    def combinationSum3(self, k, n):

        result = []

        self.backtrack(
            1,
            k,
            n,
            [],
            result
        )

        return result

    def backtrack(
        self,
        number,
        k,
        remaining,
        current,
        result
    ):

        if remaining == 0 and len(current) == k:
            result.append(current.copy())
            return

        if (
            remaining < 0
            or len(current) > k
            or number > 9
        ):
            return

        # Choice 1:
        # Include the current number.
        current.append(number)

        self.backtrack(
            number + 1,
            k,
            remaining - number,
            current,
            result
        )

        current.pop()

        # Choice 2:
        # Skip the current number.
        self.backtrack(
            number + 1,
            k,
            remaining,
            current,
            result
        )


if __name__ == "__main__":

    solution = Solution()

    print(solution.combinationSum3(3, 9))

    # Output:
    # [
    #   [1, 2, 6],
    #   [1, 3, 5],
    #   [2, 3, 4]
    # ]