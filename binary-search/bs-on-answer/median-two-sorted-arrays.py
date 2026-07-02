"""
LeetCode 4. Median of Two Sorted Arrays

Topic:
- Array
- Binary Search

Pattern:
- Binary Search on Partition

Idea:
Partition two sorted arrays into left half and right half.

We need:

1. left half has the same size as right half
   or one more element.

2. every element in left half <= every element in right half.

Condition:
maxLeft1 <= minRight2
and
maxLeft2 <= minRight1

Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> float:

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m


        while left <= right: # <= because we want to include the case where cut1 = m
            # while left < right use for find minimum valid answer
            # while left <= right use for find valid partition

            cut1 = (left + right) // 2
            cut2 = (m + n + 1) // 2 - cut1 # +1 to handle odd length


            left1 = nums1[cut1 - 1] if cut1 > 0 else float("-inf")
            left2 = nums2[cut2 - 1] if cut2 > 0 else float("-inf")

            right1 = nums1[cut1] if cut1 < m else float("inf")
            right2 = nums2[cut2] if cut2 < n else float("inf")

            if left1 <= right2 and left2 <= right1:

                if (m + n) % 2 == 1:
                    return max(left1, left2)

                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                right = cut1 - 1

            else:
                left = cut1 + 1
        return 0.0 # should not reach here

if __name__ == "__main__":
    nums1 = [1, 3, 6, 8]
    nums2 = [2, 8, 10, 12]

    sol = Solution()
    median = sol.findMedianSortedArrays(nums1, nums2)
    print(f"The median of the two sorted arrays is: {median}")