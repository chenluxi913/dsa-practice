"""
LeetCode 173. Binary Search Tree Iterator

Topic:
- Binary Search Tree
- Stack
- Inorder Traversal
- Iterator

Pattern:
- Controlled Inorder Traversal

Idea:
The inorder traversal of a BST produces
values in ascending order:

Left → Root → Right

Instead of storing the entire traversal,
maintain a stack.

Initialization:
- Push the root and all of its left descendants.
- The top of the stack is always the next
  smallest node.

next():
1. Pop the top node.
2. Push the left path of its right subtree.
3. Return the current value.

hasNext():
Return whether the stack is not empty.

Remember:

Push Left Path

↓

Pop Smallest Node

↓

Push Right Subtree's Left Path

↓

Repeat

Time Complexity:
- next(): Amortized O(1)
- hasNext(): O(1)

Space Complexity: O(h)
where h is the height of the tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root):

        self.stack = []

        self.pushLeft(root)

    def hasNext(self):

        return len(self.stack) > 0

    def next(self):

        node = self.stack.pop()

        self.pushLeft(node.right)

        return node.val

    def pushLeft(self, node):

        while node:

            self.stack.append(node)

            node = node.left


if __name__ == "__main__":

    #          7
    #         / \
    #        3   15
    #           /  \
    #          9   20
    #
    # Inorder:
    # 3 → 7 → 9 → 15 → 20

    root = TreeNode(7)

    root.left = TreeNode(3)

    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    iterator = BSTIterator(root)

    print(iterator.next())      # 3
    print(iterator.next())      # 7
    print(iterator.hasNext())   # True
    print(iterator.next())      # 9
    print(iterator.hasNext())   # True
    print(iterator.next())      # 15
    print(iterator.hasNext())   # True
    print(iterator.next())      # 20
    print(iterator.hasNext())   # False