# Implement a MyQueue class which implements a queue using two stacks.
from cc32 import Stack

class MyQueue:
	def __init__(self):
		self.s1=Stack()
		self.s2=Stack()

	def move_to(self):
		while not self.s1.isempty():
			val = self.s1.top()
			self.s2.push(self.s1.top())
			self.s1.pop()
			# print "length of s1 is %d" %self.s1.count

	def Pop(self):
		if self.s2.isempty():
			self.move_to()
		if self.s2.isempty():
			print "queue is empty..."
			return
		self.s2.pop()
		

	def Push(self,val):
		self.s1.push(val)

	def Front(self):
		if self.s2.isempty():
			self.move_to()
		if self.s2.isempty():
			print "queue is empty..."
			return None
		return self.s2.top()

def Test():
	q = MyQueue()
	q.Push(1)
	q.Push(2)
	q.Push(3)
	print q.Front() #1
	q.Pop()
	print q.Front() #2
	q.Pop()
	print q.Front() #3
	q.Push(5)
	print q.Front() #3
	q.Pop()
	print q.Front() #5
	q.Pop()
	q.Push(1)
	q.Pop()
	q.Push(2)
	q.Push(3)
	print q.Front() #empty
Test()	


