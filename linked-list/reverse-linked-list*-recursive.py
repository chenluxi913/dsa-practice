"""
LeetCode 206. Reverse Linked List (Recursive)

Topic:
- Linked List
- Recursion

Pattern:
- Recursive Pointer Reversal

Idea:
Reverse the rest of the list first.

During recursion:
head -> next

After recursion:
next -> head

Finally:
Break the original link to avoid a cycle.

Remember:
Reverse Rest
↓

Point Back
↓

Break Link

Time Complexity: O(n)
Space Complexity: O(n)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)
        
        # Reverse the current node's pointer
        head.next.next = head
        head.next = None  # Break the original link to avoid a cycle
        
        return new_head
    
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