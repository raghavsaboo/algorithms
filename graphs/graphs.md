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



