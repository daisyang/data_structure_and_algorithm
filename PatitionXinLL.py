# 2.4 Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.

class Node:
	def __init__(self,val,next=None):
		self.val= val
		self.next = next
	def __str__(self):
		return str(self.val)


#Use two dummy nodes, O(N)
def PartitionLinkedlist1(head,x):
	if (head is None or head.next is None):
		return head
	dummy1 = Node(0)
	dummy2 = Node(0)
	dummy1.next = head
	prev = dummy1
	larger=dummy2
	current = head
	while current.next:
		if current.val < x:
			prev = prev.next
		else :
			prev.next =current.next
			larger.next=current
			larger=larger.next

		current = prev.next

	# Remember to replace the next pointer of the last larger element to None !!!
	larger.next= None
	current.next = dummy2.next
	return dummy1.next

# partition O(N) if swapping values is allowed
def swap (p,q):
	temp = p.val
	p.val= q.val
	q.val = temp

def PartitionLinkedlist2(head,x):
	if head is None:
		return head
	current = head
	storeIndex = head
	while current:
		if current.val < x :
			swap (current,storeIndex)
			storeIndex= storeIndex.next
		current=current.next
	return head


# Inspired by other people
def PartitionLinkedlist3(head,x):
	
	# dummy is small than x
	dummy = Node(x-1)
	dummy.next =head
	pre = last = p = dummy
	#find the the first element larger than x
	while p and p.val < x:
		pre = p
		p = p.next

	# all the elements are smaller than x
	if p is None:
		return head
	
	last = pre
	while p:
		if p.val < x:
			pre.next = p.next
			p.next = last.next
			last.next = p
			last = p
			p = pre.next
		else:
			pre = p
			p = p.next

	return dummy.next
	

	
def main():
	head = p = Node(0)
	l = [8,1,3,2,6,7,9,0]
	s =str(head.val)
	for i in l:
		p.next = Node(i)
		p = p.next
		s+=str(i)
	print '->'.join(s) 


	head = PartitionLinkedlist3(head,5)
	s2=""
	while head:
		s2+= str(head.val)
		head = head.next
	print '->'.join(s2)

if __name__ == "__main__":
	main()