class Node:
	def __init__(self,val=None,next=None):
		self.val=val
		self.next=next
	def __str__(self):
		return str(self.val)

class LinkedList:
	def __init__(self,val = None):
		self.root = Node(val)
		self.root.next = None

	def AddNode(self,val):
		current = self.root
		while current.next is not None :
			current = current.next
		current.next = Node(val)

	def Print (self):
		current = self.root
		while current:
			print current
			current = current.next

	def last(self):
		root = self.root
		while root.next is not None: 
			root=root.next
		return root