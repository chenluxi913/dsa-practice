"""
LeetCode 846. Hand of Straights

Topic:
- Greedy
- Hash Map
- Heap

Pattern:
- Build Consecutive Groups from Smallest Card

Idea:
Each group must contain groupSize consecutive cards.

Always start from the smallest remaining card.

1. Count the frequency of every card.
2. Put all distinct card values into a min heap.
3. Take the smallest card as the start of a group.
4. Try to use:

   first, first + 1, ..., first + groupSize - 1

5. Decrease each card's frequency.
6. When a frequency becomes zero, that card must
   be the smallest value currently in the heap.
7. Remove exhausted values from the heap.

If any required consecutive card is missing,
return False.

Remember:

Count Frequencies

↓

Get Smallest Remaining Card

↓

Build Consecutive Group

↓

Decrease Counts

↓

Remove Exhausted Cards in Heap Order

Time Complexity: O(n log m)
Space Complexity: O(m)

where m is the number of distinct card values.
"""


import heapq


class Solution:

    def isNStraightHand(self, hand, groupSize):

        if len(hand) % groupSize != 0:
            return False

        count = {}

        for card in hand:
            count[card] = count.get(card, 0) + 1

        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:

            first = min_heap[0]

            for card in range(first, first + groupSize):

                if card not in count:
                    return False

                count[card] -= 1

                if count[card] == 0:

                    if card != min_heap[0]:
                        return False

                    heapq.heappop(min_heap)

        return True
    
if __name__ == "__main__":
    solution = Solution()

    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    print(solution.isNStraightHand(hand, groupSize))  # True

    hand = [1, 2, 3, 4, 5]
    groupSize = 4
    print(solution.isNStraightHand(hand, groupSize))  # False