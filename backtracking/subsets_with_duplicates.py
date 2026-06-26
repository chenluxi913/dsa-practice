class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        subset = []

        def backtrack(start):
            ans.append(subset[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        backtrack(0)
        return ans
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 2]
    print(solution.subsetsWithDup(nums))  # Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]