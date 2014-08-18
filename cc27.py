# Implement a function to check if a linked list is a palindrome.
from LinkedList import *

def reverse(root):
	if root is None or root.next is None:
		return root
	prev = root
	current = root.next
	while current :
		next = current.next
		prev.next = next
		current.next = root
		root= current
		current = next
	return root

def MiddleNode (root):
	# need to consider if the LinkedList has odd number or even
	if root is None or root.next is None:
		return
	fast = root
	slow = root
	while fast and fast.next :
		fast = fast.next.next
		slow = slow.next
	if fast:
		return slow.next
	else:
		return slow

def Ispalindrome (root):
	if root is None or root.next is None:
		return True
	middle = MiddleNode(root)
	middle = reverse(middle)
	while (middle):
		if root.val != middle.val:
			return False
		middle = middle.next
		root = root.next
	return True

def Test():
	l = LinkedList(1)
	l.AddNode(2)
	for i in range (1,5):
		l.AddNode(i)
	for i in range (5,-1,-1):
		l.AddNode(i)

	l.Print()	
	print Ispalindrome(l.root)
	print "----"
	l.Print()
Test()