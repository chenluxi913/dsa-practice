"""
LeetCode 88. Merge Sorted Array

Topic:
- Array
- Two Pointers

Pattern:
- Merge From Back

Idea:
nums1 has extra space at the end.

Use three pointers:

left  -> last valid element in nums1
right -> last element in nums2
index -> last position in nums1

Compare nums1[left] and nums2[right].

Place the larger one at nums1[index].

Continue until nums2 is exhausted.

Remember:

Back
↓

Compare

↓

Place Larger

↓

Move Pointer

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        left = m - 1
        right = n - 1
        index = m + n - 1

        # Merge from the back of nums1
        while right >= 0 and left >= 0:
            if nums1[left] > nums2[right]:
                nums1[index] = nums1[left]
                left -= 1
            else:
                nums1[index] = nums2[right]
                right -= 1
            index -= 1

        # If there are remaining elements in nums2, copy them
        while right >= 0:
            nums1[index] = nums2[right]
            right -= 1
            index -= 1

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
        