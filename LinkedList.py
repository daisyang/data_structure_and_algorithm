class Node:
	def __init__(self,val=None, next = None):
		self.val = val
		self.next =next

class LinkedList:
	def __init__(self,val = None):
		self.first = Node(val)
		self.last = self.first
		self.count = 0

	def add(self,val):
		self.last.next = Node(val)
		self.last = self.last.next
		self.count+=1
	
	def remove(self,val):
		prev = None
		current = self.first
		if self.size ==0:
			pass
		while current:
			if val is current:
				if prev is None:
					self.first = current.next
				else:
					prev.next = current.next
				self.count-=1
				break
			prev= current
			current = current.next

	def Print (self):
		current = self.first
		while current:
			print current.val
			current = current.next

	def count(self):
		return self.count
	