"""
LeetCode 1373. Maximum Sum BST in Binary Tree

Topic:
- Binary Tree
- Binary Search Tree
- DFS
- Postorder Traversal
- Tree DP

Pattern:
- Return Subtree Information

Idea:
Use postorder traversal because the current node
needs information from both the left and right subtrees.

For each subtree, return:

1. The minimum value in the subtree.
2. The maximum value in the subtree.
3. The sum of all values in the subtree.

The current subtree is a valid BST if:

left.max_node < node.val < right.min_node

If valid:
- Calculate the current subtree sum.
- Update the global maximum sum.
- Return the updated minimum, maximum, and sum.

If invalid:
- Return values that prevent its parent
  from treating this subtree as a valid BST.

Remember:

Postorder Traversal

↓

Get Left Information

↓

Get Right Information

↓

Check BST Condition

↓

Calculate Subtree Sum

↓

Update Maximum Sum

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
    # Helper class to store information about a subtree.
    class NodeValue:

        def __init__(self, min_node, max_node, subtree_sum):
            self.min_node = min_node
            self.max_node = max_node
            self.subtree_sum = subtree_sum

    def maxSumBST(self, root):

        self.max_sum = 0

        self.dfs(root)

        return self.max_sum

    def dfs(self, node):

        if not node:
            # Return values that will not affect the parent node's BST validation.
            # upper bound for min_node, lower bound for max_node, and 0 for subtree_sum.
            return self.NodeValue(
                float("inf"),
                float("-inf"),
                0
            )

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left.max_node < node.val < right.min_node:

            current_sum = (
                left.subtree_sum
                + right.subtree_sum
                + node.val
            )

            self.max_sum = max(
                self.max_sum,
                current_sum
            )

            return self.NodeValue(
                min(node.val, left.min_node),
                max(node.val, right.max_node),
                current_sum
            )
        # If the current subtree is not a valid BST, 
        # return values that will prevent its parent from treating it as a valid BST.
        return self.NodeValue(
            float("-inf"),
            float("inf"),
            0
        )


if __name__ == "__main__":

    #       4
    #      /
    #     3
    #    / \
    #   1   2
    #
    # The subtree rooted at 3 is not a BST.
    # Valid BST subtrees:
    # [1], [2]
    #
    # Maximum sum = 2

    root = TreeNode(4)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    solution = Solution()

    print(solution.maxSumBST(root))  # 2