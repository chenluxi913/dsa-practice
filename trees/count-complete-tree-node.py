"""
LeetCode 222. Count Complete Tree Nodes

Topic:
- Binary Tree
- Recursion
- Complete Binary Tree
- Bit Manipulation

Pattern:
- Compare Left Height and Right Height

Idea:
For each subtree:

1. Find the height by following only left children.
2. Find the height by following only right children.
3. If the two heights are equal,
   the subtree is a perfect binary tree.
4. A perfect binary tree with height h has:

   2^h - 1 nodes

5. Otherwise, recursively count the left
   and right subtrees.

Why?

In a complete binary tree, if the leftmost height
equals the rightmost height, every level is full.

Remember:

Find Left Height
↓

Find Right Height
↓

Heights Equal
→ Perfect Tree
→ Return 2^h - 1

Heights Different
→ Count Left and Right Recursively

Time Complexity: O(log² n)
Space Complexity: O(log n)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes(self, root):

        if not root:
            return 0

        left_height = self.findLeftHeight(root)
        right_height = self.findRightHeight(root)

        if left_height == right_height:
            return (1 << left_height) - 1

        return (
            1
            + self.countNodes(root.left)
            + self.countNodes(root.right)
        )

    def findLeftHeight(self, node):

        height = 0

        while node:
            height += 1
            node = node.left

        return height

    def findRightHeight(self, node):

        height = 0

        while node:
            height += 1
            node = node.right

        return height


if __name__ == "__main__":

    #          1
    #        /   \
    #       2     3
    #      / \   /
    #     4   5 6
    #
    # Output: 6

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    solution = Solution()

    print(solution.countNodes(root))  # 6