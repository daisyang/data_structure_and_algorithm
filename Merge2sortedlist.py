# You are given two sorted arrays, A and B, and A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.
def Merge(a,b,m,n):
	if b is None:
		return a
	ind1 = m -1
	ind2 =n -1
	ind = ind1+ind2+1
	while (ind>=0):
		if ind1 >=0 and a[ind1] > b[ind2]:
			a[ind]=a[ind1]
			ind1-=1
		else:
			a[ind]=b[ind2]
			ind2-=1
		ind-=1
	return a

def test():
	a=[-2,2,3,4,5,0,0,0,0]
	b=[-4,-3,-2,10]
	a=Merge(a,b,5,4)
	print a
test()

