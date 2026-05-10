# Day 5 — Complete Knowledge Base
## Trees (Binary Trees & BST)

---

## Part 1: Tree Basics

### What Is a Tree?

An upside-down hierarchical structure with nodes connected by edges.

```
        1          ← root (top node, no parent)
       / \
      2   3        ← children of 1
     / \   \
    4   5   6      ← leaf nodes (no children)
```

### Node Structure

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # the data
        self.left = left      # pointer to left child
        self.right = right    # pointer to right child
```

Like a linked list node but with TWO pointers instead of one.

### Binary Search Tree (BST)

For every node:
- Everything in left subtree is SMALLER
- Everything in right subtree is BIGGER

```
        8
       / \
      3   10      3 < 8 ✅   10 > 8 ✅
     / \    \
    1   6    14   1 < 3 ✅   6 > 3 ✅   14 > 10 ✅
```

---

## Part 2: Tree Traversals

### DFS (Depth-First Search) — Go deep before wide

```python
def dfs(node):
    if not node:           # base case — always needed
        return
    # do something with node.val
    dfs(node.left)         # recurse left
    dfs(node.right)        # recurse right
```

### BFS (Breadth-First Search) — Go level by level

```python
from collections import deque

def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        # do something with node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## Part 3: The Universal Base Case

Every recursive tree function needs this:

```python
if not node:
    return ____    # None, True, False, 0 — depends on the problem
```

This stops the recursion when you hit past a leaf node. Without it,
you'd try to access None.left and crash.

What to return:
- `return None` → when building/modifying a tree (invert, delete)
- `return True` → when validating (same tree, valid BST)
- `return 0` → when counting (max depth)
- `return []` → when collecting (level order)

---

## Part 4: Patterns Learned

### Pattern 1: Swap + Recurse (Invert Binary Tree)

**Signal:** "mirror", "invert", "flip"

```python
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left    # swap
    invert_tree(root.left)                             # recurse
    invert_tree(root.right)
    return root
# Time: O(n)  Space: O(h) where h = height (recursion stack)
```

### Pattern 2: Recursive Depth (Max Depth)

**Signal:** "depth", "height", "how deep"

```python
def max_depth(root):
    if not root:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return 1 + max(left, right)
# Time: O(n)  Space: O(h)
```

Pattern: depth = 1 (myself) + max(left depth, right depth)

### Pattern 3: Parallel Recursion (Same Tree)

**Signal:** "same tree", "identical", "symmetric"

```python
def is_same_tree(p, q):
    if not p and not q:        # both empty
        return True
    if not p or not q:          # one empty, one not
        return False
    if p.val != q.val:          # values differ
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
# Time: O(n)  Space: O(h)
```

The True only bubbles up if EVERY node passes all checks.
One False anywhere kills the whole chain through the `and`.

### Pattern 4: BFS Level Order (Level Order Traversal)

**Signal:** "level by level", "breadth first", "each level"

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        level_size = len(queue)              # how many nodes at this level
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)           # append VALUE not node
            if node.left:
                queue.append(node.left)      # append NODE not value
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
# Time: O(n)  Space: O(n)
```

Key: level_size = len(queue) captures how many nodes are at the
current level BEFORE we start adding children from the next level.

### Pattern 5: Range Validation (Validate BST)

**Signal:** "valid BST", "validate binary search tree"

```python
def is_valid_bst(root):
    def helper(node, low, high):
        if not node:
            return True
        if low >= node.val or node.val >= high:
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    return helper(root, float('-inf'), float('inf'))
# Time: O(n)  Space: O(h)
```

Key insights:
- Helper function adds low/high parameters that the main function doesn't need
- Start with -inf and inf (no bounds initially)
- Going left: current node becomes upper bound (high)
- Going right: current node becomes lower bound (low)
- float('-inf') and float('inf') — every number is between these

### Pattern 6: BST Property Exploitation (LCA of BST)

**Signal:** "lowest common ancestor", "LCA", in a BST

```python
def lowest_common_ancestor(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    return root
# Time: O(h)  Space: O(h)
```

Three cases:
- Both smaller → go left
- Both bigger → go right
- They split (or one equals root) → root is the answer

Always compare .val on BOTH sides: p.val < root.val, not p < root

---

## Part 5: DFS vs BFS — When to Use Which

```
DFS (recursion):
- Max depth, validate BST, same tree, invert
- When you need to process subtrees before combining results
- When the answer depends on going all the way to leaves first

BFS (queue):
- Level order traversal
- Shortest path in unweighted graph
- When you need to process level by level
- When you need nearest/closest to root
```

---

## Part 6: Common Mistakes Made Today

1. Swapping same values: root.left, root.right = root.left, root.right (no swap)
2. Returning None instead of 0 in max_depth (crashes on 1 + max(None, None))
3. Putting function inside class when it should be standalone
4. Appending node instead of node.val to result lists
5. Appending node.val instead of node to queue
6. Comparing nodes instead of values: p < root vs p.val < root.val
7. Missing .val on one side of comparison
8. Changing p and q in recursive calls (only root should move in LCA)

---

## Part 7: When to Use What

```
"Invert/mirror/flip tree"         → Swap + recurse both sides
"Depth/height of tree"            → 1 + max(left, right)
"Are two trees identical?"        → Compare values + recurse with and
"Level by level processing"       → BFS with queue + level_size
"Is it a valid BST?"              → Helper with low/high range
"Find common ancestor in BST"    → Use BST property to go left/right
```
