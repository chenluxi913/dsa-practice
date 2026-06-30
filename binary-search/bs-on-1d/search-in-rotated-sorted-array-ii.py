"""
LeetCode 81. Search in Rotated Sorted Array II

Topic:
- Array
- Binary Search

Pattern:
- Rotated Binary Search with Duplicates

Idea:
Same as LeetCode 33, but nums may contain duplicates.

When nums[left] == nums[mid] == nums[right],
we cannot know which half is sorted.

So shrink both ends.

Remember:
Duplicates block the sorted-half check.

Time Complexity:
Average: O(log n)
Worst: O(n)

Space Complexity: O(1)
"""

class Solution:

    # Solution 1: Iterative
    # Time: Average: O(log n), Worst: O(n)
    # Space: O(1)
    def search(self, nums: List[int], target: int) -> bool:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            #cannot determine which half is sorted
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            
            #left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            #right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
    
    if __name__ == "__main__":
        solution = Solution()
        nums = [2,5,6,0,0,1,2]
        target = 0
        print(solution.search(nums, target))  # Output: True

        nums = [2,5,6,0,0,1,2]
        target = 3
        print(solution.search(nums, target))  # Output: False

        nums = [1,0,1,1,1]
        target = 0
        print(solution.search(nums, target))  # Output: True