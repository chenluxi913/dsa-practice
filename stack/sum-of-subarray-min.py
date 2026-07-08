"""
LeetCode 907. Sum of Subarray Minimums

Topic:
- Array
- Stack
- Monotonic Stack

Pattern:
- Contribution
- Previous Smaller or Equal Element
- Next Smaller Element

Idea:
For each arr[i], count how many subarrays
use arr[i] as the minimum.

left  = i - previous_smaller_or_equal_index
right = next_smaller_index - i

contribution = arr[i] * left * right

Remember:
PSEE
↓
Current
↓
NSE
↓
Contribution

Time Complexity: O(n)
Space Complexity: O(n)
"""


from typing import List


class Solution:

    def findNSE(self, arr: List[int]) -> List[int]:
        n = len(arr)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            answer[i] = stack[-1] if stack else n

            stack.append(i)

        return answer

    def findPSEE(self, arr: List[int]) -> List[int]:
        n = len(arr)
        answer = [0] * n
        stack = []

        for i in range(n):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            answer[i] = stack[-1] if stack else -1

            stack.append(i)

        return answer

    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)

        total = 0

        for i in range(len(arr)):

            left = i - psee[i]
            right = nse[i] - i

            total += arr[i] * left * right
            total %= MOD

        return total
    
if __name__ == "__main__":
    solution = Solution()
    arr = [3, 1, 2, 4]
    print(solution.sumSubarrayMins(arr))  # Output: 17