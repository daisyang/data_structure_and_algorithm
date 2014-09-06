# Write a function that adds two numbers. You should not use + or any arithmetic operators.
def add(a,b):
	if b ==0:
		return a
	total = a^b
	carry = (a&b)<<1
	return add(total,carry)

def main():
	s = add(6,100)
	print s

if __name__== '__main__':
	main()