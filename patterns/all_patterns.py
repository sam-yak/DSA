"""
=== CORE DSA PATTERN TEMPLATES ===
Master these 10 templates and you can solve 90% of Google interview problems.
Each template is labeled with WHEN to use it.

Build this muscle memory: See signal → Recall pattern → Adapt to problem
"""


# ============================================================
# PATTERN 1: HASH MAP — O(1) Lookup
# ============================================================
# WHEN: Need to find complement/pair, count frequencies,
#       group items, check existence in O(1)
# SIGNAL: "find two numbers that...", "group by...", "count..."

def two_sum_pattern(nums, target):
    """Use hash map to store {value: index} for O(1) complement lookup."""
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def frequency_count_pattern(items):
    """Count occurrences — use collections.Counter or manual dict."""
    from collections import Counter
    freq = Counter(items)  # or defaultdict(int) + loop
    return freq


# ============================================================
# PATTERN 2: TWO POINTERS
# ============================================================
# WHEN: Sorted array, find pair/triplet, palindrome check,
#       merge sorted arrays, partition
# SIGNAL: "sorted array", "pair that sums to", "palindrome"

def opposite_direction(arr):
    """Two pointers moving inward — for sorted array pair finding."""
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1       # need bigger sum
        else:
            right -= 1      # need smaller sum


def same_direction(arr):
    """Fast/slow pointer — for linked list cycle, middle finding."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # slow is now at middle (or meeting point if cycle)


# ============================================================
# PATTERN 3: SLIDING WINDOW
# ============================================================
# WHEN: Contiguous subarray/substring, max/min of k-size window,
#       "longest substring with constraint"
# SIGNAL: "subarray", "substring", "contiguous", "window of size k"

def fixed_window(arr, k):
    """Fixed-size window — compute sum/property of every k-length subarray."""
    window_sum = sum(arr[:k])
    result = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # slide: add right, remove left
        result = max(result, window_sum)
    return result


def variable_window(s):
    """Variable-size window — expand right, shrink left when invalid."""
    left = 0
    window = {}      # track window state (freq map, set, etc.)
    result = 0
    for right in range(len(s)):
        # 1. EXPAND: add s[right] to window
        window[s[right]] = window.get(s[right], 0) + 1

        # 2. SHRINK: while window is invalid, remove s[left]
        while window_is_invalid():
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        # 3. UPDATE: record best valid window
        result = max(result, right - left + 1)
    return result


# ============================================================
# PATTERN 4: BINARY SEARCH
# ============================================================
# WHEN: Sorted array, search space can be halved, "minimum that satisfies",
#       "find boundary"
# SIGNAL: "sorted", "O(log n)", "find minimum/maximum that..."

def standard_binary_search(arr, target):
    """Classic binary search — find exact target."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_on_answer(lo, hi):
    """Binary search the answer space — 'minimum X such that condition(X) is True'."""
    while lo < hi:
        mid = (lo + hi) // 2
        if condition(mid):  # feasible
            hi = mid         # try smaller
        else:
            lo = mid + 1     # too small, go bigger
    return lo


# ============================================================
# PATTERN 5: BFS (Breadth-First Search)
# ============================================================
# WHEN: Shortest path (unweighted), level-order traversal,
#       multi-source spread, nearest X
# SIGNAL: "shortest", "minimum steps", "level by level", "nearest"

from collections import deque

def bfs_graph(graph, start):
    """Standard BFS — shortest path in unweighted graph."""
    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))


def bfs_grid(grid):
    """BFS on 2D grid — use for shortest path, multi-source spread."""
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    visited = set()
    # Add starting positions to queue
    # queue.append((r, c, 0))  # row, col, distance
    while queue:
        r, c, dist = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] != 0:  # valid cell
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))


# ============================================================
# PATTERN 6: DFS (Depth-First Search)
# ============================================================
# WHEN: Explore all paths, connected components, tree traversals,
#       island counting, flood fill
# SIGNAL: "all paths", "connected", "count islands", "explore"

def dfs_recursive(grid, r, c, visited):
    """DFS on grid — recursive. Use for connected components, flood fill."""
    if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0])
            or (r, c) in visited or grid[r][c] == 0):
        return
    visited.add((r, c))
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dfs_recursive(grid, r + dr, c + dc, visited)


def dfs_iterative(graph, start):
    """DFS with explicit stack — avoids recursion depth issues."""
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)


# ============================================================
# PATTERN 7: BACKTRACKING
# ============================================================
# WHEN: Generate all combinations/permutations/subsets,
#       constraint satisfaction, N-Queens, Sudoku
# SIGNAL: "all possible", "generate all", "combinations", "permutations"

def backtrack(state, choices, result):
    """
    Backtracking template:
    1. Check if we've reached a goal state
    2. For each choice: make it, recurse, undo it
    """
    if is_goal(state):
        result.append(state[:])  # COPY the state
        return

    for i, choice in enumerate(choices):
        if is_valid(choice, state):
            state.append(choice)                    # MAKE choice
            backtrack(state, choices[i+1:], result)  # RECURSE (i+1 for combos, all for perms)
            state.pop()                              # UNDO choice


# ============================================================
# PATTERN 8: TOPOLOGICAL SORT (Kahn's Algorithm)
# ============================================================
# WHEN: Dependency ordering, course prerequisites, build order,
#       detect cycles in directed graph
# SIGNAL: "prerequisites", "order of", "dependency", "schedule"

from collections import defaultdict

def topological_sort(num_nodes, edges):
    """Kahn's BFS-based topological sort. Returns [] if cycle exists."""
    graph = defaultdict(list)
    indegree = [0] * num_nodes
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque(i for i in range(num_nodes) if indegree[i] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_nodes else []  # empty = cycle


# ============================================================
# PATTERN 9: UNION-FIND (Disjoint Set)
# ============================================================
# WHEN: Dynamic connectivity, "are X and Y connected?",
#       count connected components, detect cycle in undirected graph
# SIGNAL: "connected", "groups", "components", "union"

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already connected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px  # union by rank
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True


# ============================================================
# PATTERN 10: DYNAMIC PROGRAMMING
# ============================================================
# WHEN: Optimal substructure + overlapping subproblems,
#       counting ways, min/max cost, "can you reach..."
# SIGNAL: "minimum cost", "number of ways", "can you", "longest/shortest"

# FRAMEWORK (use for EVERY DP problem):
# 1. Define state: what does dp[i] (or dp[i][j]) represent?
# 2. Recurrence: dp[i] = f(dp[i-1], dp[i-2], ...)
# 3. Base cases: dp[0] = ?, dp[1] = ?
# 4. Iteration order: left→right? bottom→up?
# 5. Space optimization: do we only need last 1-2 rows?

def dp_1d(nums):
    """1D DP template — each state depends on previous states."""
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = 1  # base case (problem-specific)

    for i in range(1, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # recurrence (problem-specific)

    return dp[n]


def dp_2d(text1, text2):
    """2D DP template — for two-sequence problems (LCS, edit distance)."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


# ============================================================
# BONUS: MONOTONIC STACK
# ============================================================
# WHEN: "Next greater/smaller element", histogram problems,
#       "for each element, find the nearest X"
# SIGNAL: "next greater", "previous smaller", "histogram"

def next_greater_element(nums):
    """Find next greater element for each position."""
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices, maintains decreasing values

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]  # nums[i] is the next greater for idx
        stack.append(i)

    return result


# ============================================================
# BONUS: PREFIX SUM
# ============================================================
# WHEN: Range sum queries, subarray sum equals K,
#       "sum of subarray from i to j"
# SIGNAL: "subarray sum", "range sum", "cumulative"

def prefix_sum(nums):
    """Build prefix sum for O(1) range queries."""
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    # sum of nums[i:j] = prefix[j] - prefix[i]
    return prefix


def subarray_sum_equals_k(nums, k):
    """Count subarrays with sum = k using prefix sum + hash map."""
    count = 0
    curr_sum = 0
    prefix_counts = {0: 1}  # prefix_sum -> frequency

    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix_counts:
            count += prefix_counts[curr_sum - k]
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1

    return count
