"""
LeetCode 1043. Partition Array for Maximum Sum

Topic:
- Dynamic Programming
- Recursion
- Memoization
- Array
- Partition DP

Pattern:
- Try Partition Length 1 to k
- Track Maximum in Current Partition

Idea:
We partition the array into contiguous subarrays
with length at most k.

After choosing a partition, every value inside
that partition becomes the maximum value of
the partition.

For every starting index:

Try every possible partition length from:

1 to k

For each partition:

1. Update the maximum element in the current
   partition.

2. Calculate the contribution of the current
   partition:

   max_element * partition_length

3. Recursively solve the remaining array.

So:

current_sum =
max_element * partition_length
+
solve(next_index)

Take the maximum among all possible partition
lengths.

Base Case:

If start == n:

There are no elements left.

Return 0.

Remember:

Start at Index

↓

Try Length 1 ... k

↓

Track Current Maximum

↓

Current Partition Value =
Maximum * Length

↓

Solve Remaining Array

↓

Take Maximum

Time Complexity: O(n * k)

Space Complexity:
O(n) + O(n)
"""


from typing import List


class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)

        memo = [-1] * n

        return self.helper(arr, k, 0, memo)

    # Recursive function to find the maximum
    # sum starting from the current index.
    def helper(self, arr, k, start, memo):

        n = len(arr)

        # Base case.
        if start == n:
            return 0

        # Return the memoized result.
        if memo[start] != -1:
            return memo[start]

        max_sum = 0
        max_element = 0

        # Try partition lengths from 1 to k.
        for length in range(1, k + 1):

            if start + length > n:
                break

            # Update the maximum element
            # in the current partition.
            max_element = max(max_element, arr[start + length - 1])

            # Current partition contribution
            # plus the remaining maximum sum.
            current_sum = max_element * length + self.helper(arr, k, start + length, memo)

            max_sum = max(max_sum, current_sum)

        memo[start] = max_sum

        return memo[start]


if __name__ == "__main__":

    solution = Solution()

    arr = [1, 15, 7, 9, 2, 5, 10]
    k = 3

    print(solution.maxSumAfterPartitioning(arr, k))

    # Output:
    # 84