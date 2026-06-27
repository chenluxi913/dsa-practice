"""
LeetCode 540. Single Element in a Sorted Array

Topic:
- Binary Search

Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:
    def singleNonDuplicate(self, nums:list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # make sure mid is even
            if mid % 2 == 1:
                mid -= 1

            # so we alwanys compare the first element of the pair with the second element of the pair
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            
            # Pair is valid, search the right half.

            else:
                right = mid

            # Pair is broken, search the left half.

        return nums[left]
    
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 4, 5, 5]

    sol = Solution()
    ans = sol.singleNonDuplicate(nums)

    print(f"The single element is: {ans}")