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


graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}


def bfs_connected_component(graph, start):

	#track visited nodes
	explored = []

	#track of nodes to be checked
	queue = [start]

	while len(queue) > 0:

		#pop the first node
		node = queue.pop(0)

		if node not in explored:
			explored.append(node)
			neighbors = graph[node]

			#add neighbors to the queue
			for neighbor in neighbors:
				queue.append(neighbor)

	return  explored

print(bfs_connected_component(graph, 'A'))



def bfs_shortest_path(graph, start, end):
	#track visited nodes
	explored = []

	#track of possible paths
	queue = [[start]]

	if start == end:
		return

	while queue:
		path = queue.pop(0)

		#get the last node from the pop
		node = path[-1]

		if node not in explored:
			neighbors = graph[node]

			for neighbour in neighbors:
				new_path = list(path)   # copy the current path
				new_path.append(neighbour)  # update the path with the current node
				queue.append(new_path)

				# return path if neighbour is goal
				if neighbour == end:
					return new_path

			explored.append(node)

	return "So sorry, but a connecting path doesn't exist :("

print(bfs_shortest_path(graph, 'A', 'G'))


# Con:  high cost (high memory requriement) - need to keep track of all the nodes
# the time complexity: 



