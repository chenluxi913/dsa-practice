"""
LeetCode 15. 3Sum

Topic:
- Array
- Sorting
- Two Pointers

Pattern:
- Sort + Fixed One Number + Two Pointers

Idea:
Sort the array first.

Fix one number nums[i].

Use two pointers to find two numbers
whose sum equals -nums[i].

Skip duplicates to avoid repeated triplets.

Remember:

Sort
↓

Fix One Number

↓

Two Pointers

↓

Skip Duplicates

Time Complexity:
O(n log n) + O(n²) = O(n²)

Space Complexity:
O(1) extra space
O(log n) if counting the sorting recursion stack
"""

class Solution:
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        result = []

        for i in range(len(nums) - 2):

            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result
    
if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]