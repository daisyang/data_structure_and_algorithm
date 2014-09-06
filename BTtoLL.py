# Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (i.e., if you have a tree with depth D, you will have D linked lists)

class Node:
	def __init__(self,val,left=None,right=None,next=None):
		self.val = val
		self.left = left
		self.right = right
		self.next = next
	def __str__(self):
		return str(self.val)

def BTtoLL(root):
	d={}
	level = 0
	d[level]=root
	while d[level]:
		head = d[level]
		newhead=None
		pre = None
		while head:
			if head.left:
				if not newhead:
					newhead=head.left
					pre = newhead
				else:
					pre.next = head.left
					pre = pre.next
			if head.right:
				if not newhead:
					newhead=head.right
					pre = newhead
				else:
					pre.next = head.right
					pre = pre.next
			head = head.next
		level+=1
		d[level]=newhead
	# d.pop(level,None)
	return d


def BTtoLL2(root,d={},level=0):
	if not root: 
		return
	if level not in d:
		d[level]=root
	else:
		p = d[level]
		while p.next:
			p=p.next
		p.next = root
	if root.left:
		BTtoLL2(root.left,d,level+1)
	if root.right:
		BTtoLL2(root.right,d,level+1)

def main():
	root = Node(1)
	root.left = Node(2)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right = Node(6)
	root.right.left= Node(7)	
	root.right.right= Node(8)
	# d={}
	# BTtoLL2(root,d,0)
	d = BTtoLL(root)
	for k in range(len(d)):
		print "level : " , k
		v = d[k]
		while v:
			print v
			v = v=v.next

if __name__ =="__main__":
	main()



