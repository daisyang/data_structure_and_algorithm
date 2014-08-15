#Write code to remove duplicates from an unsorted linked list.
#FOLLOW UP
#How would you solve this problem if a temporary buffer is not allowed?

class Node:
	def __init__(self,val=None,next=None):
		self.val=val
		self.next=next
	def __str__(self):
		return str(self.val)


def Removedupicates_withbuffer(root):
	print "id is %s" , id(root)
	l = list()
	parent=Node()
	current = root
	while (current!=None):
		if not current.val in l:
			l.append(current.val)
		else:
			parent.next=current.next
		parent = current
		current=current.next
	return root


def Removeduplicates_nobuffer(root):
	p=root
	while p :
		parent = p
		q=p.next
		while q:
			if p.val == q.val:
				parent.next = q.next
			parent=q
			q=q.next
		p=p.next


def test():

	root = Node (3)
	print "id is %s" , id(root)
	parent= root
	print "--------input done -------"
	
	for i in range(0,10) :
		temp = Node(i)
		parent.next=temp
		parent= temp
		print temp.val

	#Removedupicates_withbuffer(root)
	Removeduplicates_nobuffer(root)

	while root is not None:
		print root.val
		root=root.next
