"""
LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal

Topic:
- Binary Tree
- Recursion
- Hash Map
- Divide and Conquer

Pattern:
- Build Tree from Traversal Ranges

Idea:
Preorder traversal follows:

Root → Left → Right

Therefore, preorder[preStart] is the root
of the current subtree.

Inorder traversal follows:

Left → Root → Right

Find the root position in inorder.
Then calculate how many nodes belong
to the left subtree.

Use that left subtree size to divide
both preorder and inorder ranges.

Remember:

Take Root from Preorder
↓

Find Root in Inorder
↓

Calculate Left Subtree Size
↓

Build Left Subtree
↓

Build Right Subtree

Time Complexity: O(n)
Space Complexity: O(n)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder, inorder):

        inorder_map = {
            value: index
            for index, value in enumerate(inorder)
        }

        def build(pre_start, pre_end, in_start, in_end):

            if pre_start > pre_end or in_start > in_end:
                return None

            root_value = preorder[pre_start]
            root = TreeNode(root_value)

            inorder_root = inorder_map[root_value]

            left_size = inorder_root - in_start

            root.left = build(
                pre_start + 1,
                pre_start + left_size,
                in_start,
                inorder_root - 1
            )

            root.right = build(
                pre_start + left_size + 1,
                pre_end,
                inorder_root + 1,
                in_end
            )

            return root

        return build(
            0,
            len(preorder) - 1,
            0,
            len(inorder) - 1
        )


if __name__ == "__main__":

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    solution = Solution()
    root = solution.buildTree(preorder, inorder)

    #        3
    #       / \
    #      9   20
    #         /  \
    #        15   7

    print(root.val)               # 3
    print(root.left.val)          # 9
    print(root.right.val)         # 20
    print(root.right.left.val)    # 15
    print(root.right.right.val)   # 7