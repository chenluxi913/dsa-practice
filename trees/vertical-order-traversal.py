"""
LeetCode 987. Vertical Order Traversal of a Binary Tree

Topic:
- Binary Tree
- BFS
- Queue
- Hash Map
- Sorting

Pattern:
- Coordinate Traversal

Idea:
Assign coordinates to every node.

The root starts at:
(column, row) = (0, 0)

For each node:
- Left child:  (column - 1, row + 1)
- Right child: (column + 1, row + 1)

Use a nested hash map:

nodes_map[column][row] = list of node values

After BFS:
1. Sort columns from left to right.
2. Sort rows from top to bottom.
3. Sort node values when multiple nodes
   share the same row and column.
4. Add the values to the result.

Remember:

BFS with Coordinates
↓

Store by Column and Row

↓

Sort Columns

↓

Sort Rows

↓

Sort Same-Position Values

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def verticalTraversal(self, root):

        if not root:
            return []

        nodes_map = defaultdict(lambda: defaultdict(list))

        queue = deque([(root, 0, 0)])

        while queue:

            node, column, row = queue.popleft()

            nodes_map[column][row].append(node.val)

            if node.left:
                queue.append(
                    (node.left, column - 1, row + 1)
                )

            if node.right:
                queue.append(
                    (node.right, column + 1, row + 1)
                )

        result = []

        for column in sorted(nodes_map):

            current_column = []

            for row in sorted(nodes_map[column]):

                values = sorted(nodes_map[column][row])

                current_column.extend(values)

            result.append(current_column)

        return result


if __name__ == "__main__":

    #          3
    #         / \
    #        9   20
    #           /  \
    #          15   7
    #
    # Output:
    # [[9], [3, 15], [20], [7]]

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()

    print(solution.verticalTraversal(root))