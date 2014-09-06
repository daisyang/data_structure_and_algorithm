# Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n-pairs of parentheses.

# EXAMPLE:

# input: 3 (e.g., 3 pairs of parentheses)

# output: ((())), (()()), (())(), ()(()), ()()()

def helper(left,right,subl):
	if left==0 and right ==0:
		print "subl " ,subl
		return
	if left > 0:
		helper(left-1,right,subl+'(')
	if right > left:
		helper(left,right-1,subl+')')
	
def main():
	helper(3,3,'')
if __name__ == '__main__':
	main()