
# Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e
# Result: nothing isreturned, but the new linked list looks like a- >b- >d->e

class Node:
	def __init__(self,val=None,Next=None):
		self.val = val
		self.Next = Next
	def __str__(self):
		return str(self.val)

# This is O(N) time, but it's not necessary
# def DeleteNode(c):
# 	prev = c
# 	cur =  c
# 	while cur.Next :
# 		cur.val = cur.Next.val
# 		prev=cur
# 		cur = cur.Next
# 	prev.Next = None

def DeleteNode (c):
	# since c is in the middle of the Linkedlist, it shouldn't be None, so does its next Node
	c.val = c.Next.val
	c.Next = c.Next.Next
	

def Print (root):
	if (root ==None):
		print "root is None"
		return
	while (root):
		print root
		root=root.Next

def Test():
	root = Node (0)
	prev = root
	for i in range (1,10):
		cur = Node (i)
		prev.Next=cur
		prev=cur
	print "Initial Linkedlist"
	Print (root)
	DeleteNode(root.Next)
	print "after DeleteNode"
	Print(root)

Test()