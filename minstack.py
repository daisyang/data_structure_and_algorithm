# 3.2 How would you design a stack which, in addition to push and pop, also has a function min which returns the minimum element? push, pop and min should all operate in O(1) time. 

class Stack:
	def __init__(self,capacity=100):
		self.s=100*[None]
		self.count=-1
		self.capacity = capacity

	def isempty(self):
		return self.count ==-1

	def top(self):
		if self.isempty():
			print "The Stack is empty"
			return
		return self.s[self.count]

	def pop(self):
		if self.isempty():
			print "The Stack is empty"
			return
		self.count-=1
		self.pop()

	def push(self,val):
		if not self.isfull():
			self.count+=1
			self.s[self.count] = val

	def isfull(self):
		return self.count ==self.capacity -1 


class StackWithmin:
	MAX_VAL = 2^31-1 # sys.MAXINT
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()
		self.s2.push(StackWithmin.MAX_VAL) #make sure the stack is not None

	def isempty(self):
		return self.s1.isempty()

	def push(self,val):
		self.s1.push(val)
		if val <=self.s2.top():
			self.s2.push(val)

	def pop (self):
		if self.isempty():
			print "The stack is already empty .."
		if (self.s1.top() == self.s2.top()):
			self.s2.pop()
		self.s1.pop()

	def min(self):
		return self.s2.top()

def main():
	s =StackWithmin()
	s.push(1)
	print s.min()
	s.push(2)
	print s.min()
	s.push(3)
	print s.min()
	s.push(0)
	s.push(-1)
	print s.min()
	s.push(10)
	print s.min()
	s.pop()
	s.pop()
	print s.min()
	s.push(-1)
	print s.min()
	s.push(10)
	print s.min()
	s.pop()
	s.pop()
	print s.min()

	
if __name__ == "__main__":
	main()

