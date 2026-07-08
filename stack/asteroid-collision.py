"""
LeetCode 735. Asteroid Collision

Topic:
- Array
- Stack

Pattern:
- Stack Simulation

Idea:
Traverse each asteroid.

1. If it moves right, push it into the stack.

2. If it moves left:
   - Destroy all smaller right-moving asteroids.
   - If an equal-sized right-moving asteroid exists,
     destroy both.
   - Otherwise, if no collision is possible,
     push the current asteroid.

Remember:

Right →
Push

↓

Left ←

↓

Destroy Smaller

↓

Equal Destroy Both

↓

Push Survivor

Time Complexity: O(n)

Space Complexity: O(n)
"""


from typing import List


class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:

            # Right-moving asteroid
            if asteroid > 0:
                stack.append(asteroid)

            # Left-moving asteroid
            else:

                # Destroy all smaller right-moving asteroids
                while (
                    stack
                    and stack[-1] > 0
                    and stack[-1] < abs(asteroid)
                ):
                    stack.pop()

                # Same size: destroy both
                if (
                    stack
                    and stack[-1] == abs(asteroid)
                ):
                    stack.pop()

                # No collision possible
                elif (
                    not stack
                    or stack[-1] < 0
                ):
                    stack.append(asteroid)

        return stack
    
if __name__ == "__main__":
    solution = Solution()
    asteroids = [5, 10, -5, -10, 15]
    print(solution.asteroidCollision(asteroids))  # Output: [5, 10]