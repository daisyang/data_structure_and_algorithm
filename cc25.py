# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the Ts digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295.
# Output: 2 -> 1 -> 9.That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
# Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295.
# Output: 9 -> 1 -> 2.That is, 912.

from LinkedList import *

def AddLinkedlist(root1,root2):
	current1 = root1
	current2 = root2
	output = Node(0)
	result = output
	carry = 0
	while (current1 is not None and current2 is not None):
		val=current1.val+current2.val+carry
		result.next = Node(val%10)
		carry = int (val/10)
		result = result.next
		current1 = current1.next
		current2 = current2.next

	while current1 :
		val = current1.val + carry
		result.next = Node(val%10)
		carry = int(val/10)
		current1=current1.next

	while current2:
		val = current2.val + carry
		result.next = Node (val%10)
		carry = int(val/10)
		current2= current2.next	
	# don't forget the last carry !!
	if (carry):
		result.next = Node (carry)
	return output.next

def Sumup(node1,node2):
	if node1 is None or node2 is None : return 0
	carry = Sumup (node1.next,node2.next)
	val = node1.val + node2.val + int(carry)
	node1.val = val%10
	return val/10  

def length(node):
	count = 0
	while node:
		count+=1
		node = node.next
	return count

def Addnodes (node, count):
	for i in range (0,count):
		newhead=Node(0)
		newhead.next = node
		node = newhead
	return node

def AddLinkedlist2 (root1,root2):
	len1 = length(root1)
	len2 = length(root2)
	if len1 > len2 :
		root2 = Addnodes(root2,len1-len2)
	else:
		root1 = Addnodes(root1,len2-len1)
	
	carry = Sumup(root1,root2)
	if carry:
		newhead = Node(carry)
		newhead.next = root1
		root1=newhead
	return root1

def Test():
	# l = LinkedList(7);
	# l.AddNode(1)
	# l.AddNode(6)
	# r = LinkedList(5)
	# r.AddNode(9)
	# r.AddNode(8)

	# result = AddLinkedlist(l.root,r.root)
	# while result:
	# 	print result
	# 	result = result.next

	t1= Node(7)
	t1.next =Node(9)
	t2= Node(1)
	t2.next=Node(4)
	# t2.next.next=Node(9)
	
	newhead = AddLinkedlist2(t1,t2)
	while newhead:
		print newhead
		newhead=newhead.next

Test()

