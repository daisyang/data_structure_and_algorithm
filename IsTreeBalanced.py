# Implement a function to check if a tree is balanced. For the purposes of this question
# a balanced tree is defined to be a Node such that no two leaf nodes differ in distance from the root by more than one.

from Node import *
def max_distance(root):
	if not root:
		return 0
	left_val = max_distance(root.left)
	right_val = max_distance(root.right)
	return max(left_val,right_val)+1

def min_distance(root):
	if not root:
		return 0
	return min(min_distance(root.left),min_distance(root.right))+1

def IsBalanced(root):
	max_val = max_distance(root)
	min_val = min_distance(root)
	return max_val-min_val <=1

def main():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(2)
	node1 = root.left
	node2 = root.right
	node1.left = Node(3)
	node1.left.left = Node(3)
	val = IsBalanced(root)
	print val
if __name__ == '__main__':
	main()