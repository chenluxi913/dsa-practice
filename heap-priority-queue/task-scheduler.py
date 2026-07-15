"""
LeetCode 621. Task Scheduler

Topic:
- Greedy
- Heap
- Queue
- Hash Map
- Simulation

Pattern:
- Max Heap with Cooldown Queue

Idea:
Use a max heap to always execute the task
with the highest remaining frequency.

Python only provides a min heap, so store
each frequency as a negative number.

Use a queue to store tasks that are cooling down.

Each queue element stores:

(remaining_count, available_time)

For every CPU interval:

1. Increase the current time.
2. If the heap is not empty:
   - Execute the most frequent available task.
   - Decrease its remaining frequency.
   - If it still has remaining executions,
     place it into the cooldown queue.
3. Move a task back into the heap when
   its cooldown period finishes.
4. If no task is currently available,
   jump directly to the next available time.

Remember:

Choose Most Frequent Task

↓

Execute Once

↓

Put into Cooldown Queue

↓

Cooldown Finishes

↓

Push Back into Heap

Time Complexity: O(m log 26)
Space Complexity: O(26)

where m is the total number of CPU intervals.
Since there are only 26 task types,
the heap size is at most 26.
"""

from collections import Counter, deque
from typing import List
import heapq


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)

        max_heap = [-frequency for frequency in count.values()]

        heapq.heapify(max_heap)

        cooldown = deque()

        time = 0

        while max_heap or cooldown:

            time += 1

            if max_heap:

                remaining = heapq.heappop(max_heap) + 1

                if remaining:
                    cooldown.append(
                        (remaining, time + n)
                    )

            else:
                time = cooldown[0][1]

            if cooldown and cooldown[0][1] == time:
                remaining, available_time = cooldown.popleft()
                heapq.heappush(max_heap, remaining)

        return time


if __name__ == "__main__":

    solution = Solution()

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    print(solution.leastInterval(tasks, n))  # 8