"""
LeetCode 55. Jump Game

Topic:
- Greedy
- Array

Pattern:
- Track the Farthest Reachable Index

Idea:
Start from the first index.

Maintain the farthest index that can
currently be reached.

For every index:

1. If the current index is beyond the
   farthest reachable position,
   the last index cannot be reached.

2. Otherwise, update the farthest
   reachable position.

If the entire array is traversed,
the last index is reachable.

Remember:

Start at Index 0

↓

Current Index Reachable?

↓

Update Farthest Reach

↓

Cannot Reach Current Index → False

↓

Finish Traversal → True

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:

    def canJump(self, nums):

        farthest = 0

        for index in range(len(nums)):

            # The current index
            # cannot be reached.
            if index > farthest:
                return False

            # Update the farthest
            # reachable index.
            farthest = max(
                farthest,
                index + nums[index]
            )

        return True


if __name__ == "__main__":

    solution = Solution()

    print(solution.canJump([2, 3, 1, 1, 4]))   # True
    print(solution.canJump([3, 2, 1, 0, 4]))   # False