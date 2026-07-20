"""
LeetCode 45. Jump Game II

Topic:
- Greedy
- Array

Pattern:
- Greedy BFS Level Traversal

Idea:
Treat every jump as one BFS level.

Maintain:

current_end
    The farthest index reachable using
    the current number of jumps.

farthest
    The farthest index reachable from
    every position inside the current level.

Algorithm:

For every index:

1. Update the farthest reachable index.

2. If we have reached the end of the
   current level:

   - We must make one more jump.
   - Expand the level to farthest.

Why Greedy Works:

At each jump, we consider every position
that can currently be reached.

Among all of them, we choose the one
that extends our reachable range the most.

Since every position inside the current
range costs the same number of jumps,
taking the farthest reachable boundary
always minimizes the total jumps.

Example:

nums = [2,3,1,1,4]

Jump 0:
Range = [0]
Reach = 2

Jump 1:
Range = [1,2]
Reach = 4

Jump 2:
Reach the end.

Answer = 2

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        current_end = 0
        farthest = 0

        # No need to process the last index
        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            # Finish exploring the current level
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps