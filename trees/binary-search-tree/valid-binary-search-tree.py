"""
LeetCode 98. Validate Binary Search Tree

Topic:
- Binary Search Tree
- DFS
- Recursion

Pattern:
- Valid Range Check

Idea:
A valid BST requires every node to satisfy:

lower < node.val < upper

Start with the range:

(-∞, +∞)

For each node:

1. Check whether the current node value
   lies within the valid range.
2. Recursively validate the left subtree:
   - Update the upper bound to node.val.
3. Recursively validate the right subtree:
   - Update the lower bound to node.val.
4. Both subtrees must be valid.

Why?

A node must satisfy the constraints from
all of its ancestors, not just its parent.

Remember:

Check Current Range

↓

Go Left
(lower, node.val)

↓

Go Right
(node.val, upper)

↓

Both Subtrees Must Be Valid

Time Complexity: O(n)
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

    def isValidBST(self, root):

        return self.validate(
            root,
            float("-inf"),
            float("inf")
        )

    def validate(self, node, lower, upper):

        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        left_valid = self.validate(
            node.left,
            lower,
            node.val
        )

        right_valid = self.validate(
            node.right,
            node.val,
            upper
        )

        return left_valid and right_valid


if __name__ == "__main__":

    # Valid BST:
    #
    #       2
    #      / \
    #     1   3

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    solution = Solution()

    print(solution.isValidBST(root))   # True