"""
LeetCode 424. Longest Repeating Character Replacement

Topic:
- String
- Sliding Window
- Hash Array

Pattern:
- Variable Size Sliding Window

Idea:
Maintain a window.

For each window:

window_length - max_frequency

is the number of characters that need to be replaced.

If replacements_needed > k,
shrink the window from the left.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = [0] * 26

        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):

            index = ord(s[right]) - ord("A")
            count[index] += 1

            max_frequency = max(max_frequency, count[index])

            while (right - left + 1) - max_frequency > k:
                left_index = ord(s[left]) - ord("A")
                count[left_index] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
    
if __name__ == "__main__":
    s = "ABABCB"
    k = 2
    solution = Solution()
    result = solution.characterReplacement(s, k)
    print(result)  # Output: 4