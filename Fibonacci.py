# Write a method to generate the nth Fibonacci number.
def Fibonacci1(n):
	if n ==1 or n ==2 :
		return 1
	return Fibonacci1(n-1) + Fibonacci1(n-2) 

def Fibonacci2(n):
	l=[1,1]
	for i in range(2,n):
		c = l[1]
		l[1] = l[0] + l[1]
		l[0] = c
	return l[1]

def main():
	val1 = Fibonacci1(10)
	val2 = Fibonacci2(10)
	print val1
	print val2
if __name__ == '__main__':
	main()
