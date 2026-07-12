"""
LeetCode 450. Delete Node in a BST

Topic:
- Binary Search Tree
- Iteration
- Tree Deletion
- Pointer Rewiring

Pattern:
- Search Parent and Reconnect Subtrees

Idea:
Use the BST property to iteratively search
for the node that should be deleted.

Instead of changing the deleted node's value,
reconnect its left and right subtrees directly.

When deleting a node:

1. If it has no left child,
   return its right subtree.

2. If it has no right child,
   return its left subtree.

3. If it has two children:
   - Use the right subtree as the new subtree root.
   - Find the leftmost node in the right subtree.
   - Attach the original left subtree to that node.
   - Return the right subtree.

While searching:
- If key is smaller, move left.
- If key is greater, move right.
- When the target is found as a child,
  replace that child using the connector function.

Remember:

Search by BST Property

↓

Find Target Node

↓

No Left
→ Return Right

No Right
→ Return Left

Two Children
→ Find Leftmost in Right Subtree
→ Attach Original Left Subtree
→ Return Right Subtree

Time Complexity: O(h)
Space Complexity: O(1)
where h is the height of the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def connectSubtrees(self, node):

        if not node.left:
            return node.right

        if not node.right:
            return node.left

        left_subtree = node.left
        new_root = node.right

        leftmost = new_root

        while leftmost.left:
            leftmost = leftmost.left

        leftmost.left = left_subtree

        return new_root

    def deleteNode(self, root, key):

        if not root:
            return None

        if root.val == key:
            return self.connectSubtrees(root)

        current = root

        while current:

            if key < current.val:

                if current.left and current.left.val == key:
                    current.left = self.connectSubtrees(current.left)
                    break

                current = current.left

            else:

                if current.right and current.right.val == key:
                    current.right = self.connectSubtrees(current.right)
                    break

                current = current.right

        return root


if __name__ == "__main__":

    # Original BST:
    #
    #          5
    #         / \
    #        3   6
    #       / \   \
    #      2   4   7
    #
    # Delete 3:
    #
    #          5
    #         / \
    #        4   6
    #       /     \
    #      2       7

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    solution = Solution()
    root = solution.deleteNode(root, 3)

    print(root.left.val)       # 4
    print(root.left.left.val)  # 2