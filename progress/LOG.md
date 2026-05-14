# 📓 Daily Progress Log

Track what clicked, what didn't, and what needs revisiting.

---

## Day 1 — Arrays & Hash Maps
**Date:** March 13, 2026
**Hours spent:** ~6-7 hrs
**Problems attempted:** 6/6
**Concepts that clicked:**
- Hash map for O(1) lookups (Two Sum pattern)
- Set for existence checking (Contains Duplicate)
- Frequency counting with defaultdict(int) and Counter
- Grouping with defaultdict(list) + signature keys
- Why string += in a loop is O(n²) and how to fix with join()
- Difference between data types and data structures
- Mutable vs immutable and why it matters for dict keys

**Concepts that need review:**
- Prefix/suffix two-pass technique (Product Except Self)
- Set + smart start detection (Longest Consecutive Sequence)
- range() backwards: range(n-1, -1, -1)

**Key mistakes made:**
- Used If/Return instead of if/return (case sensitivity)
- Used curly braces {} instead of square brackets [] for dict access
- Used [] (list) instead of {} (dict) for frequency counting
- Forgot to store seen[num] = i in Two Sum
- Used = instead of *= in Product Except Self pass 2
- Forgot to import defaultdict before using it
- Used if/else with defaultdict (defeats the purpose)

**Confidence level (1-10):** 6

---

## Day 2 — Two Pointers & Sliding Window
**Date:** March 14, 2026
**Hours spent:** ~6-7 hrs
**Problems attempted:** 6/6
**Concepts that clicked:**
- Two pointers opposite direction on sorted arrays
- Why two pointers only works on sorted arrays (predictable direction)
- Two pointers gives O(1) space vs hash map O(n) space
- Sliding window with set for unique substring
- Sliding window with freq dict for character replacement
- Window length = right - left + 1
- Running min for stock profit problem

**Concepts that need review:**
- 3Sum duplicate skipping logic (three places to skip)
- Sliding window + freq dict (Longest Repeating Character Replacement)
- Why stale max_freq doesn't produce wrong answers

**Key mistakes made:**
- Added positions instead of values (left + right vs nums[left] + nums[right])
- Used = instead of == in if statement
- Forgot .lower() in palindrome comparison
- max() needs two arguments not one
- Put max_length = 0 inside loop instead of before loop
- Used if instead of while for shrinking window

**Confidence level (1-10):** 6

---

## Day 3 — Stacks, Queues & Linked Lists
**Date:** March 15, 2026
**Hours spent:** ~6-7 hrs
**Problems attempted:** 6/6
**Concepts that clicked:**
- Stack as LIFO using Python list (append/pop/[-1])
- Stack for bracket matching pattern
- Classes, objects, __init__, self
- Linked list node structure (val + next)
- Traversing linked lists with while current
- Reverse linked list four-line swap (prev/curr/next)
- Dummy node pattern for building linked lists
- Fast/slow pointers for cycle detection and finding middle
- Attaching remaining chain attaches ALL nodes automatically

**Concepts that need review:**
- Min Stack (two parallel stacks concept)
- Reorder List (combining find mid + reverse + merge)
- Merge two sorted lists (dummy node flow)

**Key mistakes made:**
- Used prev = 0 instead of prev = None
- Returned curr instead of prev after reversing
- Forgot self. inside class methods
- Used elif without a condition
- Used str as variable name

**Confidence level (1-10):** 6

---

## Day 4 — Binary Search
**Date:** March 16, 2026
**Hours spent:** ~6 hrs
**Problems attempted:** 6/6
**Concepts that clicked:**
- Standard binary search template (lo, hi, mid)
- Why lo <= hi vs lo < hi (exact match vs narrowing)
- Why hi = mid vs hi = mid - 1 (mid could be answer vs already checked)
- Rotated array: one half is always sorted
- 2D matrix flattening with // and % (math naturally gives 0-based positions)
- Binary search on answer space (Koko Bananas)
- Compare with nums[hi] not nums[lo] for rotated min

**Concepts that need review:**
- Search in Rotated Array (which half is sorted logic)
- Binary search on answer space pattern
- When to use lo <= hi vs lo < hi

**Key mistakes made:**
- Compared mid (index) instead of nums[mid] (value) — multiple times
- Used high instead of hi (variable name typo)
- Swapped lo and hi updates in elif/else
- Used Return instead of return
- Used <= instead of < in elif after equality check

**Confidence level (1-10):** 7

---

## Day 5 — Trees (BT & BST)
**Date:** March 17, 2026
**Hours spent:** ~6 hrs
**Problems attempted:** 6/6
**Concepts that clicked:**
- TreeNode structure (val, left, right)
- Base case: if not node always needed in recursion
- DFS recursion pattern for trees
- BFS with queue and level_size for level order
- Helper function with range bounds for BST validation
- BST property for LCA (both left/both right/split)
- True bubbles up only if all checks pass through `and`
- Always compare .val not node objects

**Concepts that need review:**
- None — best day yet, all 6 clean!

**Key mistakes made:**
- Swapped root.left, root.right = root.left, root.right (no actual swap)
- Returned None instead of 0 in max_depth
- Forgot .val on comparisons multiple times
- Put function inside class accidentally

**Confidence level (1-10):** 8

---

## Day 6 — DFS & Backtracking
**Date:** March 18, 2026
**Hours spent:** ~6 hrs
**Problems attempted:** 5/5
**Concepts that clicked:**
- Backtracking template: choose, explore, unchoose
- Subsets: i+1 (forward only), save at every step
- Permutations: loop all, skip used, save when complete
- Combination Sum: i (reuse), track remaining target
- DFS on grid: mark visited with '#', restore after
- N-Queens: track cols and diagonals with sets
- Backtracking IS DFS on a decision tree

**Concepts that need review:**
- N-Queens diagonal tracking (row+col, row-col)

**Key mistakes made:**
- Minor syntax issues only — logic was strong today

**Confidence level (1-10):** 8

---

## Day 7 — BFS & Graph Traversal
**Date:**
**Hours spent:**
**Problems attempted:**
**Concepts that clicked:**
**Concepts that need review:**
**Key mistakes made:**
**Confidence level (1-10):**

---

## Day 8 — Advanced Graphs
**Date:**
**Hours spent:**
**Problems attempted:**
**Concepts that clicked:**
**Concepts that need review:**
**Key mistakes made:**
**Confidence level (1-10):**

---

## Day 9 — DP (1D)
**Date:**
**Hours spent:**
**Problems attempted:**
**Concepts that clicked:**
**Concepts that need review:**
**Key mistakes made:**
**Confidence level (1-10):**

---

## Day 10 — DP (2D & Advanced)
**Date:**
**Hours spent:**
**Problems attempted:**
**Concepts that clicked:**
**Concepts that need review:**
**Key mistakes made:**
**Confidence level (1-10):**

---

## Day 11 — Heaps & Priority Queues
**Date:**
**Hours spent:**
**Problems attempted:**
**Concepts that clicked:**
**Concepts that need review:**
**Key mistakes made:**
**Confidence level (1-10):**

---

## Day 12 — Intervals & Greedy
**Date:**
**Hours spent:**
**Problems attempted:**
**Concepts that clicked:**
**Concepts that need review:**
**Key mistakes made:**
**Confidence level (1-10):**

---

## Day 13 — Tries & Advanced Strings
**Date:**
**Hours spent:**
**Problems attempted:**
**Concepts that clicked:**
**Concepts that need review:**
**Key mistakes made:**
**Confidence level (1-10):**

---

## Day 14-17 — Google Mix (Integration)
**Date range:**
**Hours spent:**
**Total problems attempted:**
**Hardest problem solved:**
**Patterns I recognized quickly:**
**Patterns I'm still slow on:**
**Confidence level (1-10):**

---

## Day 18 — Weakness Day
**Date:**
**Weak areas targeted:**
**Problems re-solved:**
**Improvement noticed?:**

---

## Day 19-20 — Mock Interviews
**Mock 1 result:**
**Mock 2 result:**
**Communication score (1-10):**
**Biggest interview weakness:**
**Behavioral stories ready? (Y/N):**

---

## Day 21 — Final Review
**Speed run problems solved:**
**Average solve time:**
**Overall confidence (1-10):**
**Ready for Google? (Y/N):**
