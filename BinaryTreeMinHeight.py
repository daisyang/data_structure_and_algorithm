# Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.

from Node import *

from collections import deque

def BST(array,start, end):
	if (start>end):
		return None
	mid = start + (end-start)/2
	root = Node(array[mid])
	root.left = BST(array,start,mid-1)
	root.right = BST(array,mid+1,end)
	return root

def height(root):
	if not root:
		return 0
	return max(height(root.left),height(root.right))+1


def printBST(l):
	while l:
		root = l.popleft()
		print " root : %d" %root.val
		if root.left:
			l.append(root.left)
		if root.right:
			l.append(root.right)

def main():
	l=[1,2,3,4,5,6]
	root = BST(l,0,len(l)-1)
	h = height(root)
	print "height is ",h
	t=deque()
	t.append(root)
	printBST(t)

if __name__== '__main__':
	main()
