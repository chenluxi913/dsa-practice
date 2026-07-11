"""
LeetCode 199. Binary Tree Right Side View

Topic:
- Binary Tree
- DFS
- Recursion

Pattern:
- Preorder Traversal

Idea:
Traverse the tree using DFS.

For the right side view:
- Visit the right child before the left child.
- The first node visited at each level
  is the rightmost node.

If the current level has not been visited,
add the node value to the result.

Remember:

DFS
↓

Visit Right Child First

↓

First Node at Each Level

↓

Add to Result

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

    def rightSideView(self, root):

        result = []

        def dfs(node, level):

            if not node:
                return

            if len(result) == level:
                result.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)

        return result


if __name__ == "__main__":

    #        1
    #       / \
    #      2   3
    #       \   \
    #        5   4
    #
    # Right Side View:
    # [1, 3, 4]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    solution = Solution()

    print(solution.rightSideView(root))