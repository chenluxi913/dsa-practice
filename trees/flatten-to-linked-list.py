"""
LeetCode 114. Flatten Binary Tree to Linked List

Topic:
- Binary Tree
- DFS
- Recursion

Pattern:
- Reverse Preorder Traversal

Idea:
The flattened tree should follow preorder:

Root → Left → Right

Instead of processing preorder directly,
traverse the tree in reverse preorder:

Right → Left → Root

Maintain a pointer 'prev' that always points
to the previously processed node.

For each node:
1. Flatten the right subtree.
2. Flatten the left subtree.
3. Connect the current node's right pointer
   to prev.
4. Set the left pointer to None.
5. Move prev to the current node.

Remember:

Traverse Right

↓

Traverse Left

↓

Connect Current to Previous

↓

Move Previous Pointer

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

    def __init__(self):
        self.prev = None

    def flatten(self, root):

        self.prev = None

        self.dfs(root)

    def dfs(self, node):

        if not node:
            return

        self.dfs(node.right)

        self.dfs(node.left)

        node.right = self.prev
        node.left = None

        self.prev = node


if __name__ == "__main__":

    # Original tree:
    #
    #          1
    #         / \
    #        2   5
    #       / \   \
    #      3   4   6
    #
    # Flattened:
    #
    # 1 → 2 → 3 → 4 → 5 → 6

    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(5)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.right = TreeNode(6)

    solution = Solution()

    solution.flatten(root)

    current = root

    while current:
        print(current.val, end=" ")
        current = current.right

    # Output:
    # 1 2 3 4 5 6