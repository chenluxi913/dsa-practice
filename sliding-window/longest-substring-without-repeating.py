"""
LeetCode 3. Longest Substring Without Repeating Characters

Topic:
- String
- Hash Set
- Sliding Window

Pattern:
- Variable Size Sliding Window

Idea:
Maintain a window with no duplicate characters.

Use a set to store characters inside the window.

Move right to expand the window.

If s[right] already exists in the set,
move left until duplicate is removed.

Remember:

Expand Right

↓

Remove Duplicates

↓

Update Answer

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()

        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length
    
if __name__ == "__main__":
    s = "abcabcbb"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)  # Output: 3