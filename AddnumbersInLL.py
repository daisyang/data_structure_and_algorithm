# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the Ts digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295.
# Output: 2 -> 1 -> 9.That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
# Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295.
# Output: 9 -> 1 -> 2.That is, 912.

class node:
	def __init__(self,val,next = None):
		self.val=val
		self.next=next

def AddLinkedlist(head1,head2):
	current1 = head1
	current2 = head2
	output = node(0)
	last = output
	carry = 0
	while (current1 is not None and current2 is not None):
		val=current1.val+current2.val+carry
		last.next = node(val%10)
		carry = int (val/10)
		last = last.next
		current1 = current1.next
		current2 = current2.next
	
	#Remember carry
	while current1 :
		val = current1.val + carry
		last.next = node(val%10)
		carry = int(val/10)
		current1=current1.next
		last = last.next

	while current2:
		val = current2.val + carry
		last.next = node (val%10)
		carry = int(val/10)
		current2= current2.next
		last = last.next	
	# don't forget the last carry !!
	if (carry):
		last.next = node (carry)
	return output.next


#Follow up, forward order 
def Sumup(node1,node2):
	if node1 is None or node2 is None : return 0
	carry = Sumup (node1.next,node2.next)
	val = node1.val + node2.val + int(carry)
	node1.val = val%10
	return val/10  

def length(node):
	count = 0
	while node:
		count+=1
		node = node.next
	return count

def Addnodes (head, count):
	for i in range (0,count):
		newhead=node(0)
		newhead.next = head
		head = newhead
	return head

def AddLinkedlist2 (head1,head2):
	len1 = length(head1)
	len2 = length(head2)
	if len1 > len2 :
		head2 = Addnodes(head2,len1-len2)
	else:
		head1 = Addnodes(head1,len2-len1)
	
	carry = Sumup(head1,head2)
	if carry:
		newhead = node(carry)
		newhead.next = head1
		head1=newhead
	return head1

def main():
	t1 = p = node(7)
	for i in range(6,9):
		p.next =node(i)
		p=p.next
	t2 = q = node(1)
	for i in range(2):
		q.next =node(i)
		q=q.next
	
	newhead = AddLinkedlist(t1,t2)
	s = ""
	while newhead:
		s+=str(newhead.val)
		newhead=newhead.next
	print '->'.join(s)

if __name__=="__main__":
	main()

