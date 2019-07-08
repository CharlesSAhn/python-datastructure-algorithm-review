

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}



def dfs(graph, start, visited = None):
	if visited is None:
		visited = []

	visited.append(start)

	for neighbor in graph[start]:
		if neighbor not in visited:
			dfs(graph, neighbor, visited)

	return visited


def dfs(graph, start):
	visited = []
	stack = [start]

	while stack:
		vertex = stack.pop()

		if vertex not in visited:
			visited.append(vertex)

			for n in graph[vertex]:
				if n not in visited:
					stack.append(n)


	return visited


graph2 = {'A': ['B', 'C'],
         'B': ['D'],
         'C': ['D'],
         'D': ['C']}

def dfs_path(graph, start, goal):
	visited = []
	stack = [ [start] ]
	paths = []

	while stack:
		path = stack.pop()

		node = path[-1]

		if node not in visited:

			neighbors = graph[node]

			for neighbor in neighbors:
				new_path = list(path)
				new_path.append(neighbor)
				stack.append(new_path)

				if neighbor == goal:
					paths.append(new_path)

			visited.append(node)




	return paths

print(dfs_path(graph2, 'A', 'D'))