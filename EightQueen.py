# Write an algorithm to print all ways of arranging eight queens on a chess board so that none of them share the same row, column or diagonal.

n = 8

def printqueens(l):
	for i in range (n):
		str=""
		for j in range(n):
			if j==l[i]:
				str+="Q"
			else:
				str+="x"
		print str
	print "-----------"

def search(r,l):
	if (r == n-1):
		printqueens(l)
		return
	for i in range (n):# each column
		l[r] = i
		ok = True
		for j in range(r): #check element before r since we haven't reached to rows that are > r
			if  l[r]==l[j] or r-j ==abs(l[r]-l[j]):
				ok = False
				break
		if ok:
			search(r+1,l)
		
		

def main():
	l=[0] * 8
	search(0,l)

if __name__ == '__main__':
	main()

