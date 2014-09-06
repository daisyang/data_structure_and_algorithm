# Write an algorithm to find the next node (i.e., in-order successor) of a given node in a binary search tree where each node has a link to its parent.

class Node:
	def __init__(self,val=None,left = None, right = None,parent = None):
		self.val= val
		self.left = left
		self.right = right
		self.parent = parent
	def addleft(self,val):
		self.left=Node(val)
		self.left.parent = self
	def addright(self,val):
		self.right = Node(val)
		self.right.parent = self
	def left(self):
		return self.left
	def right(self):
		return self.right
	def parent(self):
		return self.parent

def minleftchild(node):
	if not node:
		return None
	while node.left:
		node = node.left
	return node

def successor(root):
	if not root:
		return
	if root.right:
		return minleftchild(root.right)
	
	p = root.parent
	while  p and p.val < root.val:
		p = p.parent

	return p

#if this is not a binary search tree
# the successor of a node for a binary tree is that : if the node has right child, the successor
# is the left most left child of its right child. if the node doesn't have right child, the successor is the closest ancestor whose left branch contains the node 
def successor2(root):
	if not root:
		return
	if root.right:
		return minleftchild(root.right)
	
	p = root.parent
	while p and p.right == root:
		root = p 
		p = p.parent

	return p


def main():
	root = Node(10)
	root.addleft(5)
	root.addright(11)
	root.left.addleft(4)
	root.left.addright(6)

	root.left.left.addleft(3)
	root.left.left.addright(4.5)
	root.left.left.right.addright(4.7)
	n= root.left.left.right.right
	p = successor2(n)

	print n.val
	print p.val
if __name__ == '__main__':
	main()