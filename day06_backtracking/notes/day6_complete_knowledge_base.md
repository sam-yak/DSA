# Day 6 — Complete Knowledge Base
## DFS & Backtracking

---

## Part 1: What Is Backtracking?

Systematically explore ALL possible solutions by making choices and undoing
them when they don't work. Like navigating a maze — pick a path, if dead
end, go back and try the next.

### The Universal Template

```python
def backtrack(state, choices):
    if is_goal(state):           # reached valid solution
        result.append(state[:])  # save a COPY
        return

    for choice in choices:
        state.append(choice)     # CHOOSE
        backtrack(remaining)     # EXPLORE
        state.pop()              # UNCHOOSE (backtrack)
```

Three steps every time: **choose, explore, unchoose.**

Backtracking IS a type of DFS — you're doing DFS on a decision tree.
The pop() is what makes it backtracking specifically.

---

## Part 2: Three Variations

### Variation 1: Subsets — Save at Every Step

```
Use i + 1 (move forward only, no reuse)
Save state at every step (every partial subset is valid)

[1,2,3] → [], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]
```

### Variation 2: Permutations — Save When Complete

```
Loop through ALL elements, skip what's already used
Save only when length equals input length

[1,2,3] → [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
```

### Variation 3: Combination Sum — Reuse Allowed

```
Use i (same element can be picked again)
Save when remaining target equals 0
Stop when remaining goes negative

candidates=[2,3,7] target=7 → [2,2,3], [7]
```

---

## Part 3: Patterns Learned

### Pattern 1: Subsets (LC 78)

**Signal:** "all subsets", "power set", "all combinations"

```python
def subsets(nums):
    result = []
    def backtrack(start, current):
        result.append(current[:])            # save at EVERY step
        for i in range(start, len(nums)):
            current.append(nums[i])          # choose
            backtrack(i + 1, current)        # explore (forward only)
            current.pop()                    # unchoose
    backtrack(0, [])
    return result
# Time: O(n * 2^n)  Space: O(n)
```

Key: `i + 1` prevents reusing elements. Save before the loop
captures partial subsets including empty set.

### Pattern 2: Permutations (LC 46)

**Signal:** "all permutations", "all orderings", "all arrangements"

```python
def permute(nums):
    result = []
    def backtrack(current):
        if len(current) == len(nums):        # complete permutation
            result.append(current[:])
            return
        for num in nums:
            if num not in current:           # skip already used
                current.append(num)          # choose
                backtrack(current)           # explore
                current.pop()               # unchoose
    backtrack([])
    return result
# Time: O(n * n!)  Space: O(n)
```

Key difference from subsets: loop through ALL elements (not from start),
skip what's used. Save only when permutation is complete.

### Pattern 3: Combination Sum (LC 39)

**Signal:** "combinations that sum to target", "can reuse elements"

```python
def combination_sum(candidates, target):
    result = []
    def backtrack(start, current, remaining):
        if remaining == 0:                   # exact match
            result.append(current[:])
            return
        if remaining < 0:                    # overshot
            return
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # i not i+1
            current.pop()
    backtrack(0, [], target)
    return result
# Time: O(n^(T/M)) where T=target, M=min candidate  Space: O(T/M)
```

Key: `backtrack(i, ...)` not `i+1` because reuse is allowed.
Still use `start` to prevent duplicate combinations in different orders.

### Pattern 4: DFS on Grid (Word Search)

**Signal:** "find word in grid", "path in matrix"

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        if index == len(word):               # matched all characters
            return True
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or board[r][c] != word[index]):
            return False

        temp = board[r][c]                   # save
        board[r][c] = '#'                    # mark visited

        found = (dfs(r+1, c, index+1) or    # explore 4 directions
                 dfs(r-1, c, index+1) or
                 dfs(r, c+1, index+1) or
                 dfs(r, c-1, index+1))

        board[r][c] = temp                   # restore (backtrack)
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```

Key: mark visited by replacing with '#', restore after exploring.
Try every cell as starting point with nested for loops.

### Pattern 5: N-Queens (Constraint Backtracking)

**Signal:** "place N items with constraints", "N-Queens"

```python
def solve_n_queens(n):
    result = []
    cols = set()
    pos_diag = set()          # row + col
    neg_diag = set()          # row - col
    board = [['.' for _ in range(n)] for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row+col) in pos_diag or (row-col) in neg_diag:
                continue                      # not safe
            board[row][col] = 'Q'             # choose
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)

            backtrack(row + 1)                # explore

            board[row][col] = '.'             # unchoose
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    backtrack(0)
    return result
```

Key: place row by row. Track attacks with 3 sets (cols, positive
diagonal, negative diagonal). Positive diagonal = row+col constant.
Negative diagonal = row-col constant.

---

## Part 4: Subsets vs Permutations vs Combinations

```
                    | Subsets      | Permutations  | Combination Sum
--------------------|--------------|---------------|----------------
Order matters?      | No           | Yes           | No
Use each element    | 0 or 1 times | Exactly once  | Unlimited
Recurse with        | i + 1        | all (skip used)| i (reuse)
Save when           | Every step   | Complete only | Target reached
Loop from           | start        | 0             | start
```

---

## Part 5: Common Mistakes

1. Forgetting `current[:]` — saves reference, all entries become same list
2. Using `i + 1` when reuse is allowed (should be `i`)
3. Using `i` when reuse is NOT allowed (should be `i + 1`)
4. Looping from 0 instead of start in combinations (causes duplicates)
5. Forgetting to restore board state after DFS on grid
6. Missing base case (leads to infinite recursion)

---

## Part 6: When to Use What

```
"All subsets / power set"           → Subsets pattern (i+1, save every step)
"All permutations / arrangements"   → Permutations pattern (all, skip used)
"Combinations summing to target"    → Combination Sum (i, track remaining)
"Find word/path in grid"            → DFS on grid (4 directions, mark visited)
"Place N items with constraints"    → Constraint backtracking (check validity)
```
