#Write code to remove duplicates from an unsorted linked list.
#FOLLOW UP
#How would you solve this problem if a temporary buffer is not allowed?

class Node:
	def __init__(self,val=None,next=None):
		self.val=val
		self.next=next
	def __str__(self):
		return str(self.val)


def Removedupicates_withbuffer(head):
	d = dict()
	pre = head
	current = pre.next
	while (current is not None):
		if not current.val in d:
			d[current.val]=current
			pre.next = current
			pre = current
			
		current=current.next
	return head

def Removeduplicates_nobuffer(head):
	p=head
	while p :
		parent = p
		q=p.next
		while q:
			if p.val == q.val:
				parent.next = q.next
			parent=q
			q=q.next
		p=p.next
	return head


def main():
	head =parent = Node(0)
	l=[1,2,3,2,1,4,5,3,2,6]
	for i in range(len(l)):
		temp = Node(l[i])
		parent.next=temp
		parent= temp
		p = head
	while p is not None:
		print p.val
		p=p.next

	print "--- Input Done ---"
	head = Removedupicates_withbuffer(head)
	# head = Removeduplicates_nobuffer(head)
	while head is not None:
		print head.val
		head=head.next
	
if __name__ == "__main__":
	main()