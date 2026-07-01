"""
LeetCode 152. Maximum Product Subarray

Topic:
- Array

Pattern:
- Prefix Product
- Suffix Product

Idea:
Traverse from both directions.

Maintain:

prefix product
suffix product

Reset to 1 whenever product becomes 0.

The maximum product subarray
must appear as either:

- a prefix product
- a suffix product

Remember:

Left Product
↓

Right Product

↓

Take Maximum

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)

        prefix = 1
        suffix = 1

        answer = float("-inf")

        for i in range(n):

            # Restart after zero
            if prefix == 0:
                prefix = 1

            if suffix == 0:
                suffix = 1

            # Prefix product
            prefix *= nums[i]

            # Suffix product
            suffix *= nums[n - 1 - i]

            answer = max(answer, prefix, suffix)

        return answer
    
if __name__ == "__main__":
    nums = [2, 3, -2, 4]

    sol = Solution()
    max_product = sol.maxProduct(nums)
    print(f"The maximum product subarray is: {max_product}")