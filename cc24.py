# 2.4 Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.

from LinkedList import *

#Use two dummy nodes, O(N)
def PartitionLinkedlist1(ll,x):
	root = ll.root
	if (root is None or root.next is None):
		return root
	dummy1 = Node(0)
	dummy2 = Node(0)
	dummy1.next = root
	prev = dummy1
	larger=dummy2
	current = root
	while current.next:
		if current.val < x:
			prev = prev.next
		else :
			prev.next =current.next
			larger.next=current
			larger=larger.next

		current = prev.next

	
	larger.next= None
	current.next = dummy2.next
	return dummy1.next


# partition O(N)
def swap (p,q):
	temp = p.val
	p.val= q.val
	q.val = temp

def PartitionLinkedlist2(ll,x):
	root = ll.root
	if (root is None or root.next is None):
		return
	current = root
	storeIndex = root
	while current:
		if (current.val < x) :
			swap (current,storeIndex)
			storeIndex= storeIndex.next
		current=current.next
	return root


def Test():
	ll = LinkedList(0)
	ll.AddNode(8)
	ll.AddNode(1)
	ll.AddNode(3)
	ll.AddNode(2)
	ll.AddNode(6)
	ll.AddNode(7)
	# ll.Print()
	ll.root = PartitionLinkedlist2(ll,5)

	ll.Print()
Test()