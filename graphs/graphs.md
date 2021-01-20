# Graphs

## Representation

>### Adjacency List
>
>```python
>{
>    'JFK': ['SFO', 'LAX'],
>    'SFO': ['ORL'],
>    'ORL': ['JFK', 'LAX', 'DFW'],
>    'LAX': ['DFW'],
>    'DFW': []
>}
>```
>
>### Adjacency Matrix
>
>```python
>indices = {'JFK': 0, 'SFO': 1, 'ORL': 2, 'LAX': 3, 'DFW': 4}
>graph = [
>    [0, 1, 0, 1, 0],
>    [0, 0, 1, 0, 0],
>    [1, 0, 0, 1, 1],
>    [0, 0, 0, 0, 1],
>    [0, 0, 0, 0, 0]
>]
>```

## Traversing

### Breadth First Search

#### General

>

#### Connected Components

#### Bipartite Graphs

### Depth First Search

#### General

> ### Recursive
>
> ```python
> def DFS(graph, start, visited=set()):
>     visited.add(start)
>     for neighbor in graph[start]:
>         if neighbor not in visited:
>             DFS(graph, neighbor, visited)
>             
>      return visited
> ```
>
> ### Iterative
>
> ```python
> def DFS(graph, start, visited=set()):
>     stack = [start,]
>     while stack:
>         current = stack.pop()
>         visited.add(current)
>         for neighbor in graph[current]:
>             if neighbor not in visited:
>                 stack.append(neighbor)
> 
>     return visited
> ```

#### Finding Cycles

> Given an undirected graph, determine if it contains a cycle.
>
> ```python
> def search(graph, vertex, visited, parent):
>     visited[vertex] = True
>     
>     for neighbor in graph[vertex]:
>         if not visited[neighbor]:
>             if search(graph, neighbor, visited, vertex):
>                 return True
>             elif parent != neighbor:
>                 return True
>             
>      return False
> 
> def has_cycle(graph):
>     visited = {v: False for v in graph.keys()}
>     
>     for vertex in graph.keys():
>         if not visited[vertex]:
>             if search(graph, vertex, visited, None):
>                 return True
>             
>     return False
> ```

#### Articulation of Graph

#### Topological Sorting on DAGs

> [Topological Sort](https://en.wikipedia.org/wiki/Topological_sorting) of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex `U` to vertex `V`, `U` comes before `V` in the ordering.
>
> Given a directed graph, find the topological ordering of its vertices.
>
> ```bash
> # Example 1:
> > topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
> > [3, 2, 0, 1]
> # Example 2:
> > topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])
> > [5, 6, 3, 4, 0, 2, 1]
> ```
>
> This is how we can implement this algorithm:
>
> **a. Initialization**
>
> 1. We will store the graph in **Adjacency Lists**, which means each parent vertex will have a list containing all of its children. We will do this using a **HashMap** where the ‘key’ will be the parent vertex number and the value will be a **List** containing children vertices.
> 2. To find the sources, we will keep a **HashMap** to count the in-degrees i.e., count of incoming edges of each vertex. Any vertex with ‘0’ in-degree will be a source.
>
> **b. Build the graph and find in-degrees of all vertices**
>
> 1. We will build the graph from the input and populate the in-degrees **HashMap**.
>
> **c. Find all sources**
>
> 1. All vertices with ‘0’ in-degrees will be our sources and we will store them in a **Queue**.
>
> **d. Sort**
>
> 1. For each source, do the following things:
>    - Add it to the sorted list.
>    - Get all of its children from the graph.
>    - Decrement the in-degree of each child by 1.
>    - If a child’s in-degree becomes ‘0’, add it to the sources **Queue**.
> 2. Repeat step 1, until the source **Queue** is empty.
>
> ```python
> from collections import deque
> 
> def topological_sort(vertices, edges):
>   sortedOrder = []
>   if vertices <= 0:
>     return sortedOrder
> 
>   # a. Initialize the graph
>   inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
>   graph = {i: [] for i in range(vertices)}  # adjacency list graph
> 
>   # b. Build the graph
>   for edge in edges:
>     parent, child = edge[0], edge[1]
>     graph[parent].append(child)  # put the child into it's parent's list
>     inDegree[child] += 1  # increment child's inDegree
> 
>   # c. Find all sources i.e., all vertices with 0 in-degrees
>   sources = deque()
>   for key in inDegree:
>     if inDegree[key] == 0:
>       sources.append(key)
> 
>   # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
>   # if a child's in-degree becomes zero, add it to the sources queue
>   while sources:
>     vertex = sources.popleft()
>     sortedOrder.append(vertex)
>     for child in graph[vertex]:  # get the node's children to decrement their in-degrees
>       inDegree[child] -= 1
>       if inDegree[child] == 0:
>         sources.append(child)
> 
>   # topological sort is not possible as the graph has a cycle
>   if len(sortedOrder) != vertices:
>     return []
> 
>   return sortedOrder
> ```
>
> 

#### Strongly Connected Components on DAGs

## Weighted Graph Algorithms

### Minimum Spanning Trees

#### Prim's Algorithm

#### Kruskal's Algorithm

#### Union Find Data Structure (Disjoint Subsets)

### Shortest Paths

#### Dijkstra's Algorithm

>A network of nodes where the edges have some weight/cost associated to them between the nodes.
>
>To find the shortest/least costly path between a vertex and another vertex **assuming all edges have ==non-negative== weights** is Dijkstra's algorithm. It works by repeatedly traveling to the closest vertex which has not yet been reached.
>
>1. Create a dictionary `costs` - mapping each node to the minimum amount of cost it takes for a message to propagate to it. Initialize to `inf` for all nodes, except for the start node for which it is `0`.
>2. Consider an unvisited node and update it with the smallest propagation cost. For each of its neighbors, replace the propagation time with the time it would take to go through the current node **if it is smaller**.
>3. Continue this process until all nodes have been visited.
>4. Return the largest value in the dictionary as the `minimum/shortest path` total to reach the last node
>
>Time complexity: $O(n^2)$
>
>Space Complexity: $O(n)$
>
>```python
>class Network:
>    def __init__(self, N, edges):
>        self.vertices = range(N + 1)
>        self.edges = edges
>        
>    def make_graph(self):
>        graph = {v: [] for v in network.vertices}
>        
>        for u, v, w in network.edges:
>            graph[u].append((v, w))
>            
>        return graph
>    
>    def propagate(network):
>        graph = network.make_graph()
>        costs = {node: float('int') for node in graph}
>        costs[0] = 0
>        
>        q = list(graph)
>        while q:
>            u = min(q, key=lambda x: costs[x])
>            q.remove(u)
>            for v, cost in graph[u]:
>                costs[v] = min(costs[v], costs[u] + cost)
>                
>        return max(times.values())
>```
>
>We can use a **priority queue** for sparse graphs - ordering each node by propagation time.
>
>1. Start the priority queue (heap) to hold just the `start node` with value `0`.
>2. Each time we encounter a new neighbor, we add it to the queue, with value equal to the sum of the time from node zero to the current node, and from the current node to the neighbor.
>3. Whenever we pop a node off the queue that does not exist in the `costs` dictionary, we add a new key with the corresponding value.
>
>Time complexity: $O((|E|+|V|)logV)$
>
>```python
>def propagate(network):
>    graph = network.make_graph()
>    times = {}
>    
>    q = [(0, 0)]
>    while q:
>        u, node = heapq.heappop(q)
>        if node not in times:
>            times[node] = u
>            for neighbor, v in graph[node]:
>                if neighbor not in times:
>                    heapq.heappop(q, (u + v, neighbor))
>                    
>    return max(times.values())
>```

#### Bellman-Ford

> Some differences with Dijkstra's Algorithm:
>
> 1. Bellman-Ford (BF) has a time complexity of $O(VE(|V|-1)) \approx O(n^3)$ vs. Dijkstra's $O(n^2)$
> 2. BF does relaxation all nodes for `|V|-1` times and Dijkstra does it per node and only once.
> 3. BF can handle negative weights but Dijkstra's can't. It can also detect negative cycles.
> 4. BF visits a vertex more than once but Dijkstra's visits only once.
>
> The algorithm is as follows:
>
> 1. Set a `source` node, and set the distance/cost to all other nodes as `inf`
> 2. For each edge `(u, v)` in the graph, check if it is more efficient to get to `v` along the edge from `u` than the current best option. If so, then update the value for `v`.
> 3. Note: for any graph with `V` vertices, the longest path can have at most `|V| - 1` edges.
>    - thus we can repeat the above operation `|V| - 1` times and eventually arrive at the optimal way to reach each vertex
> 4. After `|V| - 1` iterations, if we still find a smaller path, there must be a negative cycle in the graph.
>
> ```python
> from math import log
> 
> def arbitrage(table):
>     transformed_graph = [[-log(edge) for edge in row] for row in graph]
>     
>     # Pick any source vertex - we can run Bellman-Ford from any vertex and
>     # get the right result
>     source = 0
>     n = len(transformed_graph)
>     min_dist = [float('inf')] * n
>     
>     min_dist[source] = 0
>     
>     # Relax edges |V - 1| times
>     for i in range(n - 1):
>         for v in range(n):
>             for w in range(n):
>                 if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
>                     min_dist[w] = min_dist[v] + transformed_graph[v][w]
>                     
>     # If we can still relax edges, then we have a negative cycle:
>     for v in range(n):
>         for w in range(n):
>             if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
>             	return True
>             
>     return False
> ```
>
> ### Example - Currency Exchange Arbitrage Opportunity
>
> Imagine you had a table of currency exchange rates between any two currencies as below:
>
> ```python
> graph = {
>     'USD': {'GBP': 0.77, 'INR': 71.71, 'EUR': 0.87},
>     'GBP': {'USD': 1.30, 'INR': 93.55, 'EUR': 1.14},
>     'INR': {'USD': 0.014, 'GBP': 0.011, 'EUR': 0.012},
>     'EUR': {'USD': 1.14, 'GBP': 0.88, 'INR': 81.95}
> }
> ```
>
> We can model this such that each currency is a node, and edges between the nodes are the exchange rates between each currency.
>
> The goal is to **find a cycle whose edge weight product is greater than one**.
>
> How to handle product of edge weights (instead of sum of edge weights)?
>
> - Use the property of $log(ab)=log(a)+log(b)$
> - Take the $log$ of all exchange rates, and negate them to ensure all weights are positive
>
> Then find a negative sum cycle using BF.

#### Floyd-Warshall

> Used to find the shortest path between **all** vertices in a weighted graph i.e. no starting/source node is used.