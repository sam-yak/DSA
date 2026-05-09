# Day 4 — Complete Knowledge Base
## Binary Search

---

## Part 1: The Core Idea

If data is sorted, eliminate half the search space each step. O(log n) instead of O(n).

```
Find 7 in: [1, 3, 5, 7, 9, 11, 13]

Check middle (7) → found!

Find 3 in: [1, 3, 5, 7, 9, 11, 13]

Check middle (7), 3 < 7 → search left [1, 3, 5]
Check middle (3) → found!
```

---

## Part 2: Two Types of Binary Search

### Type 1: Find Exact Match

Use when searching for a specific target. Returns the index or -1.

```python
def binary_search(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:                    # check every possibility
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1               # target is in right half
        else:
            hi = mid - 1               # target is in left half
    return -1                           # not found
```

Key details:
- `while lo <= hi` — must check when lo equals hi (single element)
- `lo = mid + 1` and `hi = mid - 1` — skip mid, already checked
- `//` for integer division (index must be whole number)
- Always compare `nums[mid]` not `mid` (value not index)

### Type 2: Find Minimum That Satisfies Condition

Use when narrowing down to the best answer. Returns the answer.

```python
def find_minimum(lo, hi):
    while lo < hi:                     # narrow to one answer
        mid = (lo + hi) // 2
        if condition(mid):
            hi = mid                   # works, try smaller (keep mid)
        else:
            lo = mid + 1               # doesn't work, skip
    return lo                           # lo == hi, the answer
```

Key details:
- `while lo < hi` — stop when one answer remains
- `hi = mid` NOT `mid - 1` — mid could be the answer
- `lo = mid + 1` — mid doesn't work, safe to skip
- Return `lo` or `hi` (they're equal when loop ends)

---

## Part 3: Patterns Learned

### Pattern 1: Standard Binary Search (LC 704)

**Signal:** "sorted array, find target"

```python
def search(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
# Time: O(log n)  Space: O(1)
```

### Pattern 2: Search Insert Position (LC 35)

**Signal:** "find target or where it would be inserted"

Same as standard binary search, but return `lo` instead of `-1`:

```python
def search_insert(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo                    # insertion point
# Time: O(log n)  Space: O(1)
```

When loop ends, `lo` is exactly where target should be inserted.

### Pattern 3: Search in Rotated Sorted Array (LC 33)

**Signal:** "rotated sorted array, find target"

At any mid, one half is always sorted. Check which half, then decide:

```python
def search(nums, target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:            # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1                  # target in sorted left
            else:
                lo = mid + 1                  # target in right
        else:                                 # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1                  # target in sorted right
            else:
                hi = mid - 1                  # target in left
    return -1
# Time: O(log n)  Space: O(1)
```

### Pattern 4: Find Min in Rotated Array (LC 153)

**Signal:** "rotated sorted array, find minimum"

Compare nums[mid] with nums[hi] to find which half has the drop:

```python
def find_min(nums):
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= nums[hi]:    # right half sorted, min is left
            hi = mid                  # keep mid (could be the min)
        else:                         # drop is in right half
            lo = mid + 1              # min is after mid
    return nums[lo]
# Time: O(log n)  Space: O(1)
```

Key: compare with nums[hi] not nums[lo]. Comparing with nums[lo] fails
when array is not rotated (pivot at 0).

### Pattern 5: Search a 2D Matrix (LC 74)

**Signal:** "sorted matrix, find target"

Treat matrix as one flat sorted array. Convert flat index to row/col:

```python
def search_matrix(matrix, target):
    m = len(matrix)        # rows
    n = len(matrix[0])     # columns
    lo = 0
    hi = m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        row = mid // n              # which row
        col = mid % n               # which column
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
# Time: O(log(m*n))  Space: O(1)
```

Why `mid // n` and `mid % n`:
- `//` counts how many complete rows have passed (row number)
- `%` gives remainder within current row (column number)
- Math naturally produces 0-based positions

### Pattern 6: Binary Search on Answer Space (Koko Eating Bananas)

**Signal:** "find minimum speed/capacity/value that satisfies condition"

Don't search through the data — search through possible answers:

```python
import math

def min_eating_speed(piles, h):
    lo = 1                              # minimum possible answer
    hi = max(piles)                     # maximum possible answer
    while lo < hi:
        mid = (lo + hi) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:                   # can finish in time
            hi = mid                     # try slower (keep mid)
        else:                            # too slow
            lo = mid + 1                 # need faster
    return lo
# Time: O(n * log(max(piles)))  Space: O(1)
```

The data (piles) doesn't need to be sorted. The answer space (1 to max)
is naturally sorted. hi = mid keeps the answer, lo = mid + 1 skips failures.

---

## Part 4: Key Differences Cheat Sheet

```
                    | Find Exact Match     | Find Min Satisfying
--------------------|----------------------|--------------------
While condition     | lo <= hi             | lo < hi
When found/valid    | return mid           | hi = mid
When not found      | lo = mid+1/hi=mid-1  | lo = mid + 1
After loop          | return -1            | return lo (or hi)
hi update           | hi = mid - 1         | hi = mid
```

---

## Part 5: Math Operators

```python
7 // 4    # → 1 (integer division — how many times 4 fits into 7)
7 % 4     # → 3 (remainder — what's left after division)
7 / 4     # → 1.75 (float division — can't use as index)

# Use // for indices (always need whole numbers)
# Use % for cycling/wrapping (column positions, circular arrays)

import math
math.ceil(7/4)    # → 2 (round UP — ceiling)
math.floor(7/4)   # → 1 (round DOWN — same as //)
```

---

## Part 6: Common Mistakes Made Today

1. Comparing `mid` instead of `nums[mid]` (index vs value)
2. Using `high` instead of `hi` (variable name mismatch)
3. Using `/` instead of `//` (float vs integer division)
4. Swapping lo and hi updates (lo = mid-1 vs hi = mid-1)
5. Using `lo <= hi` when should be `lo < hi` (or vice versa)
6. Using `hi = mid - 1` when mid could be the answer (should be hi = mid)
7. `Return` instead of `return` (case sensitivity)

---

## Part 7: When to Use What

```
"Find target in sorted array"           → Standard binary search (lo <= hi)
"Find insert position"                  → Standard + return lo
"Sorted but rotated"                    → Check which half is sorted
"Find min in rotated"                   → Compare mid with hi (lo < hi)
"Sorted 2D matrix"                      → Flatten with // and %
"Find minimum X that satisfies..."      → Binary search on answer space (lo < hi)
"Find maximum X that satisfies..."      → Binary search on answer space (lo < hi)
```
