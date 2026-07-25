"""
LeetCode 785. Is Graph Bipartite?

Topic:
- Graph
- BFS
- Graph Coloring

Pattern:
- Bipartite Graph
- Two-Coloring
- Connected Components

Idea:
A graph is bipartite if every edge connects
two nodes with different colors.

Use three states:

-1 = Uncolored
 0 = Color A
 1 = Color B

For every uncolored node:

1. Assign the first color.
2. Start BFS.
3. Color every neighbor with the opposite color.
4. If two adjacent nodes have the same color,
   the graph is not bipartite.

The graph may contain multiple connected
components, so start BFS from every
uncolored node.

Remember:

Find Uncolored Node

↓

Assign First Color

↓

BFS

↓

Neighbor Gets Opposite Color

↓

Conflict?

↓

Yes → Not Bipartite

No → Continue

Time Complexity: O(V + E)

Space Complexity: O(V)
"""

from collections import deque


class Solution:

    def bfs(self, start, graph, color):

        queue = deque()

        queue.append(start)

        # Assign the first color.
        color[start] = 0

        while queue:

            node = queue.popleft()

            for neighbor in graph[node]:

                # Neighbor has not been colored.
                if color[neighbor] == -1:

                    color[neighbor] = 1 - color[node]

                    queue.append(neighbor)

                # Adjacent nodes have the same color.
                elif color[neighbor] == color[node]:

                    return False

        return True

    def isBipartite(self, graph):

        nodes = len(graph)

        # -1 means uncolored.
        color = [-1] * nodes

        # The graph may be disconnected.
        for node in range(nodes):

            if color[node] == -1:

                if not self.bfs(
                    node,
                    graph,
                    color
                ):
                    return False

        return True


if __name__ == "__main__":

    solution = Solution()

    graph1 = [
        [1, 2, 3],
        [0, 2],
        [0, 1, 3],
        [0, 2]
    ]

    print(solution.isBipartite(graph1))
    # Expected output: False

    graph2 = [
        [1, 3],
        [0, 2],
        [1, 3],
        [0, 2]
    ]

    print(solution.isBipartite(graph2))
    # Expected output: True