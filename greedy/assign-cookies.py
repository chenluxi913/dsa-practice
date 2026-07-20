"""
LeetCode 455. Assign Cookies

Topic:
- Greedy
- Sorting
- Two Pointers

Pattern:
- Greedy Matching

Idea:
Each child needs one cookie whose size
is at least their greed factor.

Sort both arrays.

Always use the smallest cookie that can
satisfy the least greedy child.

If the current cookie is too small:
    Skip the cookie.

Otherwise:
    Assign the cookie to the child.
    Move to the next child.

Why Greedy Works:

Suppose the current child has the
smallest greed.

If a cookie cannot satisfy this child,
it cannot satisfy any later child
because later children are greedier.

If a cookie can satisfy this child,
using a larger cookie would only waste
a larger resource.

Therefore assigning the smallest
possible cookie is always optimal.

Algorithm:

Sort children.
Sort cookies.

child = 0
cookie = 0

while child < len(children)
      and cookie < len(cookies):

    if cookie >= greed:
        satisfy child
        child++

    cookie++

Answer = number of satisfied children.

Time Complexity: O(n log n + m log m)
Space Complexity: O(1)
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):

            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return child
    
if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]
    print(Solution().findContentChildren(g, s))  # Output: 1

    g = [1, 2]
    s = [1, 2, 3]
    print(Solution().findContentChildren(g, s))  # Output: 2