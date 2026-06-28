"""
LeetCode 189. Rotate Array

Topic:
- Array
- Reversal

Pattern:
- Three Reverses

Idea:

Right Rotation
Whole → Front → Back

Left Rotation
Front → Back → Whole

Remember:
Right = Reverse Whole First
Left  = Reverse Whole Last

vTime Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:


    # Helper function to reverse a portion of the array
    def reverse(self, nums: list[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotateRight(self,nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k is greater than n

        # Reverse the entire array
        self.reverse(nums, 0, n - 1)
        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # Reverse the remaining n-k elements
        self.reverse(nums, k, n - 1)

    def rotateLeft(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k is greater than n

        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # Reverse the remaining n-k elements
        self.reverse(nums, k, n - 1)
        # Reverse the entire array
        self.reverse(nums, 0, n - 1)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    sol = Solution()
    sol.rotateRight(nums, k)
    print(f"The array after rotating right by {k} positions is: {nums}")

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    sol.rotateLeft(nums, k)
    print(f"The array after rotating left by {k} positions is: {nums}")