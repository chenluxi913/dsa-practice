"""
LeetCode 875. Koko Eating Bananas

Topic:
- Array
- Binary Search

Pattern:
- Binary Search on Answer

Idea:
Search the minimum eating speed.

Search range:
left = 1
right = max(piles)

For each speed:

Calculate how many hours Koko needs.

If hours <= h:
Current speed works.
Try a smaller speed.

Otherwise:
Need a faster speed.

Remember:

Binary Search on Speed

↓

Calculate Hours

↓

Shrink Search Space

Time Complexity: O(n log M)

n = number of piles
M = max(piles)

Space Complexity: O(1)
"""


from ast import List


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left < right:

            speed = (left + right) // 2

            hours =self.calculate_hours(piles, speed)

            if hours <= h:
                # Current speed works. Try a smaller speed. keep the answer.
                right = speed
            else:
                left = speed + 1

        return left
    
    def calculate_hours(self, piles: List[int], speed: int) -> int:
        hours = 0

        for pile in piles:
            # Calculate hours needed for each pile ceiling division
            hours += (pile + speed - 1) // speed

        return hours
    
if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8

    sol = Solution()
    print(sol.minEatingSpeed(piles, h))