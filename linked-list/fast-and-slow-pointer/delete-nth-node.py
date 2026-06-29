"""
LeetCode 19. Remove Nth Node From End of List

Topic:
- Linked List
- Two Pointers

Pattern:
- Fast & Slow Pointer

Idea:
Use a dummy node before head.

Move fast pointer n steps ahead.

Then move both fast and slow together
until fast reaches the last node.

slow will stop at the node before
the one to delete.

Delete:
slow.next = slow.next.next

Remember:
Dummy
↓

Fast moves n steps

↓

Move Together

↓

Delete

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        # Move fast pointer n steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers together until fast reaches the end
        # Make sure slow stops at the node before the one to delete
        while fast:
            fast = fast.next
            slow = slow.next

        # Delete the nth node from the end
        slow.next = slow.next.next

        return dummy.next
    
if __name__ == "__main__":
    # Example usage:
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    solution = Solution()
    new_head = solution.removeNthFromEnd(head, 2)  # Remove the 2nd node from the end

    # Print the updated linked list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")