Four Templates

1) No Duplicate
LeetCode 3: 
longest-substrin-without-repeating.py

Pattern: Longest Substring Without Repeating Characters

Idea:
Maintain a window with no duplicate elements.

while duplicate:
    shrink

2) At Most K
LeetCode 1004:
max-consecutive-ones.py
LeetCode 904:
fruit-into-baskets.py

Pattern: Longest Valid Window

Idea:
Maintain a window satisfying at most K.

while invalid:
    shrink

3) Character Frequency
LeetCode 424:
longest-repeating-characters.py

Pattern: Replace Characters

Idea:

window_length - max_frequency

is the number of characters to replace.

while window_length - max_frequency > k:
    shrink

4) Exactly K Distinct
LeetCode 930:
binary-subarrays-with-sum.py
LeetCode 1428:
count-number-of-nice-subarray.py
LeetCode 992:
subarrays-with-k-interger.py

Pattern: Exactly(K) = AtMost(K) − AtMost(K−1)
Convert an Exactly K problem into two At Most K problems.

5) At Least Condition
LeetCode 1358:
substrings-of-all-three-character.py

Pattern: Count Valid Subarrays

Idea:

Maintain a window satisfying at least a condition.
Once the window becomes valid,
all longer windows ending after the current position are also valid.

while valid:
    answer += n - right
    shrink

6) Fixed Size Sliding Window
LeetCode 1423:
max-points-to-obtain.py

Pattern: Fixed Window / Replace Ends