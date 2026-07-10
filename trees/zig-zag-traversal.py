"""
LeetCode 103. Binary Tree Zigzag Level Order Traversal

Topic:
- Binary Tree
- BFS
- Queue

Pattern:
- Level Order Traversal

Idea:
Use BFS to traverse the tree level by level.

For each level:

1. Create an array of the current level size.
2. If traversing from left to right,
   place values from left to right.
3. Otherwise,
   place values from right to left.
4. Add children into the queue.
5. Toggle the traversal direction.

Instead of reversing the list after traversal,
place each value into its correct position directly.

Remember:

BFS
↓

Process One Level

↓

Place Value at Correct Index

↓

Push Children

↓

Switch Direction

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

    def zigzagLevelOrder(self, root):

        if not root:
            return []

        result = []
        queue = deque([root])

        left_to_right = True

        while queue:

            size = len(queue)

            level = [0] * size

            for i in range(size):

                node = queue.popleft()

                index = i if left_to_right else size - 1 - i

                level[index] = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

            left_to_right = not left_to_right

        return result


if __name__ == "__main__":

    #        3
    #       / \
    #      9   20
    #         /  \
    #        15   7
    #
    # Output:
    # [[3], [20, 9], [15, 7]]

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()

    print(solution.zigzagLevelOrder(root))