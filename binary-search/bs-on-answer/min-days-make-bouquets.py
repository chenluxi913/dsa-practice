"""
LeetCode 1482. Minimum Number of Days to Make m Bouquets

Topic:
- Array
- Binary Search

Pattern:
- Binary Search on Answer

Idea:
Search the minimum number of days.

For a given day,
check if we can make at least m bouquets.

A flower can be used if:

bloomDay[i] <= day

We need k adjacent bloomed flowers
to make one bouquet.

Remember:

Binary Search on Days

↓

Check Bouquets

↓

Minimum Valid Answer

Time Complexity: O(n log M)

n = len(bloomDay)
M = max(bloomDay)

Space Complexity: O(1)
"""

class Solution:
    def possible(self, bloomDay, day, m, k):
        count = 0
        bouquets = 0

        for bloom in bloomDay:
            if bloom <= day:
                count += 1
            else:
                bouquets += count // k
                count = 0

        bouquets += count // k

        return bouquets >= m

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            day = (left + right) // 2

            if self.possible(bloomDay, day, m, k):
                right = day
            else:
                left = day + 1

        return left
    
if __name__ == "__main__":
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1

    sol = Solution()
    print(sol.minDays(bloomDay, m, k))