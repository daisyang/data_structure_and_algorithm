# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

from Node import *
def Isparent (root,node):
	if not root:
		return False
	if root is node:
		return True
	return Isparent(root.left,node) or Isparent(root.right,node)


# top - down iterative
def first_ancestor1(root,p,q):
	if not root:
		return None
	if not (Isparent(root,p) and Isparent(root,q)):
		return None
	current = root
	while current:
		if Isparent(current.left,p) and Isparent(current.left,q):
			current = current.left
		elif Isparent(current.right,p) and Isparent(current.right,q):
			current = current.right
		else:
			break

	return current

# top - down recursive
def first_ancestor2(root,p,q):
	if not root:
		return None
	if Isparent(root.left,p) and Isparent(root.left,q):
		return first_ancestor2(root.left,p,q)
	elif Isparent(root.right,p) and Isparent(root.right,q):
		return first_ancestor2(root.right,p,q)
	else:
		return root


# bottom - up
def first_ancestor3 (root,p,q):
	if not root:
		return None
	if root is p or root is q:
		return root

	left = first_ancestor3(root.left,p,q)
	right = first_ancestor3(root.right,p,q)
	
	if left and right:
		return root

	return left if left else right

# Node has a parent link, iterative
def getheight(p):
	height = 0
	while p:
		height+=1
		p= p.parent
	return height

def first_ancestor4(root,p,q):
	lheight = getheight(p)
	rheight = getheight(q)
	if rheight > lheight:
		for i in range (0, rheight-lheight):
			q = q.parent
	if lheight > rheight:
		for i in range (0, lheight-rheight):
			p = p.parent
	while p and q:
		if p is q:
			return p
		p= p.parent
		q =q.parent
		
	return None


def main():
	root =Node(1)
	root.left = Node(2,root)
	root.right = Node(3,root)
	root.left.left=Node(4,root.left)
	root.left.left.right=Node(5,root.left.left)
	node = first_ancestor4(root, root.left,root.right)
	print node.val

if __name__ == '__main__':
	main()
