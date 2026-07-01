"""
LeetCode 493. Reverse Pairs

Topic:
- Array
- Divide and Conquer
- Merge Sort

Pattern:
- Merge Sort + Count Pairs

Idea:
A reverse pair is:

i < j
nums[i] > 2 * nums[j]

Use merge sort.

Before merging two sorted halves,
count reverse pairs across the two halves.

Because both halves are sorted,
we can use two pointers to count efficiently.

Remember:

Sort Left

↓

Sort Right

↓

Count Pairs

↓

Merge

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


from typing import List


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums: List[int], low: int, high: int) -> int:

        if low >= high:
            return 0

        mid = (low + high) // 2

        count = 0
        # Sort left half and right half, and count reverse pairs across them
        count += self.merge_sort(nums, low, mid)
        count += self.merge_sort(nums, mid + 1, high)
        # Count reverse pairs across the two sorted halves
        count += self.count_pairs(nums, low, mid, high)

        self.merge(nums, low, mid, high)

        return count

    def count_pairs(
        self,
        nums: List[int],
        low: int,
        mid: int,
        high: int
    ) -> int:

        right = mid + 1
        count = 0
        # Count reverse pairs across the two sorted halves
        for left in range(low, mid + 1):

            while right <= high and nums[left] > 2 * nums[right]:
                right += 1

            count += right - (mid + 1)

        return count

    def merge(
        self,
        nums: List[int],
        low: int,
        mid: int,
        high: int
    ) -> None:

        temp = []

        left = low
        right = mid + 1

        while left <= mid and right <= high:

            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1

            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1

        while right <= high:
            temp.append(nums[right])
            right += 1

        nums[low:high + 1] = temp


if __name__ == "__main__":

    nums = [1, 3, 2, 3, 1]

    sol = Solution()

    print("Reverse pairs:", sol.reversePairs(nums))