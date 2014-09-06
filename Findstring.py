# Given a sorted array of valings which is interspersed with empty valings, write a method to find the location of a given valing.
# Example: find 'ball' in ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''] will return 4
# Example: find 'ballcar' in ['at', '', '', '', '', 'ball', 'car', '', '', 'dad', '', ''] will return -1

def Stringlocation(l,left,right,val):
	if val is None:
		return -1
	
	if left > right:
		return -1	
	mid = int(left+right)/2
	print "mid" , mid, l[mid]
	while l[mid]=='' and mid<right:
		mid+=1

	if mid == right:
		while l[mid]=='' and mid >left:
			mid-=1
	print "change mid to" , mid,l[mid]
	
	if l[mid]=='':
		return -1

	if val == l[mid]:
		return mid	
	elif val < l[mid]:
		print "checking " ,left,mid-1
		return Stringlocation(l,left,mid-1,val)
	else:
		print "checking " ,mid+1,right
		return Stringlocation(l,mid+1,right,val)

#iterative
def Stringlocation2(l,val):
	first = 0
	last = len(l)-1
	while (first<=last):
		while first <=last and l[last]=='':
			last-=1

		if (first > last):
			return -1
		mid = (first+last)/2
		print "mid:" , mid
		while (l[mid] ==''): #since last is larger than mid and last has a value, so mid won't go out of the array
			mid+=1
		print "change mid to " , mid, l[mid]
		if l[mid]==val:
			return mid

		if val < l[mid]:
			last = mid-1
		else:
			first = mid+1
	return -1	

def main():
	l=['at', 'az', '', '', 'ball', '', '', 'car', '', '', 'dad', '', 'g'] 
	l=['at', '','','', 'g'] 
	
	# index = Stringlocation(l,0,len(l)-1,'c')
	index = Stringlocation2(['at','','','v','c'],'at')
	print "answer :" ,index

if __name__ == '__main__':
	main()