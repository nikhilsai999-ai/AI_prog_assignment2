Uninformed Search Algorithms – BFS, DFS and Variants

1. Water Jug Problem-
The Water Jug Problem is an example problem used to demonstrate search algorithms. In this problem, we are given two jugs with fixed capacities, and the goal is to measure a specific amount of water using these jugs.
Here we are using the (4,3) example, where-
Jug 1 capacity = 4 liters,Jug 2 capacity = 3 liters
Target = 2 liters
Initially, both jugs are empty.
Initial State is represented as- 
(0,0) .
The goal is to reach a state where either jug contains exactly 2 liters.
Example:
(2,0) or (2,x) where x is any amount of water that can be contained in jug 2 after jug 1 is filled to a capacity of 2 liters. 


2. State Space Representation
In the Water Jug problem, each state is represented as: (x, y)
x = amount of water in Jug1, y = amount of water in Jug2
The algorithm explores different states until the goal state is reached.


3. Rules / Operations
The following operations can be performed in the Water Jug problem:
1.Fill the first jug completely.
  (x,y)→(4,y)
Example:
(0,3) → (4,3)
2.Fill the second jug completely.
(x,y)→(x,3)
Example:
(4,0) → (4,3)
3.Empty the first jug completely.
(x,y)→(0,y)
Example:
(4,2) → (0,2)
4. Empty the second jug completely.
(x,y)→(x,0)
Example:
(3,3) → (3,0)
5. Transfer water from Jug1 to Jug2 until:
(x,y)→(x−min(x,3−y),y+min(x,3−y))
Jug1 becomes empty OR Jug2 becomes full
Example:
(4,1) → (2,3)
6. Transfer water from Jug2 to Jug1 until:
(x,y)→(x+min(y,4−x),y−min(y,4−x))
Jug2 becomes empty OR Jug1 becomes full
Example:
(1,3) → (4,0)
These rules generate new states which are explored by graph algorithms.


4. Breadth First Search (BFS)
Breadth First Search is an uninformed search algorithm that explores nodes level by level.
It uses a queue data structure to store states.
Working of BFS-
1.Start with the initial state
2.Insert the state into a queue
3.Remove a state from the queue
4.Generate all possible next states
5.If the goal state is found, stop
6.Otherwise add new states to the queue
7.Repeat until the goal state is reached

BFS-
1.Explores states level by level
2.Uses queue
3.Guarantees shortest path 
4.Requires more memory


5.Depth First Search (DFS)
Depth First Search is another uninformed search algorithm that explores nodes deep into the search tree first.
Instead of exploring level by level, it goes as deep as possible before backtracking.
DFS uses recursion or a stack data structure.

Working of DFS
Start from the initial state (0,0)
Visit the state and mark it as visited
Generate the next possible states
Move to one state and continue exploring deeper
If a dead end is reached, backtrack
Continue until the goal state is found


DFS-
1.Uses stack or recursion
2.Explores deep paths first
3.Uses less memory
4.Does not guarantee shortest path


Other Uninformed Search Methods
Apart from BFS and DFS, there are other search strategies which are variants of DFS.

6. Depth Limited Search (DLS)
Depth Limited Search is a variation of DFS where the search depth is limited to a fixed value. This prevents the algorithm from exploring infinitely deep paths.The algorithm stops searching once the depth limit is reached.Example-If the depth limit is 3, the algorithm explores only up to 3 levels of the search tree.The advantage is that it prevents infinite search in very deep trees.The disadvantage is that the goal state may exist deeper than the specified limit.


7.Iterative Deepening Depth First Search (IDDFS)
Iterative Deepening DFS combines the advantages of BFS and DFS. It repeatedly performs Depth Limited Search with increasing depth limits.
Perform DLS with depth limit = 0
Perform DLS with depth limit = 1
Perform DLS with depth limit = 2
Continue increasing the depth limit until the goal is found
Advantages-
1.Uses less memory like DFS.
2.Finds optimal solution like BFS.
It is basically the combination of the best features of both.


8. Comparison
Performance Comparison
Breadth First Search (BFS), Depth First Search (DFS), Depth Limited Search (DLS), and Iterative Deepening Depth First Search (IDDFS) are all uninformed search algorithms, but they explore the state space differently.

1.Breadth First Search explores nodes level by level using a queue. It is complete and guarantees the shortest path to the goal when all steps have equal cost. However, BFS requires more memory because it stores many states during the search.

2.Depth First Search explores nodes by going as deep as possible before backtracking. It uses recursion or a stack and requires less memory compared to BFS. However, DFS does not guarantee the shortest solution and may explore deep paths that do not lead to the goal.

3.Depth Limited Search is a variation of DFS where a maximum depth limit is set. This prevents the algorithm from searching infinitely deep paths, but the solution may be missed if it lies beyond the depth limit.

4.Iterative Deepening Depth First Search repeatedly performs depth-limited searches with increasing depth limits. It combines the advantages of BFS and DFS by finding the optimal solution while using relatively less memory.


