"""
LeetCode 205. Isomorphic Strings

Topic:
- String
- Hash Map

Pattern:
- Two Hash Maps
- One-to-One Mapping

Idea:
Each character in s must map to exactly one character in t.

Each character in t must also map back to exactly one character in s.

So we need two maps:

s_to_t
t_to_s

Remember:
Forward Map
↓
Backward Map
↓
Check Consistency

Time Complexity: O(n)
Space Complexity: O(1)
Because ASCII characters are limited.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True
    
if __name__ == "__main__":
    solution = Solution()
    s = "egg"
    t = "add"
    print(solution.isIsomorphic(s, t))  # Output: True

    s = "foo"
    t = "bar"
    print(solution.isIsomorphic(s, t))  # Output: False

    s = "paper"
    t = "title"
    print(solution.isIsomorphic(s, t))  # Output: True