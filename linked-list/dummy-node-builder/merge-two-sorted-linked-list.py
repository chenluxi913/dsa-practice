"""
LeetCode 21. Merge Two Sorted Lists

Topic:
- Linked List

Pattern:
- Dummy Node Builder

Idea:
Traverse both sorted lists.

Always choose the smaller node
and attach it to the merged list.

When one list ends,
attach the remaining nodes.

Remember:
Compare
↓

Connect

↓

Move

↓

Attach Remaining

Reusable Template:

dummy = ListNode()
curr = dummy

while ...:

    curr.next = node
    curr = curr.next

return dummy.next

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        # Attach the remaining nodes
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return dummy.next
    
if __name__ == "__main__":
    # Create two sorted linked lists: 1 -> 2 -> 4 and 1 -> 3 -> 4
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    solution = Solution()
    merged_head = solution.mergeTwoLists(l1, l2)

    # Print the merged linked list
    curr = merged_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")