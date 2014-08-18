# 3.2 How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time. 

class Stack:
	def __init__(self,capacity=100):
		self.s1=[]
		self.count=-1
		self.capacity = capacity

	def isempty(self):
		return self.count ==-1

	def top(self):
		if self.isempty():
			print "The Stack is empty"
			return
		return self.s1[self.count]

	def pop(self):
		if self.isempty():
			print "The Stack is empty"
			return
		self.count-=1

	def push(self,val):
		if not self.isfull():
			self.s1.append(val)
			self.count+=1

	def isfull(self):
		return self.count ==self.capacity -1 


class StackWithMin:
	MAX_VAL = 2^31-1
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()
		self.s2.push(StackWithMin.MAX_VAL)

	def Isempty(self):
		return self.s1.isempty()

	def Push(self,val):
		self.s1.push(val)
		if val <=self.s2.top():
			self.s2.push(val)

	def Pop (self):
		if self.Isempty():
			print "The stack is already empty .."
		if (self.s1.top() == self.s2.top()):
			self.s2.pop()
		self.s1.pop()

	def Min(self):
		return self.s2.top()

# def Test():
# 	s =StackWithMin()
# 	s.Push(1)
# 	print s.Min()
# 	s.Push(2)
# 	print s.Min()
# 	s.Push(3)
# 	print s.Min()
# 	s.Push(0)

# 	s.Push(-1)
# 	print s.Min()
# 	s.Push(10)
# 	print s.Min()
# 	s.Pop()
# 	s.Pop()
# 	print s.Min()
# Test()
