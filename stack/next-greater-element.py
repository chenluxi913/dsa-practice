"""
LeetCode 503. Next Greater Element II

Topic:
- Array
- Stack
- Monotonic Stack

Pattern:
- Monotonic Decreasing Stack
- Circular Array

Idea:
Traverse the array from right to left twice.

Use i % n to simulate a circular array.

Maintain a decreasing stack.

For each element:
1. Pop all elements <= current.
2. If stack is not empty, stack top is the next greater element.
3. Push current element into stack.

Remember:

Traverse Backward Twice
↓
Use i % n
↓
Pop Smaller
↓
Top is Answer

Time Complexity: O(n)
Space Complexity: O(n)
"""


from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)

        answer = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):

            index = i % n
            current = nums[index]

            while stack and stack[-1] <= current:
                stack.pop()

            if i < n:
                if stack:
                    answer[index] = stack[-1]

            stack.append(current)

        return answer
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 1, 10, 3, 4, 5]
    print(solution.nextGreaterElements(nums))  # Output: [2, -1, 2]