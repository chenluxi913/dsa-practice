"""
LeetCode 229. Majority Element II

Topic:
- Array

Pattern:
- Boyer-Moore Voting Algorithm

Idea:
Elements appearing more than n/3 times
can have at most 2 candidates.

Step 1:
Find two possible candidates.

Step 2:
Verify their real counts.

Remember:
Vote
↓
Cancel
↓
Verify

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:

    def majorityElement(self, nums: list[int]) -> list[int]:

        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in nums:

            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Verify the candidates
        result = []
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > len(nums) // 3:
                result.append(candidate)

        return result
    
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3, 1, 1, 1, 2, 2]
    print(solution.majorityElement(nums))  # Output: [3, 2]