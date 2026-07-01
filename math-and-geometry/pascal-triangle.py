"""
leetcode 118, 119
Pascal Triangle

Topic:
- Array
- Math
- Combinatorics

Pattern:
- Binomial Coefficient (nCr)

Applications:

1. Pascal Triangle I
   Return one element

2. Pascal Triangle II (LeetCode 119)
   Return one row

3. Pascal Triangle (LeetCode 118)
   Return the whole triangle

Core Formula:

Pascal[row][col] = C(row, col)

Remember:

One Element
↓

One Row

↓

Whole Triangle

All are based on nCr()

Time Complexity:

nCr           O(min(r, n-r))

One Element   O(min(r, n-r))

One Row       O(n²)

Whole Triangle O(n²)

Space Complexity:

nCr           O(1)

One Row       O(n)

Whole Triangle O(n²)
=========================================================
"""


class PascalTriangle:

    ##################################################
    # Universal Combination Formula
    ##################################################

    def nCr(self, n: int, r: int) -> int:

        r = min(r, n - r)

        result = 1

        for i in range(r):
            result *= (n - i)
            result //= (i + 1)

        return result

    ##################################################
    # Pascal Triangle I
    # Return one element
    ##################################################

    def getElement(self, row: int, col: int) -> int:
        """
        row and col are 1-indexed.

        Example:
        row = 5
        col = 3

        return 6
        """

        return self.nCr(row - 1, col - 1)

    ##################################################
    # Pascal Triangle II (LC119)
    # Return one row
    ##################################################

    def getRow(self, rowIndex: int):

        row = []

        for col in range(rowIndex + 1):
            row.append(self.nCr(rowIndex, col))

        return row

    ##################################################
    # Pascal Triangle (LC118)
    # Return whole triangle
    ##################################################

    def generate(self, numRows: int):

        triangle = []

        for row in range(numRows):

            current = []

            for col in range(row + 1):
                current.append(self.nCr(row, col))

            triangle.append(current)

        return triangle


##################################################
# Example
##################################################

if __name__ == "__main__":

    pascal = PascalTriangle()

    print("One Element")
    print(pascal.getElement(5, 3))
    print()

    print("One Row")
    print(pascal.getRow(4))
    print()

    print("Whole Triangle")
    print(pascal.generate(5))