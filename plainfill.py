# Implement the paint fill function that one might see on many image editing programs. That is, given a screen (represented by a 2-dimensional array of Colors), a point, and a new color, fill in the surrounding area until you hit a border of that color.
def fillin(arr,m,n,x,y):
	arr[x][y]='*'
	if x > 1 and arr[x-1][y]==None:
		fillin(arr,m,n,x-1,y)
	if y > 1 and arr[x][y-1]==None :
		fillin(arr,m,n,x,y-1)
	if x < m-1 and arr[x+1][y]==None :
		fillin(arr,m,n,x+1,y)
	if y < n-1 and arr[x][y+1]==None :
		fillin(arr,m,n,x,y+1)

#another iterative method can be done by putting neighbors in to a queue

def main():
	arr = [[None for x in range(30)] for y in range(30)]
	fillin(arr,30,30,0,0)
	print arr
if __name__ == '__main__':
	main()

