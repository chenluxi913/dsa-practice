"""
LeetCode 1248. Count Number of Nice Subarrays

Topic:
- Array
- Sliding Window

Pattern:
- Exactly K = AtMost(K) - AtMost(K - 1)

Idea:
A nice subarray has exactly k odd numbers.

Count subarrays with at most k odd numbers,
then subtract subarrays with at most k - 1 odd numbers.

Exactly(k)
=
AtMost(k)
-
AtMost(k - 1)

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums: List[int], k: int) -> int:

        if k < 0:
            return 0

        left = 0
        odd_count = 0
        count = 0

        for right in range(len(nums)):

            if nums[right] % 2 == 1:
                odd_count += 1

            while odd_count > k:

                if nums[left] % 2 == 1:
                    odd_count -= 1

                left += 1

            count += right - left + 1

        return count
    
if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    k = 3
    solution = Solution()
    result = solution.numberOfSubarrays(nums, k)
    print(result)  # Output: 2