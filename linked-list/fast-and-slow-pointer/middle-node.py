"""
LeetCode 876. Middle of the Linked List

Topic:
- Linked List
- Two Pointers

Pattern:
- Fast & Slow Pointer

Idea:
Use two pointers:

slow -> moves one step
fast -> moves two steps

When fast reaches the end,
slow will be at the middle.

Remember:
Slow +1
Fast +2

If there are two middle nodes,
slow automatically points to the second one.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
if __name__ == "__main__":      
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    middle_node = solution.middleNode(head)
    print(middle_node.val)  # Output: 3