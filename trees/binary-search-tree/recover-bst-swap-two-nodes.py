"""
LeetCode 99. Recover Binary Search Tree

Topic:
- Binary Search Tree
- DFS
- Recursion
- Inorder Traversal

Pattern:
- Detect Inorder Inversions

Idea:
The inorder traversal of a valid BST should be
strictly increasing:

Left → Root → Right

If two node values are swapped, the inorder
sequence will contain one or two inversions.

Maintain four pointers:

- previous: previously visited node
- first: first incorrect node
- first_next: node after the first inversion
- last: second incorrect node if another
  inversion appears

When an inversion is found:

previous.val > current.val

For the first inversion:
- first = previous
- first_next = current

For the second inversion:
- last = current

Finally:

- If two inversions exist, swap first and last.
- If only one inversion exists, swap first
  and first_next.

Remember:

Inorder Traversal

↓

Compare Previous and Current

↓

First Inversion
→ Save Previous and Current

↓

Second Inversion
→ Save Current

↓

Swap Incorrect Values

Time Complexity: O(n)
Space Complexity: O(h)
where h is the height of the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):

        self.first = None
        self.first_next = None
        self.last = None
        self.previous = None

    def recoverTree(self, root) -> None:

        self.first = None
        self.first_next = None
        self.last = None
        self.previous = TreeNode(float("-inf"))

        self.inorder(root)

        if self.last:
            self.first.val, self.last.val = (
                self.last.val,
                self.first.val
            )
        else:
            self.first.val, self.first_next.val = (
                self.first_next.val,
                self.first.val
            )

    def inorder(self, node):

        if not node:
            return

        self.inorder(node.left)

        if self.previous.val > node.val:

            if not self.first:
                self.first = self.previous
                self.first_next = node

            else:
                self.last = node

        self.previous = node

        self.inorder(node.right)


if __name__ == "__main__":

    # Incorrect BST:
    #
    #        3
    #       / \
    #      1   4
    #         /
    #        2
    #
    # Inorder:
    # 1, 3, 2, 4
    #
    # One inversion:
    # 3 > 2
    #
    # Swap 3 and 2.

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)

    solution = Solution()
    solution.recoverTree(root)

    print(root.val)              # 2
    print(root.left.val)         # 1
    print(root.right.val)        # 4
    print(root.right.left.val)   # 3