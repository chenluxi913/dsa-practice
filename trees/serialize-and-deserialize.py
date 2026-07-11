"""
LeetCode 297. Serialize and Deserialize Binary Tree

Topic:
- Binary Tree
- BFS
- Queue
- String Processing

Pattern:
- Level Order Serialization

Idea:
Use BFS (Level Order Traversal) to serialize
the binary tree.

For each node:
- Store its value.
- Store "#" if the node is None.

Including null nodes preserves the exact
tree structure.

For deserialization:

1. Read the root.
2. Use a queue to rebuild the tree level by level.
3. Read two values for each node:
   - left child
   - right child
4. Ignore "#" because it represents None.

Remember:

Serialize

BFS
↓

Store Node Values

↓

Store "#" for Null

Deserialize

Read Root

↓

Build Left Child

↓

Build Right Child

↓

Repeat

Time Complexity:
- Serialize: O(n)
- Deserialize: O(n)

Space Complexity: O(n)
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):

        if not root:
            return ""

        result = []

        queue = deque([root])

        while queue:

            node = queue.popleft()

            if not node:
                result.append("#")
                continue

            result.append(str(node.val))

            queue.append(node.left)
            queue.append(node.right)

        return ",".join(result)

    def deserialize(self, data):

        if not data:
            return None

        values = deque(data.split(","))

        root = TreeNode(int(values.popleft()))

        queue = deque([root])

        while queue:

            node = queue.popleft()

            left_value = values.popleft()

            if left_value != "#":
                node.left = TreeNode(int(left_value))
                queue.append(node.left)

            right_value = values.popleft()

            if right_value != "#":
                node.right = TreeNode(int(right_value))
                queue.append(node.right)

        return root


if __name__ == "__main__":

    #        1
    #       / \
    #      2   3
    #         / \
    #        4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()

    data = codec.serialize(root)

    print(data)
    # 1,2,3,#,#,4,5,#,#,#,#

    tree = codec.deserialize(data)

    print(tree.val)                 # 1
    print(tree.left.val)            # 2
    print(tree.right.val)           # 3
    print(tree.right.left.val)      # 4
    print(tree.right.right.val)     # 5