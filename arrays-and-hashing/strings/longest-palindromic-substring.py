"""
LeetCode 5. Longest Palindromic Substring

Topic:
- String
- Two Pointers

Pattern:
- Expand Around Center

Idea:
Every palindrome has a center.

For each index:

1. Expand odd-length palindrome.
2. Expand even-length palindrome.
3. Update the longest palindrome.

Remember:

Center

↓

Expand

↓

Update Answer

Time Complexity: O(n²)

Space Complexity: O(1)
"""


class Solution:

    def expandAroundCenter(self, s: str, left: int, right: int):

        while (
            left >= 0
            and right < len(s)
            and s[left] == s[right]
        ):
            left -= 1
            right += 1

        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):

            # Odd-length palindrome
            left1, right1 = self.expandAroundCenter(s, i, i)

            # Even-length palindrome
            left2, right2 = self.expandAroundCenter(s, i, i + 1)

            if right1 - left1 > end - start:
                start = left1
                end = right1

            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end + 1]
    
if __name__ == "__main__":
    solution = Solution()
    s = "babad"
    print(solution.longestPalindrome(s))  # Output: "bab" or "aba"