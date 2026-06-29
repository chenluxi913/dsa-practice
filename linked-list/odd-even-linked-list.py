"""
LeetCode 328. Odd Even Linked List

Topic:
- Linked List

Pattern:
- Split and Reconnect

Idea:
Split the linked list into:

odd-indexed nodes
even-indexed nodes

Reconnect odd nodes together
and even nodes together.

Finally, connect the odd list
to the beginning of the even list.

Remember:
Odd jumps over even

↓

Even jumps over odd

↓

Connect odd tail to even head

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
    
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    solution = Solution()
    new_head = solution.oddEvenList(head)

    # Print the modified linked list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")