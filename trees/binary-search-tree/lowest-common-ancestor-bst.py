"""
LeetCode 235. Lowest Common Ancestor of a Binary Search Tree

Topic:
- Binary Search Tree
- DFS
- Recursion

Pattern:
- BST Value Comparison

Idea:
Use the BST property to locate the split point
between nodes p and q.

For the current node:

1. If both values are smaller than the current node,
   recursively search the left subtree.

2. If both values are greater than the current node,
   recursively search the right subtree.

3. Otherwise, the current node is the Lowest
   Common Ancestor.

The third case means:
- p and q are on different sides, or
- the current node is equal to p or q.

Remember:

Compare with Current Node

↓

Both Smaller
→ Go Left

↓

Both Greater
→ Go Right

↓

Otherwise
→ Current Node Is LCA

Time Complexity: O(h)
Space Complexity: O(h)
where h is the height of the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root, p, q):

        if not root:
            return None

        current = root.val

        if current > p.val and current > q.val:
            return self.lowestCommonAncestor(
                root.left,
                p,
                q
            )

        if current < p.val and current < q.val:
            return self.lowestCommonAncestor(
                root.right,
                p,
                q
            )

        return root


if __name__ == "__main__":

    #              6
    #            /   \
    #           2     8
    #          / \   / \
    #         0   4 7   9
    #            / \
    #           3   5
    #
    # LCA(2, 8) = 6
    # LCA(2, 4) = 2

    root = TreeNode(6)

    root.left = TreeNode(2)
    root.right = TreeNode(8)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    solution = Solution()

    p = root.left
    q = root.left.right

    lca = solution.lowestCommonAncestor(root, p, q)

    print(lca.val)   # 2