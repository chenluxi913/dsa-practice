"""
LeetCode 23. Merge k Sorted Lists

Topic:
- Linked List
- Heap
- Priority Queue

Pattern:
- K-Way Merge

Idea:
Each linked list is already sorted.

Use a min heap to always retrieve the
smallest current node among all lists.

Initialization:

- Push the head node of every non-empty
  linked list into the heap.

Each heap element stores:

(node.val, list_index, node)

The list index is used to break ties when
two nodes have the same value because
ListNode objects cannot be compared directly.

For each step:

1. Pop the smallest node.
2. Append it to the merged list.
3. If the node has a next node,
   push the next node into the heap.
4. Repeat until the heap becomes empty.

Remember:

Push All List Heads

↓

Pop Smallest Node

↓

Append to Result

↓

Push Next Node

↓

Repeat

Time Complexity: O(n log k)
Space Complexity: O(k)

where:
- n is the total number of nodes
- k is the number of linked lists.
"""


import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists):

        min_heap = []

        for index, node in enumerate(lists):

            if node:

                heapq.heappush(
                    min_heap,
                    (node.val, index, node)
                )

        dummy = ListNode()

        tail = dummy

        while min_heap:

            value, index, node = heapq.heappop(min_heap)

            tail.next = node
            tail = tail.next

            if node.next:

                heapq.heappush(
                    min_heap,
                    (
                        node.next.val,
                        index,
                        node.next
                    )
                )

        return dummy.next
    
if __name__ == "__main__":
    # Example usage:
    # Create linked lists for testing
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    lists = [list1, list2, list3]

    solution = Solution()
    merged_head = solution.mergeKLists(lists)

    # Print the merged linked list
    current = merged_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")