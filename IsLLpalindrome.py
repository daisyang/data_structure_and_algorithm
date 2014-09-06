# Implement a function to check if a linked list is a palindrome.

class node:
	def __init__(self,val,next = None):
		self.val = val
		self.next =next

def reverse(head):
	if head is None or head.next is None:
		return head
	prev = head
	current = head.next
	while current :
		next = current.next
		prev.next = next
		current.next = head
		head= current
		current = next
	return head

def reverse2 (head):
	if head is None or head.next is None:
		return head
	dummy = node(0)
	dummy.next = head
	last = dummy
	pre = head
	p = pre.next
	while p:
		pre.next = p.next
		p.next = last.next
		last.next = p
		p = pre.next
	return dummy.next


def Middlenode (head):
	# need to consider if the LinkedList has odd number or even
	# 1 2 3 2 1
	#     s   f
	# 1 2 2 1
	#     s    f
	if head is None or head.next is None:
		return
	fast = head
	slow = head
	while fast and fast.next :
		fast = fast.next.next
		slow = slow.next
	if fast: # odd
		return slow.next
	else: #even
		return slow

def Ispalindrome (head):
	if head is None or head.next is None:
		return True
	middle = Middlenode(head)
	middle = reverse(middle)
	while (middle):
		if head.val != middle.val:
			return False
		middle = middle.next
		head = head.next
	return True

def printLL(p):
	s = ""
	while p:
		s+=str(p.val)
		p=p.next
	print '->'.join(s)
	
def main():
	l = [1,2,3,4]
	head = p = None
	for i in l:
		if head is None:
			head = p = node(i)
		else:
			p.next = node(i)
			p=p.next

	print "---original LinkedList---"
	printLL(head)
	# p = reverse2(head)
	# print "---reversed LinkedList---"
	# printLL(p)
	print Ispalindrome(head)
	
if __name__ == "__main__":
	main()