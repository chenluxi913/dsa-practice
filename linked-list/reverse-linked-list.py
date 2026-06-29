"""
LeetCode 206. Reverse Linked List

Topic:
- Linked List

Pattern:
- Pointer Reversal

Idea:
Reverse one link at a time.

Use three pointers:

prev -> previous node
curr -> current node
next -> next node

At each step:
1. Save next node.
2. Reverse current pointer.
3. Move all pointers forward.

Remember:
Save → Reverse → Move

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # Save next node
            curr.next = prev       # Reverse current pointer
            prev = curr            # Move prev forward / save prev for next iteration
            curr = next_node       # Move curr forward / move to next node to work on

        return prev  # New head of the reversed list
    

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    reversed_head = solution.reverseList(head)

    # Print the reversed linked list
    current = reversed_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None