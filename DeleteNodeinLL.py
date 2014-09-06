
# Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e
# Result: nothing is returned, but the new linked list looks like a- >b- >d->e

class Node:
	def __init__(self,val=None,next=None):
		self.val = val
		self.next = next
	def __str__(self):
		return str(self.val)


def DeleteNode (c):
	# since c is in the middle of the Linkedlist, it shouldn't be None, so does its next Node
	c.val = c.next.val
	c.next = c.next.next
	

def Print (root):
	s = ""
	if (root ==None):
		print "root is None"
		return
	while (root):
		s+=str(root.val)
		root=root.next
	print "->".join(s)

def main():
	root = Node (0)
	prev = root
	for i in range (1,10):
		cur = Node (i)
		prev.next=cur
		prev=cur
	print "Initial Linkedlist"
	Print (root)
	d = root.next.next
	print "Delete node : " , d
	
	DeleteNode(d)
	print "After DeleteNode"
	Print(root)

if __name__ == "__main__":
	main()