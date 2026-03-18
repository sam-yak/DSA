# Day 2 — Complete Knowledge Base
## Two Pointers & Sliding Window

---

## Part 1: Two Pointers — The Core Idea

Instead of nested loops O(n²) to check pairs, use two index variables that
move intelligently, reducing it to O(n).

### Type 1: Opposite Direction

Two pointers start at opposite ends, move toward each other.

```python
left = 0
right = len(arr) - 1

while left < right:
    if some_condition:
        left += 1
    else:
        right -= 1
```

**Use when:** sorted arrays, palindrome checking, pair finding

**Why it needs sorted arrays:** In a sorted array, moving left++ always gives
a bigger value, moving right-- always gives a smaller value. This predictability
is what makes the logic work. In unsorted arrays, moving a pointer could give
you bigger OR smaller — you can't decide which way to go.

### Type 2: Same Direction (Fast/Slow)

Both pointers start at the beginning. One moves faster.
**Use when:** linked list cycle detection, finding middle element.
(We'll cover this in Day 3)

---

## Part 2: Sliding Window — The Core Idea

Maintain a "window" (a contiguous subarray/substring) defined by left and right
pointers. Expand right to explore. Shrink left when window becomes invalid.

```python
left = 0
window_state = set() or {}  # track what's in the window
best = 0

for right in range(len(s)):
    # 1. EXPAND: add s[right] to window state
    # 2. SHRINK: while window is invalid, remove s[left] and move left
    # 3. UPDATE: best = max(best, right - left + 1)

return best
```

**Window length = right - left + 1** (both endpoints included)

**Use when:** "longest/shortest subarray/substring with condition"

---

## Part 3: Patterns Learned

### Pattern 1: Two Pointers — Palindrome Check (Valid Palindrome)

**Signal:** "is this a palindrome?", "reads same forward and backward"

```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():   # skip junk from left
            left += 1
        while left < right and not s[right].isalnum():  # skip junk from right
            right -= 1
        if s[left].lower() == s[right].lower():         # compare lowercase
            left += 1
            right -= 1
        else:
            return False
    return True
# Time: O(n)  Space: O(1)
```

**Key details:**
- `.isalnum()` checks if character is letter or digit
- `.lower()` converts to lowercase for case-insensitive comparison
- Inner while loops skip non-alphanumeric characters (spaces, punctuation)
- Inner whiles need `left < right` check to prevent pointer crossing

### Pattern 2: Two Pointers — Sorted Array Pair (Two Sum II)

**Signal:** "sorted array", "find pair that sums to target"

```python
def two_sum_ii(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]    # 1-indexed
        elif total < target:
            left += 1       # need bigger sum
        else:
            right -= 1      # need smaller sum
    return []
# Time: O(n)  Space: O(1) ← better than hash map O(n) space
```

**Key insight:** O(1) space vs O(n) space with hash map. When array is sorted,
two pointers is the better approach.

### Pattern 3: Sort + Two Pointers + Skip Duplicates (3Sum)

**Signal:** "find triplets", "all unique combinations that sum to X"

```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:    # skip duplicate fixed number
            continue
        target = -nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:   # skip dup
                    left += 1
                while left < right and nums[right] == nums[right - 1]: # skip dup
                    right -= 1
                left += 1      # move past last duplicate
                right -= 1     # move past last duplicate
            elif total < target:
                left += 1
            else:
                right -= 1
    return result
# Time: O(n²)  Space: O(1) excluding output
```

**Key details:**
- Sort first so two pointers work
- O(n²) because two pointer while loop runs fully for EACH fixed number
- Skip duplicates in three places: fixed number, left pointer, right pointer
- After skipping duplicates, must move pointers one more step

### Pattern 4: Running Min/Max (Best Time to Buy/Sell Stock)

**Signal:** "maximum profit", "best time to buy and sell", "track minimum so far"

```python
def max_profit(prices):
    min_price = prices[0]
    best = 0
    for price in prices:
        min_price = min(min_price, price)     # track cheapest so far
        profit = price - min_price             # what if I sell today?
        best = max(best, profit)               # best profit so far
    return best
# Time: O(n)  Space: O(1)
```

**Key insight:** You don't need two pointers or sliding window. Just track
the minimum price seen so far and calculate profit at each step.

### Pattern 5: Sliding Window + Set (Longest Substring Without Repeating)

**Signal:** "longest substring without repeating", "all unique characters"

```python
def length_of_longest_substring(s):
    left = 0
    window = set()
    best = 0
    for right in range(len(s)):
        while s[right] in window:            # duplicate found
            window.remove(s[left])           # shrink: remove leftmost
            left += 1
        window.add(s[right])                 # expand: add current
        best = max(best, right - left + 1)   # update best
    return best
# Time: O(n)  Space: O(min(n, alphabet_size))
```

**Key details:**
- Set tracks characters currently in the window
- When duplicate found, shrink from left until duplicate is gone
- Must remove s[left] BEFORE incrementing left
- Add s[right] AFTER the while loop (after duplicates cleared)

### Pattern 6: Sliding Window + Freq Dict (Longest Repeating Char Replacement)

**Signal:** "longest substring with at most k replacements", "make all same character"

```python
def character_replacement(s, k):
    freq = {}
    left = 0
    max_freq = 0
    best = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        max_freq = max(max_freq, freq[s[right]])
        while (right - left + 1) - max_freq > k:   # need too many replacements
            freq[s[left]] -= 1                       # shrink
            left += 1
        best = max(best, right - left + 1)
    return best
# Time: O(n)  Space: O(1) — at most 26 characters
```

**Key insight:**
- Characters to replace = window_length - most_frequent_char_count
- If replacements needed > k, window is invalid → shrink
- max_freq doesn't need to be perfectly accurate when shrinking
  because a stale max_freq just prevents the window from growing,
  it never produces a wrong best answer

---

## Part 4: Two Pointers vs Hash Map

| Scenario | Hash Map | Two Pointers |
|----------|----------|--------------|
| Unsorted array | ✅ Use this | ❌ Won't work |
| Sorted array | ✅ Works (O(n) space) | ✅ Better (O(1) space) |
| Need indices | ✅ Stores indices | ✅ Has indices (left, right) |

**Rule:** If the array is sorted, think two pointers first.

---

## Part 5: Sliding Window Template Summary

```python
# FIXED WINDOW (window size = k)
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i - k]    # add right, remove left

# VARIABLE WINDOW (most common in interviews)
left = 0
state = set() or {}
best = 0
for right in range(len(s)):
    # expand: update state with s[right]
    while window_is_invalid:
        # shrink: update state, remove s[left], left += 1
    best = max(best, right - left + 1)
return best
```

---

## Part 6: Common Mistakes Made Today

1. Adding positions instead of values: `left + right` vs `nums[left] + nums[right]`
2. Using `=` (assignment) instead of `==` (comparison) in if statements
3. Forgetting to move pointers after skipping duplicates in 3Sum
4. `return False` at wrong indentation level — exits function too early
5. Missing `.lower()` in palindrome comparison
6. `max(profit)` with one argument — needs two: `max(best, profit)`
7. Resetting `max_length = 0` inside loop instead of before loop
8. Using `if` instead of `while` for shrinking window — might need multiple shrinks

---

## Part 7: When to Use What

```
"Sorted array + find pair"     → Two Pointers (opposite direction)
"Is this a palindrome?"        → Two Pointers (opposite direction)
"Find triplets that sum to X"  → Sort + Fix one + Two Pointers
"Maximum profit / running min" → Single pass tracking min/max
"Longest substring with..."    → Sliding Window (variable size)
"Subarray/substring + condition" → Sliding Window
```
