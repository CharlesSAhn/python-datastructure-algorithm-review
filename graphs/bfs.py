# 1. BFS begins at the starting vertex s and colors start gray to show that it is currently being explored.
# 2. Two other values, the distance and the predecessor, are intialized to 0 and None respectively for the starting vertex.
# 3. Finally, start is placed on a Queue
# 4. The next step is to begin to systematically explore vertices at the front of the queue.
# 5. We explore each new node at the front of the queue by iterating over its adjacency list.  As each node on the adjancency list is examined its color is checked.
# 6. If it is white, the vertex is unexplorered, and four things happen:
   #. The new, unexplored vertex nbr, is colored gray.
   #. The predecessor of nbr is set to the current node currentVert
   #. The distance to nbr is set to the distance to currentVert + 1
   #. nbr is added to the end of a queue.  Addoing nbr to the end of the queue effectively schedules this node for further exploration, but not until all the
    # other vertices on the adjancey list of currentVert have been explored.