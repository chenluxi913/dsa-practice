"""
LeetCode 237. Delete Node in a Linked List

Topic:
- Linked List

Pattern:
- Copy Next Node

Idea:
We are not given head, so we cannot find the previous node.

Instead:
1. Copy the next node's value into current node.
2. Skip the next node.

This makes the current node look like the next node,
and removes the next node from the list.

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == "__main__":
    # Test case
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    # Create a linked list: 4 -> 5 -> 1 -> 9
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)

    # Delete node with value 5
    node_to_delete = head.next  # Node with value 5
    Solution().deleteNode(node_to_delete)

    # Print the modified linked list: should be 4 -> 1 -> 9
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next