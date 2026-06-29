"""
LeetCode 2095. Delete the Middle Node of a Linked List

Topic:
- Linked List
- Two Pointers

Pattern:
- Fast & Slow Pointer

Idea:
Use two pointers:

slow -> moves one step
fast -> starts two steps ahead and moves two steps

By starting fast two steps ahead,
slow stops at the node BEFORE the middle.

Delete:
slow.next = slow.next.next

Special Case:
If the list has only one node,
return None.

Remember:
Fast starts two steps ahead.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        #s tart fast two steps ahead to stop slow at the node before the middle
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        slow.next = slow.next.next

        return head
    
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    new_head = solution.deleteMiddle(head)

    # Print the modified linked list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")  # Output: 1 -> 2 -> 4 -> 5 -> None