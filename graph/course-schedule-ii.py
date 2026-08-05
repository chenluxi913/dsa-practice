"""
LeetCode 210. Course Schedule II

Topic:
- Graph
- Breadth-First Search
- Topological Sort
- In-Degree

Pattern:
- Kahn's Algorithm
- BFS Topological Sort

Idea:
Build a directed graph using the prerequisite
relationships.

For each pair:

[course, prerequisite]

Add the directed edge:

prerequisite -> course

The in-degree of a course represents how many
prerequisites must still be completed before
that course can be taken.

First, add all courses with an in-degree of zero
to the queue because they have no prerequisites.

Then repeatedly:

1. Remove a course from the queue.
2. Add it to the course ordering.
3. Visit every course unlocked by it.
4. Decrease the neighbor's in-degree.
5. If the neighbor's in-degree becomes zero,
   add it to the queue.

If all courses are added to the ordering,
return the ordering.

If fewer than numCourses courses are processed,
the graph contains a cycle, so it is impossible
to finish all courses.

Remember:

Build Prerequisite -> Course Graph

↓

Calculate In-Degrees

↓

Add All Zero In-Degree Courses

↓

Process Courses with BFS

↓

Decrease Neighbors' In-Degrees

↓

Add Newly Unlocked Courses

↓

Check Whether All Courses Were Processed

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""


from collections import deque


class Solution:

    # Function to return the topological
    # ordering of the graph.
    def topoSort(
        self,
        V,
        adj
    ):

        # To store the in-degrees of nodes.
        in_degree = [0] * V

        # Calculate the in-degree of each node.
        for node in range(V):

            for neighbor in adj[node]:
                in_degree[neighbor] += 1

        # Queue to facilitate BFS.
        queue = deque()

        # Add all nodes with no incoming edges.
        for node in range(V):

            if in_degree[node] == 0:
                queue.append(node)

        # To store the topological ordering.
        order = []

        # Process nodes until the queue is empty.
        while queue:

            # Get the next available course.
            node = queue.popleft()

            # Add it to the ordering.
            order.append(node)

            # Traverse all courses unlocked
            # by the current course.
            for neighbor in adj[node]:

                # Remove the current prerequisite.
                in_degree[neighbor] -= 1

                # If all prerequisites have been
                # completed, add it to the queue.
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order

    def findOrder(
        self,
        numCourses,
        prerequisites
    ):

        # To store the directed graph.
        adj = [
            []
            for _ in range(numCourses)
        ]

        # Build the graph.
        for course, prerequisite in prerequisites:

            # prerequisite -> course
            adj[prerequisite].append(course)

        # Get the topological ordering.
        order = self.topoSort(
            numCourses,
            adj
        )

        # If all courses were not processed,
        # the graph contains a cycle.
        if len(order) < numCourses:
            return []

        return order


if __name__ == "__main__":

    solution = Solution()

    numCourses = 4

    prerequisites = [
        [1, 0],
        [2, 0],
        [3, 1],
        [3, 2]
    ]

    print(
        solution.findOrder(
            numCourses,
            prerequisites
        )
    )

    # Possible Output:
    # [0, 1, 2, 3]
    #
    # Another Valid Output:
    # [0, 2, 1, 3]