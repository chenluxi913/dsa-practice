"""
LeetCode 701. Insert into a Binary Search Tree

Topic:
- Binary Search Tree
- Recursion
- Tree Insertion

Pattern:
- BST Search Path

Idea:
Use the BST property:

- If val is smaller than the current node,
  insert it into the left subtree.
- If val is greater than the current node,
  insert it into the right subtree.

Continue recursively until reaching None.

When the current node is None,
create and return a new TreeNode.

Remember:

Compare with Current Node

↓

Smaller
→ Go Left

Greater
→ Go Right

↓

Reach None

↓

Create New Node

↓

Return Current Root

Time Complexity: O(h)
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

    def insertIntoBST(self, root, val):

        return self.solve(root, val)

    def solve(self, node, val):

        if not node:
            return TreeNode(val)

        if val < node.val:
            node.left = self.solve(node.left, val)

        else:
            node.right = self.solve(node.right, val)

        return node


def printInOrder(root):

    if not root:
        return

    printInOrder(root.left)
    print(root.val, end=" ")
    printInOrder(root.right)


if __name__ == "__main__":

    # Original BST:
    #
    #        4
    #       / \
    #      2   7
    #     / \
    #    1   3
    #
    # Insert 5:
    #
    #        4
    #       / \
    #      2   7
    #     / \  /
    #    1  3 5

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    solution = Solution()
    root = solution.insertIntoBST(root, 5)

    printInOrder(root)
    # Output:
    # 1 2 3 4 5 7