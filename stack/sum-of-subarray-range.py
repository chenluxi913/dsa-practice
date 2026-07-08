"""
LeetCode 2104. Sum of Subarray Ranges

Idea:
Range of subarray = maximum - minimum

So:

Answer =
sum of all subarray maximums
-
sum of all subarray minimums

Use contribution method.

Minimum:
NSE  -> pop >=
PSEE -> pop >

Maximum:
NGE  -> pop <=
PGEE -> pop <

For each arr[i]:

Contribution as minimum:
arr[i] * left_min * right_min

Contribution as maximum:
arr[i] * left_max * right_max

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def findNSE(self, nums):
        n = len(nums)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # next smaller element
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            answer[i] = stack[-1] if stack else n

            stack.append(i)

        return answer
    
    def findNGE(self, nums):
        n = len(nums)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # next greater element
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            answer[i] = stack[-1] if stack else n

            stack.append(i)

        return answer
    
    def findPSEE(self, nums):
        n = len(nums)
        answer = [0] * n
        stack = []

        for i in range(n):
            # previous smaller or equal element
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()

            answer[i] = stack[-1] if stack else -1

            stack.append(i)

        return answer
    
    def findPGEE(self, nums):
        n = len(nums)
        answer = [0] * n
        stack = []

        for i in range(n):
            # previous greater or equal element
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()

            answer[i] = stack[-1] if stack else -1

            stack.append(i)

        return answer
    
    def sumSubarrayRanges(self, nums):
        n = len(nums)
        left_min = self.findPSEE(nums)
        right_min = self.findNSE(nums)
        left_max = self.findPGEE(nums)
        right_max = self.findNGE(nums)

        total_min = 0
        total_max = 0

        for i in range(n):
            left_count_min = i - left_min[i]
            right_count_min = right_min[i] - i
            total_min += nums[i] * left_count_min * right_count_min

            left_count_max = i - left_max[i]
            right_count_max = right_max[i] - i
            total_max += nums[i] * left_count_max * right_count_max

        return total_max - total_min
    
if __name__ == "__main__":
    solution = Solution()
    arr = [1, 2, 3]
    print(solution.sumSubarrayRanges(arr))  # Output: 4