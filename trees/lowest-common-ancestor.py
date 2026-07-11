"""
LeetCode 236. Lowest Common Ancestor of a Binary Tree

Topic:
- Binary Tree
- DFS
- Recursion

Pattern:
- Postorder Traversal
- Divide and Conquer

Idea:
Use DFS to search for nodes p and q.

For each node:

1. If the current node is None,
   return None.
2. If the current node is p or q,
   return the current node.
3. Search the left subtree.
4. Search the right subtree.
5. If both left and right return a node,
   the current node is the Lowest Common Ancestor.
6. Otherwise, return the non-None result.

Why?

- If p and q are found in different subtrees,
  the current node is their first common ancestor.
- If both nodes are in the same subtree,
  the subtree will return the answer directly.

Remember:

DFS
↓

Search Left

↓

Search Right

↓

Both Found
→ Current Node Is LCA

One Found
→ Return That Node

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

    def lowestCommonAncestor(self, root, p, q):

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right

        if not right:
            return left

        return root


if __name__ == "__main__":

    #              3
    #            /   \
    #           5     1
    #          / \   / \
    #         6   2 0   8
    #            / \
    #           7   4
    #
    # LCA(5, 1) = 3
    # LCA(5, 4) = 5

    root = TreeNode(3)

    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    solution = Solution()

    p = root.left
    q = root.right

    lca = solution.lowestCommonAncestor(root, p, q)

    print(lca.val)    # 3