#2.2 Implement an algorithm to find the kth to last element of a singly linked list.

class Node:
	def __init__(self,val=None,Next=None):
		self.val = val
		self.Next=Next
	def __str__(self):
		return str(self.val)


def FindlastK(root,K):
	if (root==None):
		return rot
	fast = root
	slow = root

	# Make sure K is not larger than the length of the linked list
	for i in range (0,K):
		if fast is None:
			return None
		fast=fast.Next
		
	while (fast):
		fast=fast.Next
		slow=slow.Next
	return slow

def Print (root):
	if (root ==None):
		print "root is None"
		return
	while (root):
		print root
		root=root.Next


def main():
	print "start in here "
	root = Node (0)
	prev = root
	for i in range (1,10):
		cur = Node (i)
		prev.Next=cur
		prev=cur
	print "initial linked list"
	Print(root)
	k = 10
	newroot = FindlastK(root,k)
	print "last, " , k , " :" , newroot
	
if __name__ == "__main__":
	main()


