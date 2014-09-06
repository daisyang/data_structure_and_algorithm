# Write a program to sort a stack in ascending order. You should not make any assumptions about how the stack is implemented. 
# The following are the only functions that should be used to write this program: push | pop | peek | isEmpty.

from cc32 import *
def SortStack(s):
	s_aux = Stack()
	while (not s.isempty()):
		temp = s.top()
		s.pop()	
		while ( not s_aux.isempty() and temp > s_aux.top()):
			s.push(s_aux.top())
			s_aux.pop()
			
		s_aux.push(temp)
	return s_aux

def Test():
	s = Stack()
	s.push(100)
	s.push(3)
	s.push(4)
	s.push(7)
	s.push(8)
	s.push(1)
	s.push(9)
	s.push(8)
	s.push(7)
	s.push(6)
	s_aux = SortStack(s)
	while (not s_aux.isempty()):
		print s_aux.top()
		s_aux.pop()
Test()



		
