# Given a matrix in which each row and each column is sorted, write a method to find an element in it.

# start from right diagonal...  
def search(arr,val):
	row = 0
	m = len(arr)-1
	col = n = len(arr[0])-1
	while (row <=m and col>=0):
		if val ==  arr[row][col]:
			return True
		if val > arr[row][col]:
			row+=1
		else:
			col-=1

	return False
def main():
	l= [ [1,2,3] for y in range (3)]
	l[1][:]=[4,5,6]
	l[2][:]=[7,8,9]
	print l
	print search2(l,5)

	
if __name__ == '__main__':
	main()

