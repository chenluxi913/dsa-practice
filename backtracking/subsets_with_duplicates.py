"""
LeetCode 90. Subsets II

Topic:
- Backtracking

Time Complexity: O(n * 2^n)
Space Complexity: O(n)
"""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        subset = []

        def backtrack(start):
            # Add the current subset to the answer list
            ans.append(subset[:])

            #try every possible next element
            for i in range(start, len(nums)):

                #skip duplicates at the same recursive depth
                if i > start and nums[i] == nums[i - 1]:
                    continue
                #chose the current element
                subset.append(nums[i])

                #explore further with the current element included
                backtrack(i + 1)

                #undo the choice for backtracking
                subset.pop()
                
        backtrack(0)
        return ans
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 2]
    print(solution.subsetsWithDup(nums))  # Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]