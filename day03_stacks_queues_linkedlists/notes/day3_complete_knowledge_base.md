# Day 3 — Complete Knowledge Base
## Stacks, Queues & Linked Lists

---

## Part 1: Stack

A stack is a **Last In, First Out (LIFO)** data structure. Like a stack of plates —
you add and remove from the top only.

### Stack in Python (just a list)

```python
stack = []

# PUSH — add to top
stack.append(5)       # stack = [5]
stack.append(3)       # stack = [5, 3]
stack.append(8)       # stack = [5, 3, 8]
                      #                ↑ top

# PEEK — look at top without removing
stack[-1]             # → 8

# POP — remove from top and return it
stack.pop()           # → 8, stack = [5, 3]

# CHECK IF EMPTY
not stack             # True if empty
len(stack) == 0       # same thing

# SIZE
len(stack)            # → 2
```

### When to Use a Stack

- Matching brackets/parentheses
- Undo/redo operations
- Tracking history
- Next greater/smaller element
- Processing things in reverse order

---

## Part 2: Queue

A queue is **First In, First Out (FIFO)**. Like a line at a store.

```python
from collections import deque

q = deque()

q.append(1)       # add to right → [1]
q.append(2)       # add to right → [1, 2]
q.append(3)       # add to right → [1, 2, 3]
q.popleft()       # remove from left → returns 1, q = [2, 3]
q.popleft()       # remove from left → returns 2, q = [3]
```

We'll use queues heavily in Day 7 (BFS).

---

## Part 3: Linked List

A chain of nodes where each node points to the next one.

### Node Definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val       # the data
        self.next = next     # pointer to next node (or None if last)
```

### Creating a Linked List

```python
# Method 1: One at a time
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
# Result: 1 → 2 → 3 → None

# Method 2: Nested (compact)
head = ListNode(1, ListNode(2, ListNode(3)))
# Result: 1 → 2 → 3 → None
```

### Traversing a Linked List

```python
current = head
while current:              # while not None
    print(current.val)      # do something
    current = current.next  # move to next node
```

### Array vs Linked List

```
                   Array        Linked List
Access by index    O(1)         O(n)
Insert at start    O(n)         O(1)
Insert at end      O(1)         O(n)
Search             O(n)         O(n)
```

---

## Part 4: Classes and Objects

```python
class MinStack:                    # CLASS = blueprint
    def __init__(self):            # __init__ = constructor (runs when created)
        self.stack = []            # self = this specific object
        self.min_stack = []

    def push(self, val):           # methods always take self first
        self.stack.append(val)     # always use self.variable

s = MinStack()                     # OBJECT = real thing built from blueprint
s.push(5)                          # use the object
```

Key rules:
- `class` = blueprint, `object` = thing built from it
- `__init__` runs automatically when object is created
- `self` = the object referring to itself
- Always use `self.variable` inside methods, never just `variable`
- You never pass `self` yourself — Python does it automatically

---

## Part 5: Dummy Node Pattern

When building a new linked list, use a fake starting node to avoid
special-casing the first node:

```python
dummy = ListNode(0)      # fake node
current = dummy           # build from here

# ... attach nodes to current.next ...

return dummy.next         # skip the fake, return the real head
```

Without dummy: 10 lines to handle the first node
With dummy: 2 lines, then straight to the loop

---

## Part 6: Patterns Learned

### Pattern 1: Stack for Matching (Valid Parentheses)

**Signal:** "valid brackets", "matching pairs", "balanced"

```python
def is_valid(s):
    matches = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char not in matches:           # opening bracket
            stack.append(char)
        else:                              # closing bracket
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()
    return not stack
# Time: O(n)  Space: O(n)
```

### Pattern 2: Two Parallel Stacks (Min Stack)

**Signal:** "design a stack with O(1) getMin"

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

### Pattern 3: Reverse Linked List (Pointer Swap)

**Signal:** "reverse a linked list"

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next     # save next
        curr.next = prev          # flip pointer
        prev = curr               # move prev forward
        curr = next_node          # move curr forward
    return prev                    # prev is new head
# Time: O(n)  Space: O(1)
```

The four-line swap:
1. Save the next node (before breaking the link)
2. Flip the pointer (point backward)
3. Move prev forward
4. Move curr forward

### Pattern 4: Merge Two Sorted Lists (Dummy Node)

**Signal:** "merge two sorted lists"

```python
def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1       # attach entire remaining chain
    if list2:
        current.next = list2
    return dummy.next
# Time: O(n + m)  Space: O(1)
```

### Pattern 5: Fast/Slow Pointers (Cycle Detection)

**Signal:** "detect cycle", "find middle of linked list"

```python
# Cycle detection
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next           # 1 step
        fast = fast.next.next      # 2 steps
        if slow == fast:
            return True
    return False
# Time: O(n)  Space: O(1)
```

```python
# Find middle
slow = head
fast = head
while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next
# slow is now at the middle
```

Why `while fast and fast.next`: fast moves 2 steps, so you check
both fast and fast.next exist before doing fast.next.next.

### Pattern 6: Reorder List (Find Mid + Reverse + Merge)

**Signal:** "reorder list", "interleave front and back"

Three steps using patterns you already know:
1. Find middle (fast/slow pointers)
2. Reverse second half
3. Merge alternating

```python
def reorder_list(head):
    if not head or not head.next:
        return head

    # Step 1: Find middle
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    second = slow.next
    slow.next = None           # cut the list
    prev = None
    while second:
        next_node = second.next
        second.next = prev
        prev = second
        second = next_node
    second = prev

    # Step 3: Merge alternating
    first = head
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

    return head
```

---

## Part 7: Common Mistakes Made Today

1. Using `{}` instead of `[]` for dict access (freq{char} vs freq[char])
2. Forgetting `self.` inside class methods
3. Using `str` as variable name (shadows built-in)
4. `elif` without a condition (use `elif condition:` or `else:`)
5. Single `=` instead of `==` in comparisons
6. `prev = 0` instead of `prev = None` for linked list end
7. Returning `curr` instead of `prev` after reversing linked list
8. Forgetting to move pointers after attaching nodes

---

## Part 8: When to Use What

```
"Match brackets/pairs"           → Stack
"Undo/history/reverse order"     → Stack
"Next greater/smaller element"   → Monotonic Stack (Day 13)
"Process in order (FIFO)"        → Queue
"Reverse a linked list"          → prev/curr/next swap
"Merge two sorted lists"         → Dummy node + compare
"Detect cycle in linked list"    → Fast/slow pointers
"Find middle of linked list"     → Fast/slow pointers
"Reorder/rearrange linked list"  → Find mid + reverse + merge
```
