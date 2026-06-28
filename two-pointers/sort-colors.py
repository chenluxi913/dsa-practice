"""
LeetCode 75. Sort Colors

Topic:
- Array
- Two Pointers

Pattern:
- Dutch National Flag

Idea:
Maintain three regions:

0s | 1s | Unknown | 2s

left  = next position for 0
mid   = current element
right = next position for 2

Rules:
0 -> swap with left, left++, mid++
1 -> mid++
2 -> swap with right, right--

Remember:
0 goes Left
1 stays Middle
2 goes Right

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left, mid, right = 0, 0, len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1

if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]

    sol = Solution()
    sol.sortColors(nums)

    print(f"The modified array after sorting colors is: {nums}")