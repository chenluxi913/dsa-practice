"""
LeetCode 160. Intersection of Two Linked Lists

Topic:
- Linked List
- Two Pointers

Pattern:
- Switch Heads

Idea:
Use two pointers.

Pointer A starts at headA.
Pointer B starts at headB.

When A reaches the end, move it to headB.
When B reaches the end, move it to headA.

This makes both pointers travel the same total distance.

If the lists intersect:
They will meet at the intersection node.

If they do not intersect:
They will both become None.

Remember:
A walks A + B
B walks B + A

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA  # Can be the intersection node or None
    
if __name__ == "__main__":
    # Example usage:
    # Creating two intersecting linked lists:
    # List A: 1 -> 2 -> 3
    # List B: 6 -> 3 (intersecting at node with value 3)
    
    intersecting_node = ListNode(3)
    
    headA = ListNode(1, ListNode(2, intersecting_node))
    headB = ListNode(6, intersecting_node)
    
    solution = Solution()
    intersection = solution.getIntersectionNode(headA, headB)
    
    if intersection:
        print(f"Intersection at node with value: {intersection.val}")
    else:
        print("No intersection.")