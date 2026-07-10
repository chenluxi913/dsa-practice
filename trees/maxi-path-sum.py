"""
LeetCode 124. Binary Tree Maximum Path Sum

Topic:
- Binary Tree
- DFS
- Recursion

Pattern:
- Tree DP
- Maximum Path Sum

Idea:
Use DFS to calculate the maximum path gain
that each node can contribute to its parent.

For every node:

1. Compute the maximum gain from the left subtree.
2. Compute the maximum gain from the right subtree.
3. Ignore negative gains since they reduce the path sum.
4. The maximum path passing through the current node is:
   node.val + left_gain + right_gain.
5. Update the global maximum path sum.
6. Return the maximum gain that can be extended
   to the parent:
   node.val + max(left_gain, right_gain).

Why only return one side?

A path cannot split when extending upward.
The parent can only continue through either
the left branch or the right branch.

Remember:

DFS
↓

Get Left Gain & Right Gain

↓

Ignore Negative Gains

↓

Update Global Maximum
(left + node + right)

↓

Return One-Side Gain
(node + max(left, right))

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

    def maxPathSum(self, root: TreeNode) -> int:

        self.max_sum = float("-inf")

        def dfs(node):

            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            current_path = node.val + left_gain + right_gain

            self.max_sum = max(self.max_sum, current_path)

            return node.val + max(left_gain, right_gain)

        dfs(root)

        return self.max_sum

if __name__ == "__main__":
    # Example usage:
    # Construct the binary tree:
    #       -10
    #       /  \
    #      9   20
    #          / \
    #         15  7
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    result = solution.maxPathSum(root)
    print(result)  # Output: 42