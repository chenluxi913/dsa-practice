"""
LeetCode 26. Remove Duplicates from Sorted Array

Topic:
- Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #slow pointer to the last unique element
        i = 0
        #fast pointer to traverse the array
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    sol = Solution()
    ans = sol.removeDuplicates(nums)

    print(f"The length of the array after removing duplicates is: {ans}")
    print(f"The modified array is: {nums[:ans]}")

        