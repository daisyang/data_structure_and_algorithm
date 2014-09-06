# Given a directed graph, design an algorithm to find out whether 
#there is a route between two nodes.
from Graph import *
from collections import deque
#check if the graph contains circle, if it does, need to keep track of visited nodes!!
#also check what is the graph representation, is it the adjacency list or matrix ?
def BFS(g,start,des):
	queue=deque()
	visited=[]
	queue.append(start)
	while queue:
		node = queue.popleft()
		if node is des:
			return True
		if node not in visited:
			queue.extend(g.getVertex(node).getConnections())
		visited.append(node)
	return False

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
	print "result:"
	connected = BFS(g,0,3)
	print connected
if __name__ == '__main__':
	main()