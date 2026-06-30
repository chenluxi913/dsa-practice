"""
LeetCode 704. Binary Search

Topic:
- Array
- Binary Search

Pattern:
- Iterative Binary Search
- Recursive Binary Search

Idea:
Search in a sorted array.

Compare the middle element with the target.

If target is smaller:
Search the left half.

If target is larger:
Search the right half.

Remember:
Find Mid
↓

Compare

↓

Discard Half

Time Complexity: O(log n)

Space Complexity:
- Iterative: O(1)
- Recursive: O(log n)
"""


from typing import List


class Solution:

    # Solution 1: Iterative
    # Time: O(log n)
    # Space: O(1)
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1

    # Solution 2: Recursive
    # Time: O(log n)
    # Space: O(log n)
    def search_recursive(self, nums: List[int], target: int) -> int:

        def dfs(left: int, right: int) -> int:

            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return dfs(mid + 1, right)

            else:
                return dfs(left, mid - 1)

        return dfs(0, len(nums) - 1)


if __name__ == "__main__":

    sol = Solution()

    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    print("Iterative :", sol.search(nums, target))
    print("Recursive :", sol.search_recursive(nums, target))