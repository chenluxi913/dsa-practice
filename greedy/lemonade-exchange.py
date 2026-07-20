"""
LeetCode 860. Lemonade Change

Topic:
- Greedy
- Simulation

Pattern:
- Track Available Resources

Idea:
Each lemonade costs $5.

Maintain:
- five: number of $5 bills
- ten: number of $10 bills

For each customer:

1. If the customer pays $5:
   - No change is needed.
   - Store the $5 bill.

2. If the customer pays $10:
   - Give back one $5 bill.
   - If no $5 bill is available, return False.

3. If the customer pays $20:
   - We need to give back $15.
   - Prefer one $10 bill and one $5 bill.
   - Otherwise, use three $5 bills.
   - If neither option is possible, return False.

Why Greedy Works:

For a $20 bill, using one $10 and one $5
preserves more $5 bills.

$5 bills are more flexible because:
- A $10 customer always requires one $5 bill.
- A $20 customer can use either:
  - one $10 + one $5
  - three $5 bills

Therefore, we should preserve $5 bills whenever possible.

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:

            if bill == 5:
                five += 1

            elif bill == 10:
                if five == 0:
                    return False

                five -= 1
                ten += 1

            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1

                elif five >= 3:
                    five -= 3

                else:
                    return False

        return True
    
if __name__ == "__main__":
    solution = Solution()
    bills = [5, 5, 5, 10, 20]
    print(solution.lemonadeChange(bills))  # Output: True