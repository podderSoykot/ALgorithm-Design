"""
Bfs algorithm used to search atree or graph data stracture for a
node that meets a set of criteria. It begans that the root of the 
tree or graph and investigates all nodes at the current depth 
level before moving on to nodes at the next depth level before 
moving on to nodes at the next depth level.

Breadth First Search (BFS) is a fundamental algorithm used to 
explore nodes and edges of a graph in the order of their distance 
from a starting node. It's particullarly usefull for finding the 
shortest path in an unweighted graph or for exploring all nodes
at a certain "level" before moving deeper into the graph.

BFS:

Start from a Node: designated starting node.
Use a queue: Utilize a queue to explore  level by lavel. This 
queue helps manage which  node to visit next.

Mark Visited Node: Trace which node have been visited  to avoid
preprocessing  the same node multiplw times.

Explore Neighbours: For each node, explore  it's neighbouring 
queue if they haven't been visited yet.

Repeat: Continue this process until there are no more nodes
to explore (the qqueue is empty)



"""

from collections import deque

def bfs(graph,start):
    queue=deque([start])
    visited=set([start])
    while queue:
        current=queue.popleft()
        print(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":[],
    "F":[]
}

bfs(graph,"A")