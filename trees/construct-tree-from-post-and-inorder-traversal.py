"""
LeetCode 106. Construct Binary Tree from Inorder and Postorder Traversal

Topic:
- Binary Tree
- Recursion
- Hash Map
- Divide and Conquer

Pattern:
- Build Tree from Traversal Ranges

Idea:
Postorder traversal follows:

Left → Right → Root

Therefore, postorder[postEnd] is the root
of the current subtree.

Inorder traversal follows:

Left → Root → Right

Find the root position in inorder.
Then calculate the number of nodes
in the left subtree.

Use the left subtree size to divide
both inorder and postorder ranges.

Remember:

Take Root from Postorder End

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

    def buildTree(self, inorder, postorder):

        inorder_map = {
            value: index
            for index, value in enumerate(inorder)
        }

        def build(in_start, in_end, post_start, post_end):

            if in_start > in_end or post_start > post_end:
                return None
            # Take the root value from the end of the postorder range
            # different from preorder where we take the root from the start of the range
            root_value = postorder[post_end]
            root = TreeNode(root_value)

            inorder_root = inorder_map[root_value]

            left_size = inorder_root - in_start

            root.left = build(
                in_start,
                inorder_root - 1,
                post_start,
                post_start + left_size - 1
            )

            root.right = build(
                inorder_root + 1,
                in_end,
                post_start + left_size,
                post_end - 1
            )

            return root

        return build(
            0,
            len(inorder) - 1,
            0,
            len(postorder) - 1
        )


if __name__ == "__main__":

    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    solution = Solution()
    root = solution.buildTree(inorder, postorder)

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