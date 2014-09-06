class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo={} # a dictionary of neighborID and weight
	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr]=weight
	def __str__(self):
		return str(self.id) + ' connectedTo: '+str([x for x in self.connectedTo] )
	def getConnections(self):
		return self.connectedTo.keys()
	
	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]

class Graph:
	def __init__(self):
		self.vertList={} # a dictionary of (vertexID , vertex )
		self.numVertices = 0
	def addVertex(self,key):
		self.numVertices = self.numVertices + 1
		if key in self.vertList:
			return None
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex
	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def __contains__(self,n):
		return n in self.vertList
	
	def addEdge(self,f,t,cost = 0): # f and t is already in the graph vertexlist
		self.vertList[f].addNeighbor(t,cost)
	def getVertices(self):
		return self.vertList.keys()
	
	def __iter__(self):
		return iter(self.vertList.values())
def main():
	g = Graph()
	for i in range(6):
		g.addVertex(i)
	g.addEdge(0,1,5)
	g.addEdge(0,5,2)
	g.addEdge(1,2,4)
	g.addEdge(2,3,9)
	g.addEdge(3,4,7)
	g.addEdge(3,5,3)
	g.addEdge(4,0,1)
	g.addEdge(5,4,8)
	g.addEdge(5,2,1)
	for v in g :
		for w in v.getConnections():
			print "%s, %s" %(v.getId(), w)
	v=g.getVertex(0)
	print v.getConnections()

if __name__ == '__main__':
	main()

