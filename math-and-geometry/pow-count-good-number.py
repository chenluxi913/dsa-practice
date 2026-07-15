"""
LeetCode 1922. Count Good Numbers

Topic:
- Math
- Fast Exponentiation
- Modular Arithmetic

Pattern:
- Count Choices by Position

Idea:
A good digit string satisfies:

Even index:
0, 2, 4, 6, 8

→ 5 choices

Odd index:
2, 3, 5, 7

→ 4 choices

For a string of length n:

Even positions:
(n + 1) // 2

Odd positions:
n // 2

The answer is:

5^(even_positions)
*
4^(odd_positions)

Since n can be as large as 10^15,
use Binary Exponentiation.

Binary Exponentiation:

If exponent is odd:
Multiply the current result.

Square the base.

Divide the exponent by 2.

Repeat until the exponent becomes 0.

Remember:

Count Even Positions

↓

Count Odd Positions

↓

Binary Exponentiation

↓

Multiply Both Results

↓

Take Modulo

Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:

    def countGoodNumbers(self, n):

        MOD = 10**9 + 7

        even = (n + 1) // 2
        odd = n // 2

        return (
            self.power(5, even, MOD)
            * self.power(4, odd, MOD)
        ) % MOD

    def power(self, base, exponent, mod):

        result = 1

        while exponent > 0:

            if exponent % 2 == 1:
                result = (
                    result * base
                ) % mod

            base = (base * base) % mod

            exponent //= 2

        return result


if __name__ == "__main__":

    solution = Solution()

    print(solution.countGoodNumbers(1))    # 5
    print(solution.countGoodNumbers(4))    # 400
    print(solution.countGoodNumbers(50))   # 564908303