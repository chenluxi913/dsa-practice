"""
LeetCode 2. Add Two Numbers

Topic:
- Linked List
- Math

Pattern:
- Dummy Node
- Carry

Idea:
Traverse both linked lists together.

At each step:
1. Read current values.
2. Add them with carry.
3. Create a new node.
4. Move pointers forward.

Continue while:
- l1 exists
- l2 exists
- carry exists

Remember:
Read
↓

Add + Carry
↓

Create Node
↓

Move

Reusable Template:

dummy = ListNode()
curr = dummy

while ...:

    curr.next = ListNode(value)

    curr = curr.next

return dummy.next

Time Complexity: O(max(m, n))
Space Complexity: O(max(m, n))
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            
            # create a new node with the digit value (total % 10)
            curr.next = ListNode(total % 10)

            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
    
if __name__ == "__main__":
    # Create two linked lists: 2 -> 4 -> 3 and 5 -> 6 -> 4
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # Print the result linked list
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")  # End of the linked list