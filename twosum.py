# Design an algorithm to find all pairs of integers within an array which sum to a specified value.
# nlogn
def Find2Sum(l,val):
	if l is None:
		return
	l.sort()
	out=[]
	k = 0
	j = len(l) -1 
	while (k < j):
		if l[k]+l[j]==val:
			out.append((l[k],l[j]))
			k+=1
			j-=1
		elif l[k]+l[j] < val:
			k+=1
		else:
			j-=1 
	return out

#n
def Find2Sum2(l,val):
	d = {}
	out = []
	for element in l:
		if d.get(element) is None:
			d[val - element] = element
		else:
			out.append((d[element], element)) 
	return out
def main():
	l=[7,5,6,4,3,1,2,8]
	out = Find2Sum2(l,8)
	for k,j in out:
		print k , j
if __name__ == '__main__':
	main()
