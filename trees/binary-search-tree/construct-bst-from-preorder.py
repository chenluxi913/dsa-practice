"""
LeetCode 1008. Construct Binary Search Tree from Preorder Traversal

Topic:
- Binary Search Tree
- DFS
- Recursion

Pattern:
- Build BST with Upper Bound

Idea:
Preorder traversal follows:

Root → Left → Right

Use a class variable 'self.index' to track
the next preorder value.

Each recursive call has an upper bound.

For the current value:

1. If all values are used, return None.
2. If the current value exceeds the upper bound,
   it does not belong to this subtree.
3. Create the current node.
4. Build the left subtree using the current
   node value as the new upper bound.
5. Build the right subtree using the parent's
   upper bound.

Remember:

Read Current Value

↓

Check Upper Bound

↓

Create Root

↓

Build Left
(bound = root.val)

↓

Build Right
(bound unchanged)

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

    def bstFromPreorder(self, preorder):

        self.index = 0

        return self.build(
            preorder,
            float("inf")
        )

    def build(self, preorder, upper_bound):

        if (
            self.index == len(preorder)
            or preorder[self.index] > upper_bound
        ):
            return None

        root = TreeNode(preorder[self.index])

        self.index += 1

        root.left = self.build(
            preorder,
            root.val
        )

        root.right = self.build(
            preorder,
            upper_bound
        )

        return root


if __name__ == "__main__":

    preorder = [8, 5, 1, 7, 10, 12]

    solution = Solution()

    root = solution.bstFromPreorder(preorder)

    #         8
    #       /   \
    #      5     10
    #     / \      \
    #    1   7      12

    print(root.val)               # 8
    print(root.left.val)          # 5
    print(root.right.val)         # 10
    print(root.left.left.val)     # 1
    print(root.left.right.val)    # 7
    print(root.right.right.val)   # 12