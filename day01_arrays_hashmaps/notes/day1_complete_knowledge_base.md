# Day 1 — Complete Knowledge Base
## Everything We Learned: Arrays, Strings, Hash Maps & Python Fundamentals

---

## Part 1: Data Types vs Data Structures

### Data Types (hold a single value)

```python
# Integer — whole numbers
x = 42
x = -7
x = 0
type(42)    # → <class 'int'>

# Float — decimal numbers
x = 3.14
x = -0.5
type(3.14)  # → <class 'float'>

# Boolean — True or False (always capitalized)
x = True
x = False
type(True)  # → <class 'bool'>

# String — text, always in quotes
x = "hello"
x = 'hello'       # single or double quotes both work
x = "a"            # single character is still a string
x = ""             # empty string
x = "12345"        # digits in quotes = string, NOT a number
type("hello")      # → <class 'str'>

# NoneType — represents "nothing"
x = None
type(None)  # → <class 'NoneType'>
```

### Data Structures (containers that hold and organize multiple values)

```python
# List — ordered, mutable, allows duplicates
arr = [1, 2, 3, 2]
arr = [1, "hello", True, [2, 3]]    # can hold mixed types
type([])    # → <class 'list'>

# Tuple — ordered, immutable, allows duplicates
t = (1, 2, 3)
# t[0] = 99  ← CRASH, can't modify
type(())    # → <class 'tuple'>

# Set — unordered, mutable, NO duplicates
s = {1, 2, 3}
s = set([1, 2, 2, 3])    # → {1, 2, 3} duplicates auto-removed
type(set()) # → <class 'set'>

# Dict (Hash Map) — key-value pairs, unordered
d = {"a": 1, "b": 2}
type({})    # → <class 'dict'>
```

### Key Differences

```
             | Ordered? | Mutable? | Duplicates? | Access     | Lookup Speed
-------------|----------|----------|-------------|------------|-------------
String       | Yes      | NO       | Yes         | s[i]       | O(1) index, O(n) search
List         | Yes      | Yes      | Yes         | arr[i]     | O(1) index, O(n) search
Tuple        | Yes      | NO       | Yes         | t[i]       | O(1) index, O(n) search
Set          | No       | Yes      | NO          | —          | O(1) search
Dict         | No       | Yes      | NO (keys)   | d[key]     | O(1) search
```

### Mutable vs Immutable — Why It Matters

```python
# MUTABLE — can be changed after creation
arr = [1, 2, 3]
arr[0] = 99        # ✅ arr = [99, 2, 3]

s = {1, 2}
s.add(3)           # ✅ s = {1, 2, 3}

d = {"a": 1}
d["b"] = 2         # ✅ d = {"a": 1, "b": 2}

# IMMUTABLE — cannot be changed after creation
s = "hello"
s[0] = "H"         # ❌ CRASH

t = (1, 2, 3)
t[0] = 99          # ❌ CRASH

# Why does this matter?
# 1. Dict keys MUST be immutable (that's why we use tuple(sorted(s)) not list)
# 2. String += in a loop is O(n²) because it creates a new string every time
```

---

## Part 2: The Python Arsenal

### List Operations

```python
arr = []

# Adding
arr.append(x)           # add to end             O(1)
arr.insert(i, x)        # add at position i      O(n) — shifts everything

# Removing
arr.pop()               # remove from end        O(1)
arr.pop(i)              # remove from position i O(n) — shifts everything

# Accessing
arr[i]                  # access by index        O(1)
arr[-1]                 # last element           O(1)
arr[1:3]                # slice (new list)       O(k) where k = slice size

# Searching
x in arr                # check existence        O(n) SLOW
arr.index(x)            # find position          O(n)

# Other
len(arr)                # size                   O(1)
arr.sort()              # sort in place          O(n log n)
sorted(arr)             # return new sorted list O(n log n)
arr.reverse()           # reverse in place       O(n)

# Creating
arr = [0] * 5           # → [0, 0, 0, 0, 0]
arr = [1] * n           # → n ones
arr = [x*x for x in range(5)]  # → [0, 1, 4, 9, 16]  (list comprehension)
```

### Set Operations

```python
s = set()

s.add(x)                # add element            O(1)
s.discard(x)            # remove (no error)      O(1)
s.remove(x)             # remove (KeyError)      O(1)
x in s                  # check existence        O(1) FAST ← killer feature
len(s)                  # size                   O(1)

# Creating
s = set()               # empty set
s = {1, 2, 3}           # with values
s = set([1, 2, 2, 3])   # from list, removes duplicates → {1, 2, 3}
```

### Dict Operations

```python
d = {}

d[key] = value          # set                    O(1)
d[key]                  # get (KeyError if missing)  O(1)
d.get(key, default)     # safe get               O(1)
key in d                # check key exists       O(1)
del d[key]              # delete                 O(1)
len(d)                  # size                   O(1)

# Iterating
for key in d:                  # keys only
for key, val in d.items():     # both
for val in d.values():         # values only

# Getting all values as a list
list(d.values())        # → [val1, val2, val3]
```

### defaultdict — Auto-Creating Missing Keys

```python
from collections import defaultdict

# PROBLEM: regular dict crashes on missing keys
freq = {}
freq['a'] += 1          # ❌ CRASH — 'a' doesn't exist yet

# SOLUTION: defaultdict auto-creates with a default value
freq = defaultdict(int)   # missing key → int() → 0
freq['a'] += 1            # ✅ auto-creates freq['a'] = 0, then adds 1

groups = defaultdict(list) # missing key → list() → []
groups['key'].append('x')  # ✅ auto-creates groups['key'] = [], then appends

# The argument is a FUNCTION that returns the default:
# int()  → 0
# list() → []
# str()  → ""
```

### Counter — Frequency Counting in One Line

```python
from collections import Counter

freq = Counter("anagram")     # → {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
freq = Counter([1, 1, 2, 3])  # → {1: 2, 2: 1, 3: 1}

# Counters can be compared directly
Counter("abc") == Counter("bca")  # → True (same frequencies)
```

### Deque — Double-Ended Queue

```python
from collections import deque

q = deque()
q.append(x)             # add to right           O(1)
q.appendleft(x)         # add to left            O(1)
q.pop()                 # remove from right      O(1)
q.popleft()             # remove from left       O(1)
```

### Heap — Always Gives You the Smallest

```python
import heapq

heap = []
heapq.heappush(heap, x)    # add                 O(log n)
heapq.heappop(heap)         # remove smallest     O(log n)
heap[0]                     # peek at smallest    O(1)
```

---

## Part 3: String Rules

### Strings Are Immutable Arrays of Characters

```python
s = "hello"
s[0]            # → 'h'          O(1) access
len(s)          # → 5            O(1)
s[0] = "H"      # ❌ CRASH — strings cannot be modified
```

### Key String Operations

```python
s.lower()           # → "hello"
s.upper()           # → "HELLO"
s.isalnum()         # True if all alphanumeric
s.isalpha()         # True if all letters
s.isdigit()         # True if all digits
s[::-1]             # → "olleh" (reverse)
ord('a')            # → 97 (character to ASCII number)
chr(97)             # → 'a' (ASCII number to character)
```

### NEVER Concatenate Strings in a Loop

```python
# ❌ BAD — O(n²) because strings are immutable
# Each += creates a brand new string by copying everything
s = ""
for char in chars:
    s += char       # copies 1 char, then 2, then 3... = O(n²)

# ✅ GOOD — O(n) using list + join
# Lists are mutable, append is O(1)
parts = []
for char in chars:
    parts.append(char)    # O(1) each time
s = "".join(parts)        # one O(n) pass at the end
```

### Sorting Strings

```python
sorted("eat")           # → ['a', 'e', 't']     returns a LIST
tuple(sorted("eat"))    # → ('a', 'e', 't')     tuple can be a dict key
# We use this as a "signature" for anagram grouping
```

---

## Part 4: Python Syntax Rules

### Everything Is Lowercase

```python
def    # ✅ not Def
for    # ✅ not For
if     # ✅ not If
else   # ✅ not Else
while  # ✅ not While
return # ✅ not Return
in     # ✅ not In
not    # ✅ not Not

# EXCEPTIONS — these ARE capitalized
True
False
None
```

### Colons Are Required

```python
# Every if, else, elif, for, while, def ends with :
def my_function():       # ← colon
for i in range(n):       # ← colon
if x > 5:               # ← colon
else:                    # ← colon
while x > 0:             # ← colon
```

### Dict Access Uses Square Brackets

```python
freq = {}
freq{char}    # ❌ WRONG — curly braces are only for creating dicts
freq[char]    # ✅ CORRECT — square brackets for accessing

# Curly braces = creating:  freq = {}  or  freq = {"a": 1}
# Square brackets = accessing:  freq["a"]  or  freq[char]
```

### Functions Return, They Don't Print

```python
# ❌ WRONG
def two_sum(nums, target):
    print [0, 1]

# ✅ CORRECT
def two_sum(nums, target):
    return [0, 1]
```

### Parentheses vs Square Brackets

```python
# Function calls use PARENTHESES
len(arr)                # ✅
list(d.values())        # ✅
groups[sig].append(s)   # ✅ append is a function call

# Indexing uses SQUARE BRACKETS
arr[0]                  # ✅
d["key"]                # ✅
groups[sig]             # ✅

# WRONG — mixing them up
len[arr]                # ❌ len is a function, use ()
list[d.values()]        # ❌ list is a function, use ()
groups[sig].append[s]   # ❌ append is a function, use ()
```

### Variable Naming

```python
# ✅ GOOD — snake_case, descriptive
num_set = set(nums)
left_product = 1
freq_t = {}
best = 0

# ❌ BAD — shadows built-in functions
list = [1, 2]      # breaks list()
set = {1, 2}       # breaks set()
len = 5            # breaks len()
max = 10           # breaks max()
min = 3            # breaks min()
sum = 0            # breaks sum()
```

---

## Part 5: The range() Function

```python
# 1 argument: range(stop) — starts at 0
range(5)              # → 0, 1, 2, 3, 4

# 2 arguments: range(start, stop)
range(2, 6)           # → 2, 3, 4, 5

# 3 arguments: range(start, stop, step)
range(0, 10, 2)       # → 0, 2, 4, 6, 8
range(3, -1, -1)      # → 3, 2, 1, 0 (counting backwards)

# CRITICAL: stop is ALWAYS excluded
range(5)              # includes 0,1,2,3,4 — NOT 5

# When to use range vs direct loop
for num in nums:              # when you need ELEMENTS
for i, num in enumerate(nums): # when you need BOTH index and element
for i in range(n):             # when you need POSITIONS (especially for modifying arrays)
for i in range(n-1, -1, -1):  # when you need to go BACKWARDS
```

---

## Part 6: Complexity Cheat Sheet

### Time Complexity

```
O(1)        — constant, instant (hash map lookup, array access)
O(log n)    — halving each step (binary search)
O(n)        — one pass through data (single for loop)
O(n log n)  — sorting
O(n²)       — nested loops (loop inside a loop)
O(2^n)      — exponential (brute force subsets)
O(n!)       — factorial (brute force permutations)
```

### How to Identify Complexity

```python
# O(n) — single loop
for i in range(n):
    # O(1) work

# O(n²) — nested loops (loop INSIDE a loop)
for i in range(n):
    for j in range(n):
        # O(1) work

# O(n) — two SEPARATE loops (NOT nested)
for i in range(n):      # O(n)
    pass
for i in range(n):      # O(n)
    pass
# Total: O(n) + O(n) = O(2n) = O(n)

# O(n) — loop with O(1) hash operations
for num in nums:            # O(n) iterations
    if num in my_set:       # O(1) per lookup
        pass
```

### Space Complexity Rules

```python
# O(1) — fixed number of variables
left = 0
right = n - 1
total = 0

# O(n) — data structure grows with input
seen = set()               # could hold up to n elements
freq = {}                  # could hold up to n keys
answer = [0] * n           # n-size array

# Rule: if your data structure grows with input size → O(n) space
```

---

## Part 7: Patterns Learned Today

### Pattern 1: Hash Map Complement Lookup (Two Sum)

**Signal:** "find two numbers that add to target"
**Approach:** For each number, check if complement (target - num) exists in hash map

```python
def two_sum(nums, target):
    seen = {}                           # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i                   # store AFTER checking
    return []
# Time: O(n)  Space: O(n)
```

### Pattern 2: Set for Existence Check (Contains Duplicate)

**Signal:** "does X exist?", "have I seen this before?"
**Approach:** Add to set, check membership before adding

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
# Time: O(n)  Space: O(n)
```

### Pattern 3: Frequency Counting (Valid Anagram)

**Signal:** "count occurrences", "same frequency", "anagram"
**Approach:** Count with dict/defaultdict/Counter, compare counts

```python
# Method 1: if/else with regular dict
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Method 2: .get() shorthand
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

# Method 3: defaultdict (no checking needed)
from collections import defaultdict
freq = defaultdict(int)
for char in s:
    freq[char] += 1

# Method 4: Counter (one line)
from collections import Counter
freq = Counter(s)
```

### Pattern 4: Grouping by Signature (Group Anagrams)

**Signal:** "group items by some shared property"
**Approach:** Create signature for each item, use as dict key, collect items in lists

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        sig = tuple(sorted(s))      # signature: sorted characters
        groups[sig].append(s)        # group by signature
    return list(groups.values())
# Time: O(n * k log k)  Space: O(n * k)
```

### Pattern 5: Set + Smart Start Detection (Longest Consecutive Sequence)

**Signal:** "longest consecutive", "sequence", must be O(n)
**Approach:** Put everything in a set, only count from sequence starts (num-1 not in set)

```python
def longest_consecutive(nums):
    num_set = set(nums)
    best = 0
    for num in num_set:
        if num - 1 not in num_set:      # sequence START
            length = 1
            while num + length in num_set:
                length += 1
            best = max(best, length)
    return best
# Time: O(n)  Space: O(n)
```

### Pattern 6: Prefix/Suffix Two-Pass (Product of Array Except Self)

**Signal:** "product/sum of everything except current", "without division"
**Approach:** Pass 1 builds left products, Pass 2 multiplies right products in

```python
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    left_product = 1
    for i in range(n):
        answer[i] = left_product        # store left product
        left_product *= nums[i]         # update running product

    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product      # MULTIPLY (not assign) right product
        right_product *= nums[i]

    return answer
# Time: O(n)  Space: O(1) extra (output doesn't count)
```

---

## Part 8: Common Mistakes Made Today

1. **Using `If`/`Return` instead of `if`/`return`** — Python keywords are always lowercase
2. **Using `freq{}` instead of `freq[]`** — curly braces create, square brackets access
3. **Using `[]` instead of `{}`** — `freq = []` is a list, `freq = {}` is a dict
4. **Forgetting `seen[num] = i`** in Two Sum — dict stays empty, nothing works
5. **Using `.append[s]` instead of `.append(s)`** — function calls use parentheses
6. **Using `=` instead of `*=`** in Product Except Self — overwrites left pass progress
7. **Forgetting `from collections import defaultdict`** — must import before using
8. **Using if/else with defaultdict** — defeats the purpose, just increment directly

---

## Part 9: When to Use What (Decision Guide)

```
"Do I need O(1) lookup?"
  ├── "Just existence check?" → SET
  └── "Need associated value?" → DICT

"Do I need to count things?"
  ├── "Quick and clean?" → Counter
  ├── "Need custom logic?" → defaultdict(int)
  └── "Want to understand internals?" → dict with if/else

"Do I need to group things?"
  └── "By some shared property?" → defaultdict(list) with signature as key

"Do I need to build a string?"
  └── "In a loop?" → list + "".join() (NEVER += in a loop)

"Do I need to go backwards through an array?"
  └── range(n-1, -1, -1)

"= or *= ?"
  ├── "Fresh assignment?" → =
  └── "Combine with existing value?" → *=  (or +=)
```
