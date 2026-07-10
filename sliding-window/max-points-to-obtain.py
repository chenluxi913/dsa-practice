"""
LeetCode 1423. Maximum Points You Can Obtain from Cards

Topic:
- Array
- Sliding Window

Pattern:
- Fixed Size Sliding Window

Idea:
Initially take all k cards from the left.

Then gradually replace one left card
with one right card.

Keep updating the maximum score.

Remember:

Take All from Left

↓

Move One Card
Left → Right

↓

Update Maximum

Time Complexity: O(k)
Space Complexity: O(1)
"""


from typing import List


class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:

        left_sum = sum(cardPoints[:k])
        right_sum = 0

        max_score = left_sum

        right = len(cardPoints) - 1

        for left in range(k - 1, -1, -1):

            left_sum -= cardPoints[left]
            right_sum += cardPoints[right]

            right -= 1

            max_score = max(max_score, left_sum + right_sum)

        return max_score