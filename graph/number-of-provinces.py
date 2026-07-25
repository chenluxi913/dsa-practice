"""
LeetCode 547. Number of Provinces

Topic:
- Graph
- BFS
- Adjacency Matrix
- Adjacency List

Pattern:
- Convert Matrix to List
- Count Connected Components

Idea:
The input is an adjacency matrix.

First convert it into an adjacency list.

Then traverse every city:

1. If a city is unvisited,
   it starts a new province.

2. Run BFS from that city.

3. Mark all directly or indirectly
   connected cities as visited.

Each BFS traversal discovers one province.

Remember:

Matrix

↓

Adjacency List

↓

Find Unvisited Node

↓

New Province

↓

BFS All Connected Nodes

Time Complexity: O(V^2)
Space Complexity: O(V + E)
"""


from collections import deque


class Solution:

    def findCircleNum(self, isConnected):

        vertices = len(isConnected)

        graph = self.buildGraph(isConnected)

        visited = [False] * vertices

        provinces = 0

        for city in range(vertices):

            if not visited[city]:

                provinces += 1

                self.dfs(
                    city,
                    graph,
                    visited
                )

        return provinces

    def buildGraph(self, isConnected):

        vertices = len(isConnected)

        graph = [[] for _ in range(vertices)]

        for city in range(vertices):

            for neighbor in range(vertices):

                if (
                    isConnected[city][neighbor] == 1
                    and city != neighbor
                ):
                    graph[city].append(neighbor)

        return graph

    def dfs(self, city, graph, visited):

        visited[city] = True

        for neighbor in graph[city]:

            if not visited[neighbor]:
                self.dfs(neighbor, graph, visited)


if __name__ == "__main__":

    solution = Solution()

    print(
        solution.findCircleNum(
            [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 1]
            ]
        )
    )  # 2