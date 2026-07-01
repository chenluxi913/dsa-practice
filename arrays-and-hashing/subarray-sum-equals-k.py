"""
LeetCode 560. Subarray Sum Equals K

Topic:
- Array
- Hash Map
- Prefix Sum

Pattern:
- Prefix Sum + Hash Map

Idea:
Let:

prefix_sum = sum of elements from index 0 to i

If:

current_prefix_sum - previous_prefix_sum = k

Then:

previous_prefix_sum = current_prefix_sum - k

Store every prefix sum and its frequency in a hash map.

Remember:
Current Prefix
↓

Current - k

↓

Count Previous Prefix

Time Complexity: O(n)
Space Complexity: O(n)
"""


from typing import List


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum_map = {0: 1}

        current_prefix_sum = 0
        subarray_count = 0

        for num in nums:

            # Update current prefix sum
            current_prefix_sum += num

            # Previous prefix sum needed
            sum_to_remove = current_prefix_sum - k

            # Count all matching subarrays
            subarray_count += prefix_sum_map.get(sum_to_remove, 0)

            # Record current prefix sum
            prefix_sum_map[current_prefix_sum] = (
                prefix_sum_map.get(current_prefix_sum, 0) + 1
            )

        return subarray_count
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1]
    k = 2
    print(solution.subarraySum(nums, k))  # Output: 2