"""
LeetCode 18. 4Sum

Topic:
- Array
- Sorting
- Two Pointers

Pattern:
- Sort + Fix Two Numbers + Two Pointers

Idea:
Sort the array first.

Fix nums[i] and nums[j].

Then use two pointers to find
nums[left] + nums[right]
equal to:

target - nums[i] - nums[j]

Skip duplicates at every level.

Remember:

Sort
↓
Fix First
↓
Fix Second
↓
Two Pointers
↓
Skip Duplicates

Time Complexity: O(n³)
Space Complexity: O(1) extra space
"""


from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        result = []
        n = len(nums)

        for i in range(n - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(solution.fourSum(nums, target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]