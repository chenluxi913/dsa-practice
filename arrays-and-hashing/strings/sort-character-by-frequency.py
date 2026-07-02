"""
LeetCode 451. Sort Characters By Frequency

Topic:
- String
- Hash Map
- Sorting

Pattern:
- Count Frequency + Sort

Idea:
Count each character's frequency.

Sort characters by frequency in decreasing order.

Build the result by repeating each character
according to its frequency.

Remember:
Count
↓
Sort by Frequency
↓
Build String

Time Complexity: O(n log k)
k = number of unique characters

Space Complexity: O(n)

"""
from collections import Counter

class Solution:

    def frequencySort(self, s: str) -> str:

        # Count frequency of each character
        count = Counter(s)

        # Sort characters by frequency in decreasing order
        sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)
        #sorted_chars = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        # Build the result string
        result = []
        for char, freq in sorted_chars:
            result.append(char * freq)
            #result.append(char * count[char])

        return ''.join(result)
    
if __name__ == "__main__":
    solution = Solution()
    s = "tree"
    print(solution.frequencySort(s))  # Output: "eert" or "eetr"
