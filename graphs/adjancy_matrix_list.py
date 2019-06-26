# One of the easiest ways to implement a graph is to use a two-dimentional matrix.
# In this matrix implementation, each of the rows and columns represent a vertex in the graph.
# The value that is stored in the cell at the intersection of row v and column w indicates if there is an edge from vertex v to vertex w.
# When two vertices are connected by an edge, we say that they are adjacent.

# Adjancy list
# - a more space-efficient way to implement a sparsely connected graph is to use an adjacency list.
# - in an adjacency list implementation we keep a master list of all vertices in the graph object and then each
#    vertex object in the graph maintains a list of the other vertices that it is connected to.
# - In our implementation of the Vertex class we will use a  dictionary rather than a list of where the dictionary keys are the vertices, and
#   the values are the weights.


class Vertex:

	def __init__(self, key):
		self.id = key
		self.connectedTo = {}

	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def getConnection(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

	def __str__(self):
		return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])


class Graph:

	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self, key):
		self.numVertices = self.numVertices + 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex

		return newVertex

	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def addEdge(self, f, t, cost=0):
		if f not in self.vertList:
			nv = self.addVertex(f)

		if t not in self.vertList:
			nv = self.addVertex(t)

		self.vertList[f].addNeighbor(self.vertList[t], cost)


	def getVertices(self):
		return self.vertList.keys()


	def __iter__(self):
		return iter(self.vertList.values())

	def __contains__(self, n):
		return n in self.vertList


g = Graph()

for i in range(6):
	g.addVertex(i)

print(g.vertList)

g.addEdge(0,1,2)

for vertex in g:
	print(vertex)