"""
LeetCode 76. Minimum Window Substring

Topic:
- String
- Sliding Window
- Hash Array

Pattern:
- Minimum Valid Window

Idea:
Count the frequency of characters in t.

Expand the window by moving the right pointer.

If the current character is still needed,
increase the matched character count.

When all characters in t are matched,
shrink the window from the left while
keeping it valid.

Update the minimum window during shrinking.

Remember:

Expand Right
↓

Match Characters

↓

Window Becomes Valid

↓

Update Answer

↓

Shrink Left

Time Complexity: O(m + n)
Space Complexity: O(1)
"""


class Solution:

    def minWindow(self, s: str, t: str) -> str:

        freq = [0] * 256

        for char in t:
            freq[ord(char)] += 1

        left = 0
        matched = 0

        min_length = float("inf")
        start = -1

        for right in range(len(s)):

            if freq[ord(s[right])] > 0:
                matched += 1

            freq[ord(s[right])] -= 1

            while matched == len(t):

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                freq[ord(s[left])] += 1

                if freq[ord(s[left])] > 0:
                    matched -= 1

                left += 1

        if start == -1:
            return ""

        return s[start:start + min_length]
    
if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    result = solution.minWindow(s, t)
    print(result)  # Output: "BANC"