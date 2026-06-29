"""
LeetCode 148. Sort List

Topic:
- Linked List
- Divide and Conquer
- Merge Sort

Pattern:
- Find Middle
- Split List
- Merge Two Sorted Lists

Idea:
Use merge sort on linked list.

1. Find the middle of the list.
2. Split the list into two halves.
3. Recursively sort both halves.
4. Merge two sorted linked lists.

Remember:
Middle
↓
Split
↓
Sort
↓
Merge

Time Complexity: O(n log n)
Space Complexity: O(log n)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # Step 1: Find the middle of the linked list
        middle = self.findMiddle(head)

        # Step 2: Split the linked list into two halves
        right_half = middle.next
        middle.next = None  # Split the list into two halves
        left_half = head

        # Step 3: Recursively sort both halves
        left_sorted = self.sortList(left_half)
        right_sorted = self.sortList(right_half)

        # Step 4: Merge two sorted linked lists
        return self.mergeTwoLists(left_sorted, right_sorted)
    
    def findMiddle(self, head: ListNode) -> ListNode:
        slow = head
        # make sure fast starts at head.next to find the first middle node in case of even number of nodes
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

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

        # Attach remaining nodes if any
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return dummy.next
    
if __name__ == "__main__":
    # Create an unsorted linked list: 4 -> 2 -> 1 -> 3
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    solution = Solution()
    sorted_head = solution.sortList(head)

    # Print the sorted linked list
    curr = sorted_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")