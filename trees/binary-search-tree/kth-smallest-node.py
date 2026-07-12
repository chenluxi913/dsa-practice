"""
LeetCode 230. Kth Smallest Element in a BST

Topic:
- Binary Search Tree
- DFS
- Recursion
- Inorder Traversal

Pattern:
- Inorder Traversal of BST

Idea:
The inorder traversal of a BST visits nodes
in ascending order:

Left → Root → Right

Maintain a counter k.

For each visited node:
1. Traverse the left subtree.
2. Decrease k.
3. If k becomes 0, the current node is
   the kth smallest node.
4. Traverse the right subtree.

Stop recursion once the answer is found.

Remember:

Traverse Left

↓

Visit Current Node

↓

Decrease K

↓

K == 0
→ Save Answer

↓

Traverse Right

Time Complexity: O(h + k)
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

    def kthSmallest(self, root, k):

        self.k = k
        self.result = None

        self.inorder(root)

        return self.result

    def inorder(self, node):

        if not node or self.result is not None:
            return

        self.inorder(node.left)

        if self.result is not None:
            return

        self.k -= 1

        if self.k == 0:
            self.result = node.val
            return

        self.inorder(node.right)


if __name__ == "__main__":

    #        5
    #       / \
    #      3   6
    #     / \
    #    2   4
    #   /
    #  1
    #
    # Inorder:
    # 1, 2, 3, 4, 5, 6
    #
    # k = 3
    # Answer = 3

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    solution = Solution()

    print(solution.kthSmallest(root, 3))  # 3