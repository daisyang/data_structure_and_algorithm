# Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C

from LinkedList import *
def Detectcircle(root):
	if (root is None or root.next is None):
		return root
	slow = root
	fast = root
	
	while (slow and fast and fast.next):
		slow = slow .next
		fast = fast.next.next
		if slow == fast:
			return slow
	return None	

def FindFirstInloop(root):
	p= Detectcircle(root)
	if p is None:
		return None
	q = root
	while (q!=p):
		p=p.next
		q=q.next
	return p

def Test():
	l = LinkedList(0)
	for i in range (1,5):
		l.AddNode(i)

	last = l.last()
	last.next = l.root.next.next
	n = Detectcircle(l.root)
	print n
	m = FindFirstInloop(l.root)
	print m
Test()