"""
LeetCode 802. Find Eventual Safe States

Topic:
- Graph
- Breadth-First Search
- Topological Sort
- Reverse Graph

Pattern:
- Kahn's Algorithm
- Reverse Topological Sort

Idea:
A terminal node has no outgoing edges.

A safe node is a node where every possible path
eventually reaches a terminal node (or another
safe node).

Instead of processing the original graph,
reverse every edge.

For an original edge:

u -> v

Create the reversed edge:

v -> u

Then perform Kahn's Algorithm on the reversed
graph.

In the reversed graph:

- The in-degree of a node equals the
  out-degree of the original graph.

First, add all nodes with an in-degree of zero
(original terminal nodes) to the queue.

Then repeatedly:

1. Remove a safe node from the queue.
2. Add it to the answer.
3. Visit all of its predecessors.
4. Decrease their in-degrees.
5. If a predecessor's in-degree becomes zero,
   it is also a safe node.

Finally, sort the answer before returning it.

Remember:

Reverse Every Edge

↓

Calculate In-Degrees

↓

Add Terminal Nodes

↓

Process with BFS

↓

Decrease In-Degrees

↓

New In-Degree Becomes Zero

↓

Node Is Safe

↓

Sort the Result

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""


from collections import deque


class Solution:

    # Function to return the topological
    # sorting of the reversed graph.
    def topoSort(
        self,
        V,
        adj
    ):

        # To store the in-degrees.
        inDegree = [0] * V

        # Calculate the in-degrees.
        for node in range(V):

            for neighbor in adj[node]:
                inDegree[neighbor] += 1

        # Queue to facilitate BFS.
        queue = deque()

        # Add all nodes with
        # zero in-degree.
        for node in range(V):

            if inDegree[node] == 0:
                queue.append(node)

        # To store the result.
        result = []

        while queue:

            node = queue.popleft()

            result.append(node)

            # Traverse all neighbors.
            for neighbor in adj[node]:

                inDegree[neighbor] -= 1

                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        return result

    def eventualSafeNodes(
        self,
        graph
    ):

        V = len(graph)

        # To store the reversed graph.
        reverseGraph = [
            []
            for _ in range(V)
        ]

        # Reverse every edge.
        for node in range(V):

            for neighbor in graph[node]:

                # node -> neighbor
                #
                # becomes
                #
                # neighbor -> node
                reverseGraph[neighbor].append(node)

        # Get the safe nodes.
        result = self.topoSort(
            V,
            reverseGraph
        )

        # Return the nodes in
        # ascending order.
        result.sort()

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