"""
LeetCode 1011. Capacity To Ship Packages Within D Days

Topic:
- Array
- Binary Search

Pattern:
- Binary Search on Answer
- Minimum Valid Answer

Idea:
Search the minimum ship capacity.

For each capacity:
Calculate how many days are needed.

If needed_days <= days:
This capacity works.
Try a smaller capacity.

Otherwise:
Capacity is too small.
Try a larger capacity.

Remember:

Binary Search on Capacity
↓
Calculate Days
↓
Minimum Valid Answer

Time Complexity: O(n log S)

n = len(weights)
S = sum(weights)

Space Complexity: O(1)
"""


from typing import List


class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        while left < right:

            capacity = (left + right) // 2

            needed_days = self.calculateDays(weights, capacity)

            if needed_days <= days:
                right = capacity
            else:
                left = capacity + 1

        return left

    def calculateDays(self, weights: List[int], capacity: int) -> int:

        days = 1
        current_load = 0

        for weight in weights:

            if current_load + weight > capacity:
                days += 1
                current_load = 0

            current_load += weight # remember to add for the last package

        return days
    
if __name__ == "__main__":
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5

    sol = Solution()
    min_capacity = sol.shipWithinDays(weights, days)
    print(f"The minimum ship capacity to ship all packages within {days} days is: {min_capacity}")