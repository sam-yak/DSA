# Day 1 — Arrays, Strings & Hash Maps

## The Big Picture

Arrays and hash maps are the bread and butter of coding interviews. Over 60% of
Google interview problems involve arrays or hash maps in some way, even if they're
primarily testing another concept. Today is about building an unshakeable foundation.

---

## Core Concepts to Master Today

### 1. Arrays in Python

Python lists ARE dynamic arrays under the hood.

**Key operations and their time complexity:**

| Operation | Time | Notes |
|-----------|------|-------|
| `arr[i]` access | O(1) | Direct index |
| `arr.append(x)` | O(1) amortized | May resize internally |
| `arr.insert(i, x)` | O(n) | Shifts everything right |
| `arr.pop()` | O(1) | Remove from end |
| `arr.pop(i)` | O(n) | Remove from middle, shifts left |
| `x in arr` | O(n) | Linear scan |
| `arr.sort()` | O(n log n) | Timsort, stable |
| `len(arr)` | O(1) | Stored internally |
| Slicing `arr[i:j]` | O(j-i) | Creates new list |

**Python tricks you MUST know:**

```python
# Enumerate — get index AND value (never use range(len(...)) for this)
for i, val in enumerate(nums):
    print(i, val)

# List comprehension — concise array building
squares = [x*x for x in range(10)]
evens = [x for x in nums if x % 2 == 0]

# Zip — iterate two arrays together
for a, b in zip(arr1, arr2):
    pass

# Unpacking
first, *middle, last = [1, 2, 3, 4, 5]  # first=1, middle=[2,3,4], last=5

# Sorting with key
intervals.sort(key=lambda x: x[0])  # sort by first element
```

---

### 2. Hash Maps (dict) — Your Best Friend

A hash map gives you O(1) average lookup, insert, delete. It trades space for time.

**The fundamental insight:** Whenever you're doing O(n) searches inside a loop
(turning your solution into O(n²)), ask yourself: "Can I use a hash map to make
this lookup O(1)?"

**Key operations:**

| Operation | Time |
|-----------|------|
| `d[key]` access | O(1) avg |
| `d[key] = val` set | O(1) avg |
| `key in d` check | O(1) avg |
| `del d[key]` delete | O(1) avg |
| `d.get(key, default)` | O(1) avg |

**Essential Python dict patterns:**

```python
# defaultdict — auto-initializes missing keys
from collections import defaultdict
graph = defaultdict(list)     # missing key → empty list
freq = defaultdict(int)       # missing key → 0

# Counter — frequency counting in one line
from collections import Counter
freq = Counter([1, 1, 2, 3, 3, 3])  # {3: 3, 1: 2, 2: 1}
freq.most_common(2)  # [(3, 3), (1, 2)]

# dict.get() — safe access with default
count = d.get(key, 0) + 1

# Iterating
for key in d:                  # keys only
for key, val in d.items():     # both
for val in d.values():         # values only
```

---

### 3. Hash Sets — When You Only Care About Existence

```python
s = set()
s.add(5)        # O(1)
s.remove(5)     # O(1), raises KeyError if missing
s.discard(5)    # O(1), no error if missing
5 in s          # O(1) — this is the killer feature
```

**When to use set vs dict:**
- Set: "Have I seen this before?" / "Does this exist?"
- Dict: "Have I seen this before, AND what was associated with it?"

---

### 4. Strings in Python

Strings are immutable arrays of characters. This means:
- `s[i]` is O(1)
- `s + "abc"` creates a NEW string (O(n)) — never concatenate in a loop!
- Use `"".join(parts)` for building strings efficiently

**Key string operations:**

```python
s.lower(), s.upper()        # case conversion
s.isalnum()                 # alphanumeric check
s.isalpha(), s.isdigit()    # type checks
s[::-1]                     # reverse
ord('a')  # 97              # char → ASCII
chr(97)   # 'a'             # ASCII → char
```

---

## Today's Problem Set

### Problem 1: Two Sum (LC 1) — The Classic

**Why this matters:** This is literally the most asked interview question ever.
It teaches the core hash map pattern: store what you've seen, look up what you need.

**The brute force trap:** O(n²) — check every pair. NEVER do this in an interview.

**The pattern:**
For each number, I need `target - num`. Instead of scanning the array for it,
I store every number I've seen in a hash map. Then checking becomes O(1).

```
nums = [2, 7, 11, 15], target = 9

i=0: num=2, need 7, seen={} → not found → seen={2:0}
i=1: num=7, need 2, seen={2:0} → FOUND at index 0 → return [0, 1]
```

---

### Problem 2: Contains Duplicate (LC 217)

**Pattern:** Set for O(1) membership testing.
If I've seen a number before (it's in my set), there's a duplicate.

---

### Problem 3: Valid Anagram (LC 242)

**Pattern:** Frequency counting. Two strings are anagrams if they have
the same character frequencies. Use Counter or a frequency dict.

---

### Problem 4: Group Anagrams (LC 49)

**Pattern:** Hash map where the KEY is the "signature" of each group.
For anagrams, the signature is the sorted string: `sorted("eat") = "aet"`.
All anagrams produce the same sorted key.

```python
# Key insight: use tuple(sorted(word)) as the hash map key
# because lists aren't hashable, but tuples are
groups = defaultdict(list)
for word in strs:
    key = tuple(sorted(word))
    groups[key].append(word)
```

---

### Problem 5: Longest Consecutive Sequence (LC 128)

**Pattern:** Set + intelligent iteration. Don't start counting from every number —
only start from numbers that are the BEGINNING of a sequence (where num-1 is NOT
in the set).

```
nums = [100, 4, 200, 1, 3, 2]
set = {1, 2, 3, 4, 100, 200}

100: is 99 in set? No → start here → 100 (length 1)
4:   is 3 in set? Yes → skip (not a sequence start)
200: is 199 in set? No → start here → 200 (length 1)
1:   is 0 in set? No → start here → 1,2,3,4 (length 4) ← answer
3:   is 2 in set? Yes → skip
2:   is 1 in set? Yes → skip
```

This is O(n) despite the nested loops — each element is visited at most twice.

---

### Problem 6: Product of Array Except Self (LC 238)

**Pattern:** Prefix and suffix products. For each position i, the answer is
(product of everything left of i) × (product of everything right of i).

```
nums  = [1,  2,  3,  4]
left  = [1,  1,  2,  6]   ← running product from the left
right = [24, 12, 4,  1]   ← running product from the right
ans   = [24, 12, 8,  6]   ← left[i] * right[i]
```

The trick: you can compute this with a single output array and two passes,
using O(1) extra space (output array doesn't count per the problem).

---

## End of Day Checkpoint

By end of Day 1, you should be able to:
- [ ] Solve Two Sum in under 5 minutes with full explanation
- [ ] Explain when to use dict vs set and why
- [ ] Write the frequency counting pattern without looking
- [ ] Explain why Longest Consecutive Sequence is O(n), not O(n²)
- [ ] Implement prefix/suffix product in a single pass
- [ ] State time/space complexity for every solution you wrote
