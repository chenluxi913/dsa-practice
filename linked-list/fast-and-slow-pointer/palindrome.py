"""
LeetCode 234. Palindrome Linked List

Topic:
- Linked List
- Two Pointers

Pattern:
- Fast & Slow Pointer
- Reverse Linked List

Idea:
1. Find the middle of the linked list.
2. Reverse the second half.
3. Compare the first half and reversed second half.

Remember:
Middle
↓
Reverse
↓
Compare

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle of the linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 3: Compare the first half and reversed second half
        left, right = head, prev
        while right:  # Only need to compare until the end of the reversed half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
    

if __name__ == "__main__":
    # Example usage:
    # Create a palindrome linked list: 1 -> 2 -> 2 -> 1
    node4 = ListNode(1)
    node3 = ListNode(2, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    solution = Solution()
    print(solution.isPalindrome(head))  # Output: True

    # Create a non-palindrome linked list: 1 -> 2
    nodeB = ListNode(2)
    headB = ListNode(1, nodeB)

    print(solution.isPalindrome(headB))  # Output: False