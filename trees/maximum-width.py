"""
LeetCode 662. Maximum Width of Binary Tree

Topic:
- Binary Tree
- BFS
- Queue
- Complete Binary Tree Indexing

Pattern:
- Level Order Traversal

Idea:
Use BFS to traverse the tree level by level.

Assign each node an index as if the tree were
a complete binary tree.

For a node with index i:
- Left child index:  2 * i + 1
- Right child index: 2 * i + 2

For each level:
1. Record the first node's index.
2. Normalize all indices by subtracting
   the first index of the current level.
3. Record the first and last normalized indices.
4. Calculate the width:

   last_index - first_index + 1

Normalizing indices prevents them from becoming
too large in a deep binary tree.

Remember:

BFS Level by Level
↓

Assign Complete Tree Indices
↓

Normalize Current Level
↓

Get First and Last Index
↓

Update Maximum Width

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def widthOfBinaryTree(self, root):

        if not root:
            return 0

        max_width = 0

        queue = deque([(root, 0)])

        while queue:

            size = len(queue)

            first_index = queue[0][1]

            first = 0
            last = 0

            for i in range(size):

                node, index = queue.popleft()

                current_index = index - first_index

                if i == 0:
                    first = current_index

                if i == size - 1:
                    last = current_index

                if node.left:
                    queue.append(
                        (node.left, 2 * current_index + 1)
                    )

                if node.right:
                    queue.append(
                        (node.right, 2 * current_index + 2)
                    )

            current_width = last - first + 1

            max_width = max(max_width, current_width)

        return max_width


if __name__ == "__main__":

    #          1
    #        /   \
    #       3     2
    #      / \     \
    #     5   3     9
    #
    # Last level:
    # 5, 3, null, 9
    #
    # Maximum width = 4

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)

    solution = Solution()

    print(solution.widthOfBinaryTree(root))  # 4