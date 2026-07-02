"""
LeetCode 410. Split Array Largest Sum

Topic:
- Array
- Binary Search

Pattern:
- Binary Search on Answer
- Minimum Valid Answer

Idea:
Search the minimum possible largest subarray sum.

For each candidate largest sum:

Greedily split the array.

If adding the next number exceeds
the candidate sum,

start a new subarray.

If the required number of subarrays
is less than or equal to k,

the candidate works.

Try a smaller answer.

Otherwise,

the candidate is too small.

Try a larger answer.

Remember:

Binary Search on Largest Sum

↓

Count Subarrays

↓

Minimum Valid Answer

Time Complexity: O(n log S)

n = len(nums)
S = sum(nums)

Space Complexity: O(1)
"""

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        while left < right:

            mid = (left + right) // 2

            if self.countSubarrays(nums, mid) <= k:
                right = mid
            else:
                left = mid + 1

        return left # always return left

    def countSubarrays(self, nums: list[int], largest_sum: int) -> int:

        subarrays = 1 # at least one subarray
        current_sum = 0

        for num in nums:

            if current_sum + num > largest_sum:
                subarrays += 1
                current_sum = 0

            current_sum += num

        return subarrays
    
if __name__ == "__main__":
    nums = [7, 2, 5, 10, 8]
    k = 2

    sol = Solution()
    min_largest_sum = sol.splitArray(nums, k)
    print(f"The minimum largest sum for splitting the array into {k} subarrays is: {min_largest_sum}")