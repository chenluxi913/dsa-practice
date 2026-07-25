"""
LeetCode 207. Course Schedule

Topic:
- Graph
- DFS

Pattern:
- Directed Graph Cycle Detection
- Three-State DFS

Idea:
Each course is a node.

For every pair:

[course, prerequisite]

Build the directed edge:

prerequisite -> course

Use three states to detect a cycle:

0 = Unvisited
1 = Visiting
2 = Visited

If DFS reaches a node whose state is 1,
the node is already on the current recursion path,
so a cycle exists.

If any cycle exists, not all courses can be completed.

Remember:

Build Directed Graph

↓

0 = Unvisited

↓

Mark Current Node as 1

↓

DFS All Neighbors

↓

Meet State 1 → Cycle

↓

Finish Current Node → Mark as 2

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""


class Solution:

    def canFinish(self, numCourses, prerequisites):

        # Build adjacency list.
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # 0 = unvisited
        # 1 = visiting
        # 2 = visited
        state = [0] * numCourses

        # The graph may contain disconnected components,
        # so start DFS from every unvisited course.
        for course in range(numCourses):

            if state[course] == 0:

                if self.hasCycle(course, graph, state):
                    return False

        return True

    def hasCycle(self, course, graph, state):

        # Mark the course as part of
        # the current recursion path.
        state[course] = 1

        for next_course in graph[course]:

            # A visiting neighbor is already on the
            # current DFS path, so a cycle exists.
            if state[next_course] == 1:
                return True

            # Only perform DFS on unvisited courses.
            if state[next_course] == 0:

                if self.hasCycle(next_course, graph, state):
                    return True

        # All neighbors have been safely processed.
        state[course] = 2

        return False


if __name__ == "__main__":

    solution = Solution()

    print(
        solution.canFinish(
            2,
            [[1, 0]]
        )
    )  # True

    print(
        solution.canFinish(
            2,
            [[1, 0], [0, 1]]
        )
    )  # False