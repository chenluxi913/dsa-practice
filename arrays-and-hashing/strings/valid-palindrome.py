"""
LeetCode 125. Valid Palindrome

Topic:
- String
- Two Pointers
- Recursion

Pattern:
- Iterative Two Pointers
- Recursive Two Pointers

Idea:
Check characters from both ends.

Skip non-alphanumeric characters.
Compare characters ignoring case.

Remember:
Skip
↓
Compare
↓
Move / Recurse

Time Complexity: O(n)

Space Complexity:
- Iterative: O(1)
- Recursive: O(n)
"""


class Solution:

    # Iterative version
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    # Recursive version
    def isPalindromeRecursive(self, s: str) -> bool:
        return self.check(s, 0, len(s) - 1)

    def check(self, s: str, left: int, right: int) -> bool:

        if left >= right:
            return True

        if not s[left].isalnum():
            return self.check(s, left + 1, right)

        if not s[right].isalnum():
            return self.check(s, left, right - 1)

        if s[left].lower() != s[right].lower():
            return False

        return self.check(s, left + 1, right - 1)


if __name__ == "__main__":

    sol = Solution()

    tests = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "0P"
    ]

    for s in tests:
        print("Input:", s)
        print("Iterative:", sol.isPalindrome(s))
        print("Recursive:", sol.isPalindromeRecursive(s))
        print("-" * 30)