"""
LeetCode 141. Linked List Cycle

Topic:
- Linked List
- Two Pointers

Pattern:
- Fast & Slow Pointer
- Floyd's Cycle Detection

Idea:
Use two pointers:

slow -> moves one step
fast -> moves two steps

If there is a cycle:
fast will eventually meet slow.

If there is no cycle:
fast will reach None.

Remember:
Meet -> Cycle
None -> No Cycle

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle detected
    
if __name__ == "__main__":
    # Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = head.next.next  # Create a cycle

    solution = Solution()
    has_cycle = solution.hasCycle(head)
    print(has_cycle)  # Output: True