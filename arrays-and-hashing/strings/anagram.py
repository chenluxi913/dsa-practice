"""
LeetCode 242. Valid Anagram

Topic:
- String
- Hash Table

Pattern:
- Character Counting

Idea:
Two strings are anagrams if they have
the same character counts.

Count each character in the first string.

Subtract each character in the second string.

If every count becomes zero,
the two strings are anagrams.

Remember:

Count

↓

Subtract

↓

Check All Zero

Time Complexity: O(n)

Space Complexity: O(1)

Only 26 lowercase English letters.
"""


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = [0] * 26

        for char in s:
            count[ord(char) - ord("a")] += 1

        for char in t:
            count[ord(char) - ord("a")] -= 1

        for frequency in count:
            if frequency != 0:
                return False

        return True
    
if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))  # Output: True