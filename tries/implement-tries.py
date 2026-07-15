"""
LeetCode 208. Implement Trie (Prefix Tree)

Topic:
- Trie
- Prefix Tree
- String

Pattern:
- Character-by-Character Traversal

Idea:
A Trie stores one character per node.

Each node contains:

1. An array of 26 child pointers.
2. A boolean indicating whether
   the current node is the end
   of a word.

insert(word):
- Traverse each character.
- Create a child node if needed.
- Move to the child.
- Mark the last node as the end.

search(word):
- Traverse each character.
- If a character is missing,
  return False.
- Return whether the last node
  is the end of a word.

startsWith(prefix):
- Traverse each character.
- If all characters exist,
  return True.

Remember:

Insert

Root

↓

Character

↓

Create Child If Needed

↓

Move Down

↓

Mark End

Search

Root

↓

Character

↓

Missing?
→ False

↓

End of Word?
→ True / False

Prefix Search

Root

↓

Character

↓

Missing?
→ False

↓

Reach End of Prefix
→ True

Time Complexity:
- insert: O(n)
- search: O(n)
- startsWith: O(n)

Space Complexity:
O(total characters inserted)
"""


class TrieNode:

    def __init__(self):

        self.children = [None] * 26
        self.is_end = False

    def contains(self, ch):

        index = ord(ch) - ord("a")

        return self.children[index] is not None

    def put(self, ch, node):

        index = ord(ch) - ord("a")

        self.children[index] = node

    def get(self, ch):

        index = ord(ch) - ord("a")

        return self.children[index]

    def setEnd(self):

        self.is_end = True


class Trie:

    def __init__(self):

        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for ch in word:

            if not node.contains(ch):
                node.put(ch, TrieNode())

            node = node.get(ch)

        node.setEnd()

    def search(self, word):

        node = self.root

        for ch in word:

            if not node.contains(ch):
                return False

            node = node.get(ch)

        return node.is_end

    def startsWith(self, prefix):

        node = self.root

        for ch in prefix:

            if not node.contains(ch):
                return False

            node = node.get(ch)

        return True


if __name__ == "__main__":

    trie = Trie()

    trie.insert("apple")

    print(trie.search("apple"))      # True
    print(trie.search("app"))        # False
    print(trie.startsWith("app"))    # True

    trie.insert("app")

    print(trie.search("app"))        # True