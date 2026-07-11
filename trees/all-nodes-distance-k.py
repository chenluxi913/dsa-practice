"""
LeetCode 863. All Nodes Distance K in Binary Tree

Topic:
- Binary Tree
- BFS
- Queue
- Hash Map
- Graph Traversal

Pattern:
- Parent Map
- BFS from Target

Idea:
A binary tree only stores links from parent to child.

However, to find all nodes at distance k from
the target, we may need to move upward to a parent.

Therefore:

1. Use BFS to build a parent map.
2. Start another BFS from the target node.
3. From each node, explore:
   - left child
   - right child
   - parent
4. Use a visited set to avoid revisiting nodes.
5. When the current distance reaches k,
   all nodes remaining in the queue are the answer.

Remember:

Build Parent Map
↓

Start BFS from Target
↓

Move Left, Right, Parent
↓

Avoid Visited Nodes
↓

Collect Queue at Distance K

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

    def distanceK(self, root, target, k):

        parent_map = {}

        queue = deque([root])

        while queue:

            node = queue.popleft()

            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)

            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

        queue = deque([target])
        visited = {target}

        current_distance = 0

        while queue:

            if current_distance == k:
                return [node.val for node in queue]

            size = len(queue)

            for _ in range(size):

                node = queue.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)

                parent = parent_map.get(node)

                if parent and parent not in visited:
                    visited.add(parent)
                    queue.append(parent)

            current_distance += 1

        return []


if __name__ == "__main__":

    #              3
    #            /   \
    #           5     1
    #          / \   / \
    #         6   2 0   8
    #            / \
    #           7   4
    #
    # Target = 5
    # k = 2
    #
    # Output:
    # [7, 4, 1]

    root = TreeNode(3)

    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    target = root.left

    solution = Solution()

    print(solution.distanceK(root, target, 2))