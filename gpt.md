🧠 MASTER CLASSIFICATION
BUCKET (Technique)
   → Pattern (Why we use it)
       → Data Structure
           → Example Problems

🔵 1. BFS BUCKET
✅ Core Idea:
Level-by-level exploration (queue)

🧩 Patterns under BFS

1. Shortest Path (unweighted graph)
👉 BFS guarantees minimum steps

Data Structures:

Graph
Grid
Problems:

Rotten Oranges
01 Matrix
Shortest Path in Binary Matrix
Walls and Gates
Word Ladder

2. Multi-source BFS
👉 Start from multiple points at once

Data Structures:

Grid / Graph
Problems:

Rotten Oranges
Walls and Gates
As Far from Land as Possible

3. Level Order Traversal

👉 Pure tree BFS

Data Structures:

Tree
Problems:

Binary Tree Level Order Traversal
Zigzag Level Order
Average of Levels

4. BFS for State Space
👉 Each state = node

Data Structures:

Graph (implicit)
Problems:

Open the Lock
Minimum Genetic Mutation


🟢 2. DFS BUCKET (Traversal DFS)

✅ Core Idea:
Go deep, no choices, no undo

🧩 Patterns under DFS

1. Tree Traversal

👉 Basic DFS

Data Structures:

Tree
Problems:

Inorder / Preorder / Postorder
Max Depth of Binary Tree
Diameter of Binary Tree

2. Connected Components
👉 Count regions

Data Structures:

Graph / Grid
Problems:

Number of Islands
Number of Provinces
Flood Fill

3. Cycle Detection
👉 Detect loops

Data Structures:

Graph
Problems:

Detect Cycle in Undirected Graph
Course Schedule (DFS version)

4. Path Existence

👉 Just check if path exists

Data Structures:

Graph
Problems:

Find if Path Exists in Graph

🟡 3. BACKTRACKING BUCKET (Decision DFS)
✅ Core Idea:
DFS + choices + undo

🧩 Patterns under Backtracking

1. Generate All Subsets

👉 Include / exclude

Data Structures:

Array
Problems:

Subsets
Subsets II

2. Permutations

👉 Arrange elements

Data Structures:

Array
Problems:

Permutations
Permutations II

3. Combination Sum
👉 Choose multiple times

Data Structures:

Array
Problems:

Combination Sum
Combination Sum II

4. Grid Backtracking

👉 Move in directions + undo

Data Structures:

Grid
Problems:

Word Search ✅ (your confusion)
Path with maximum gold

5. Constraint Placement Problems
👉 Place things carefully

Data Structures:

Board / Grid
Problems:

N-Queens ✅ (your confusion)
Sudoku Solver

🔴 4. TOPOLOGICAL SORT BUCKET

✅ Core Idea:
Ordering with dependencies (DAG only)

🧩 Patterns under Topo Sort

1. Course Scheduling (dependency resolution)
Data Structures:

Graph (Directed)
Problems:

Course Schedule
Course Schedule II

2. Kahn’s Algorithm (BFS based)

Technique:

Indegree + queue
Problems:

Course Schedule
Alien Dictionary

3. DFS Topo Sort
Technique:

Postorder stack
Problems:

Course Schedule (DFS version)

4. Ordering Problems
Problems:

Alien Dictionary
Find Eventual Safe States

--------------------------------------------------------------------------
🔵 5. SHORTEST PATH BUCKET (VERY IMPORTANT)
✅ Core Idea:
Find minimum cost / distance path

🧩 Patterns

1. Unweighted Shortest Path

👉 Uses BFS (you already covered)

Rotten Oranges
Word Ladder

2. Weighted Shortest Path (Dijkstra)

👉 Uses Priority Queue (Min Heap)

Data Structure:

Graph (weighted)
Problems:

Dijkstra Algorithm
Network Delay Time
Cheapest Flights Within K Stops

3. Bellman-Ford (advanced)

👉 Handles negative weights

(You don’t need this immediately but good to know)

🟣 6. MINIMUM SPANNING TREE (MST) BUCKET

✅ Core Idea:
Connect all nodes with minimum total cost

🧩 Patterns

1. Kruskal’s Algorithm

👉 Uses Disjoint Set (Union-Find)

Problems:

Minimum Cost to Connect All Points
Kruskal MST problems

2. Prim’s Algorithm

👉 Heap-based

🟡 7. DISJOINT SET (UNION-FIND) BUCKET

✅ Core Idea:
Group elements into connected components efficiently

🧩 Patterns

1. Dynamic Connectivity

Problems:

Number of Connected Components in Graph
Number of Provinces

2. Cycle Detection

Problems:

Detect Cycle (Undirected Graph)

3. Grid Connectivity

Problems:

Number of Islands (alternative to DFS)
Accounts Merge
✅ Operations
find(x)       # find parent
union(x, y)   # connect

🟢 8. GRAPH + BACKTRACKING (ADVANCED MIX)

✅ Core Idea:
DFS + constraints + graph

Problems:
Word Search ✅
All Paths from Source to Target
Hamiltonian Path (advanced)

🔴 9. GRAPH COLORING / BIPARTITE
✅ Core Idea:
Divide graph into groups without conflict

🧩 Patterns
1. Bipartite Graph
Technique:

BFS or DFS
Problems:

Is Graph Bipartite?
Possible Bipartition


🟠 10. MATRIX / GRID AS GRAPH (SPECIALIZED BUCKET)
You already touched this, but it’s so common it deserves its own category.

🧩 Patterns
1. Island problems
Number of Islands
Max Area of Island
2. Shortest path in grid
Shortest Path in Binary Matrix
01 Matrix
3. Multi-source problems
Rotten Oranges
Walls and Gates


✅ Build a 10–15 problem curated list (covering ALL of these buckets in perfect order)
→ This will remove randomness from your prep completely

Just say “roadmap” 👍

✅ DFS connects to:

Backtracking Tree traversal Graph traversal

✅ BFS connects to:

Shortest path Topo sort

✅ Heap connects to:

Dijkstra Top K Greedy

✅ DP connects to:

Optimization problems Backtracking improvement

✅ Greedy connects to:

Intervals Scheduling

✅ Trie connects to:

Strings Backtracking (Word Search II)
