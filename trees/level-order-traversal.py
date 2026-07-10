"""
LeetCode 102. Binary Tree Level Order Traversal

Topic:
- Binary Tree
- BFS
- Queue

Pattern:
- Level Order Traversal

Idea:
Use BFS to traverse the binary tree level by level.

For each level:

1. Record the number of nodes in the queue.
2. Process exactly that many nodes.
3. Store their values in the current level list.
4. Push their children into the queue.
5. Add the current level to the answer.

Remember:

Queue
↓

Process Current Level

↓

Collect Node Values

↓

Push Children

↓

Add Level to Answer

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

    def levelOrder(self, root):

        if not root:
            return []

        result = []

        queue = deque([root])

        while queue:

            size = len(queue)
            level = []

            for _ in range(size):

                node = queue.popleft()

                # Collect the value of the current node
                level.append(node.val)

                # Push children into the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result


if __name__ == "__main__":

    #        3
    #       / \
    #      9   20
    #         /  \
    #        15   7
    #
    # Output:
    # [[3], [9, 20], [15, 7]]

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print(solution.levelOrder(root))