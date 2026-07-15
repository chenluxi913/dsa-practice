"""
LeetCode 703. Kth Largest Element in a Stream

Topic:
- Heap
- Priority Queue
- Data Stream

Pattern:
- Maintain Top K Elements

Idea:
Maintain a min heap containing only the
largest k elements seen so far.

Why use a min heap?

Among the largest k elements, the smallest one
is exactly the kth largest element overall.

Initialization:
1. Convert nums into a min heap.
2. Remove the smallest elements until
   only k elements remain.

add(val):
1. Push val into the heap.
2. If the heap size exceeds k,
   remove the smallest element.
3. The heap root is the kth largest element.

Remember:

Keep Only Largest K Elements

↓

Min Heap Root

↓

Kth Largest Element

Time Complexity:
- Constructor: O(n log n)
- add: O(log k)

Space Complexity: O(k)
"""

import heapq


class KthLargest:

    def __init__(self, k, nums):

        self.k = k
        self.min_heap = nums

        heapq.heapify(self.min_heap)

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val):

        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
    
if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))  # returns 4
    print(kthLargest.add(5))  # returns 5
    print(kthLargest.add(10)) # returns 5
    print(kthLargest.add(9))  # returns 8
    print(kthLargest.add(4))  # returns 8