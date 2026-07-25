"""
LeetCode 127. Word Ladder

Topic:
- Graph
- BFS
- String
- Hash Set

Pattern:
- Shortest Path in an Unweighted Graph
- Level-Order BFS
- Word Transformation

Idea:
Treat every word as a graph node.

Two words are connected if they differ
by exactly one character.

Start BFS from beginWord.

For each word:

1. Change every character from 'a' to 'z'.
2. Generate all possible neighboring words.
3. If the new word exists in wordList,
   it is a valid transformation.
4. Add it to the queue.
5. Remove it from the set immediately
   to mark it as visited.

The queue stores:

(word, sequence_length)

Since every transformation costs exactly 1,
BFS guarantees that the first time we reach
endWord is the shortest transformation sequence.

Remember:

beginWord

↓

Change One Letter

↓

Check Dictionary

↓

Valid Neighbor

↓

Remove from Set (Visited)

↓

Push into Queue

↓

First Reach endWord = Shortest Sequence

Time Complexity: O(N * L * 26)

Space Complexity: O(N)

Where:
N = number of words
L = length of each word
"""

from collections import deque


class Solution:

    def ladderLength(
        self,
        beginWord,
        endWord,
        wordList
    ):

        # Hash set for O(1) lookup.
        words = set(wordList)

        # endWord must exist.
        if endWord not in words:
            return 0

        # Queue stores:
        # (current_word, sequence_length)
        queue = deque()

        queue.append((beginWord, 1))

        # Mark beginWord as visited
        # if it exists in wordList.
        words.discard(beginWord)

        while queue:

            word, steps = queue.popleft()

            # First arrival is the shortest path.
            if word == endWord:
                return steps

            # Try changing every character.
            for index in range(len(word)):

                original = word[index]

                for code in range(
                    ord("a"),
                    ord("z") + 1
                ):

                    character = chr(code)

                    # Skip the original character.
                    if character == original:
                        continue

                    next_word = (
                        word[:index]
                        + character
                        + word[index + 1:]
                    )

                    if next_word in words:

                        # Mark visited immediately.
                        words.remove(next_word)

                        queue.append(
                            (
                                next_word,
                                steps + 1
                            )
                        )

        return 0


if __name__ == "__main__":

    solution = Solution()

    print(
        solution.ladderLength(
            "hit",
            "cog",
            [
                "hot",
                "dot",
                "dog",
                "lot",
                "log",
                "cog"
            ]
        )
    )
    # Expected output: 5

    print(
        solution.ladderLength(
            "hit",
            "cog",
            [
                "hot",
                "dot",
                "dog",
                "lot",
                "log"
            ]
        )
    )
    # Expected output: 0