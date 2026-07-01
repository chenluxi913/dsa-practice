"""
LeetCode 31. Next Permutation

Topic:
- Array
- Two Pointers

Pattern:
- Find Pivot
- Swap
- Reverse Suffix

Idea:
Find the next lexicographically greater permutation.

Steps:
1. Find the first index i from the right where nums[i] < nums[i + 1].
2. Find the first index j from the right where nums[j] > nums[i].
3. Swap nums[i] and nums[j].
4. Reverse the suffix after i.

If no pivot exists, reverse the whole array.

Remember:
Find Pivot
↓
Find Bigger
↓
Swap
↓
Reverse Suffix

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = n - 2

        # Step 1: Find the first index i from the right where nums[i] < nums[i + 1].
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            # Step 2: Find the first index j from the right where nums[j] > nums[i].
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap nums[i] and nums[j].
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the suffix after i.
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    print(nums)  # Output: [1, 3, 2]