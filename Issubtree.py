# You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes. 
# Create an algorithm to decide if T2 is a subtree of T1

from Node import *
def helper(p,q):
	if not p and not q:
		return True
	if not p or not q :
		return False

	if p.val == q.val:
		return helper(p.left,q.left) and helper(p.right,q.right)
	
	return helper(p.left,q) or helper(p.right,q)

def Issubtree(p,q):
	if not q:
		return True
	return helper(p,q)

def main():
	root1 = Node(0)
	root1.left = Node(1)
	root1.right = Node(2)
	root1.left.left = Node(3)
	root1.left.right = Node(4)
	
	root2 = Node (3)
	# root2.left = Node(1)
	# root2.right = Node(4)
	check = Issubtree(root1,root2)
	print check
if __name__ == '__main__':
	main()