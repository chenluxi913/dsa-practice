"""
LeetCode 142. Linked List Cycle II

Topic:
- Linked List
- Two Pointers

Pattern:
- Fast & Slow Pointer
- Floyd's Cycle Detection

Idea:
Step 1:
Use fast and slow pointers.

If they never meet,
there is no cycle.

Step 2:
After they meet,
move one pointer back to head.

Move both pointers one step at a time.

The node where they meet again
is the start of the cycle.

Remember:
Meet Once
↓

One Back to Head
↓

Move Together
↓

Meet Again = Cycle Start

Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        # Step 1: Detect if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Cycle detected, move one pointer to head
                slow = head

                # Step 2: Find the start of the cycle
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow  # Start of the cycle

        return None  # No cycle detected
    
if __name__ == "__main__":
    # Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle)
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = head.next.next  # Create a cycle

    solution = Solution()
    cycle_start_node = solution.detectCycle(head)

    if cycle_start_node:
        print(cycle_start_node.val)  # Output: 3
    else:
        print("No cycle detected")