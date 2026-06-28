"""
LeetCode 283. Move Zeroes

Topic:
- Array
- Two Pointers

Pattern:
- Slow and Fast Pointer

Idea:
Move all non-zero elements to the front.
The slow pointer tracks the next position for a non-zero element.
The remaining positions will naturally become zeros after swaps.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # Initialize the slow pointer
        slow = 0

        # Traverse the array with the fast pointer
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # Swap the elements at slow and fast pointers
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # Move the slow pointer to the next position
                slow += 1

if __name__ == "__main__":  
    nums = [0, 1, 0, 3, 12]

    sol = Solution()
    sol.moveZeroes(nums)

    print(f"The modified array after moving zeroes is: {nums}")