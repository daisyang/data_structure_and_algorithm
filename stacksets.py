# 3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, 
# we would likely start a new stack when the previous stack exceeds some threshold. 
# Implement a data structureSetOf Stacks that mimics this. SetOf Stacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should be have identically to a single stack(that is,pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

from cc32 import Stack

class SetOfStacks:
	def __init__(self,threshold = 10):
		self.capacity = threshold
		self.stacks=[]
		self.stacks.append(Stack(threshold))
		self.current=0
		
	def Push(self,val):
		if self.stacks[self.current].isfull():
		 	self.stacks.append(Stack(self.capacity))
		 	self.current+=1 
		self.stacks[self.current].push(val)
	
	def Pop(self):
		while (self.stacks and self.stacks[self.current].isempty()):
			self.stacks.pop()
			self.current-=1
	
		if not self.stacks :
			print "SetOfStacks is empty .."
			return
		self.stacks[self.current].pop()
			
	def Top(self):
		while (self.stacks and self.stacks[self.current].isempty()):
			self.stacks.pop()
			self.current-=1		
		if not self.stacks :
			print "SetOfStacks is empty .."
			return
		return self.stacks[self.current].top()
	
	def Pop_at(self,which):
		if not self.stacks:
			print "SetOfStacks is empty ..."
			return
		if which > self.current or which < 0 :
			print " No such stack ..."
			return
		stack = self.stacks[which]
		stack.pop()

def main():
	stack = SetOfStacks(1)
	stack.Push(1)
	stack.Push(2)
	stack.Push(3)
	stack.Push(4)
	print stack.Top()
	stack.Pop_at(0)
	stack.Pop()
	stack.Pop()
	print stack.Top()
	stack.Pop()
	print len(stack.stacks)
	print stack.current
	print stack.stacks[stack.current].top()

if __name__ == "__main__":
	main()





				

