"""
LeetCode 802. Find Eventual Safe States

Topic:
- Graph
- Depth-First Search
- Cycle Detection

Pattern:
- DFS
- Visited Array
- Path Visited Array

Idea:
A node is safe if every possible path starting
from it eventually reaches a terminal node.

During DFS, if we encounter a node that is
already in the current DFS path, a cycle is
found.

Nodes inside a cycle, or nodes that can reach
a cycle, are unsafe.

Use three arrays:

1. vis
   Whether the node has been visited.

2. pathVis
   Whether the node is currently in the DFS path.

3. check
   Whether the node is safe.

During DFS:

- Mark the current node as visited.
- Add it to the current DFS path.
- Assume it is unsafe.

Traverse every neighbor.

If a cycle is found,
return immediately.

If all neighbors are safe,
mark the current node as safe.

Finally, remove the node from the
current DFS path.

Remember:

DFS

↓

Mark Visited

↓

Add to Current Path

↓

Visit All Neighbors

↓

Cycle Found?

↓

Unsafe

↓

No Cycle Found

↓

Mark Safe

↓

Remove from Current Path

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""


from typing import List


class Solution:

    # Function to perform DFS traversal
    # while checking for safe nodes.
    def dfsCheck(
        self,
        node: int,
        adj: List[List[int]],
        vis: List[bool],
        pathVis: List[bool],
        check: List[bool]
    ) -> bool:

        # Mark the node as visited.
        vis[node] = True

        # Add the node to
        # the current DFS path.
        pathVis[node] = True

        # Assume the node
        # is not safe.
        check[node] = False

        # Traverse all neighbors.
        for neighbor in adj[node]:

            # Visit the neighbor
            # if it has not been visited.
            if not vis[neighbor]:

                if self.dfsCheck(
                    neighbor,
                    adj,
                    vis,
                    pathVis,
                    check
                ):
                    return True

            # A cycle is found.
            elif pathVis[neighbor]:
                return True

        # No cycle exists through
        # the current node.
        check[node] = True

        # Remove the node from
        # the current DFS path.
        pathVis[node] = False

        return False

    def eventualSafeNodes(
        self,
        graph: List[List[int]]
    ) -> List[int]:

        V = len(graph)

        # Visited array.
        vis = [False] * V

        # Current DFS path.
        pathVis = [False] * V

        # Whether the node is safe.
        check = [False] * V

        # Start DFS from every node.
        for node in range(V):

            if not vis[node]:

                self.dfsCheck(
                    node,
                    graph,
                    vis,
                    pathVis,
                    check
                )

        # Store all safe nodes.
        result = []

        for node in range(V):

            if check[node]:
                result.append(node)

        return result


if __name__ == "__main__":

    solution = Solution()

    graph = [
        [1, 2],
        [2, 3],
        [5],
        [0],
        [5],
        [],
        []
    ]

    print(
        solution.eventualSafeNodes(
            graph
        )
    )

    # Output:
    # [2, 4, 5, 6]