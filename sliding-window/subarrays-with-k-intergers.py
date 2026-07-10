"""
LeetCode 992. Subarrays with K Different Integers

Topic:
- Array
- Hash Map
- Sliding Window

Pattern:
- Exactly K = AtMost(K) - AtMost(K - 1)

Idea:
Count subarrays with exactly k distinct integers.

Exactly(k)
=
AtMost(k)
-
AtMost(k - 1)

Time Complexity: O(n)
Space Complexity: O(n)
"""


from typing import List


class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums: List[int], k: int) -> int:

        count = {}

        left = 0
        answer = 0

        for right in range(len(nums)):

            count[nums[right]] = count.get(nums[right], 0) + 1

            while len(count) > k:

                count[nums[left]] -= 1

                if count[nums[left]] == 0:
                    del count[nums[left]]

                left += 1

            answer += right - left + 1

        return answer
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 1, 2, 3]
    k = 2
    result = solution.subarraysWithKDistinct(nums, k)
    print(result)  # Output: 7