# Given a sorted array of n integers that has been rotated an unknown number of times, give an O(log n) algorithm that finds an element in the array. You may assume that the array was originally sorted in increasing order.
# EXAMPLE:
# Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
# Output: 8 (the index of 5 in the array)
def FindvalueinRotatedarr(l,val,left,right):
	if left > right:
		return None
	mid = int((left+right)/2)
	if val == l[mid]:
		return mid
	if l[left] < l[mid]: 
		if val >= l[left] and val < l[mid]: # make sure to include boundaries
			return FindvalueinRotatedarr(l,val,left,mid-1)
		else:
			return FindvalueinRotatedarr(l,val,mid+1,right)
	else:
		if val >l[mid] and val <= l[right]:
			return FindvalueinRotatedarr(l,val,mid+1,right)
		else:
			return FindvalueinRotatedarr(l,val,left,mid-1)

def main():
	l=[15,16 ,19 ,20 ,25 ,0 ,1 ,3, 4, 5, 7, 10, 14]
	for i in l:
		a= FindvalueinRotatedarr(l,i,0,len(l)-1)
		print a
if __name__ == '__main__':
	main()