"""
LeetCode 295. Find Median from Data Stream

Topic:
- Heap
- Priority Queue
- Data Stream

Pattern:
- Two Heaps

Idea:
Maintain two heaps:

1. small (Max Heap)
   Stores the smaller half of the numbers.

2. large (Min Heap)
   Stores the larger half of the numbers.

Python only provides a min heap, so
store negative values in the max heap.

Maintain two invariants:

1. Every element in small
   <= every element in large.

2. The size difference between the
   two heaps is at most 1.

addNum(num):

1. Push the number into the max heap.
2. If the largest value in small is greater
   than the smallest value in large,
   move one element to large.
3. Rebalance the heap sizes.

findMedian():

- If one heap has more elements,
  its top is the median.

- Otherwise, the median is the average
  of both heap tops.

Remember:

Insert into Max Heap

↓

Fix Heap Order

↓

Balance Heap Sizes

↓

Read Median

Time Complexity:
- addNum: O(log n)
- findMedian: O(1)

Space Complexity: O(n)
"""


import heapq


class MedianFinder:

    def __init__(self):

        # Max Heap (store negatives)
        self.small = []

        # Min Heap
        self.large = []

    def addNum(self, num):

        heapq.heappush(
            self.small,
            -num
        )

        if (
            self.small
            and self.large
            and (-self.small[0] > self.large[0])
        ):

            value = -heapq.heappop(self.small)

            heapq.heappush(
                self.large,
                value
            )

        if len(self.small) > len(self.large) + 1:

            value = -heapq.heappop(self.small)

            heapq.heappush(
                self.large,
                value
            )

        elif len(self.large) > len(self.small) + 1:

            value = heapq.heappop(self.large)

            heapq.heappush(
                self.small,
                -value
            )

    def findMedian(self):

        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (
            -self.small[0]
            + self.large[0]
        ) / 2
    
if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())  # 1.5
    medianFinder.addNum(3)
    print(medianFinder.findMedian())  # 2.0