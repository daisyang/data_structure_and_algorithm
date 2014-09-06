# Write a method to count the number of 2s between 0 and n.
def howmanyIs(val,number):	
	cur = low = high=ans=0
	factor = 1
	while val/factor > 1 :
		low = val - (val/factor)*factor
		cur = (val/factor) % 10
		high = val/(10*factor)
		if  cur < number:
			ans+=high*factor
		elif cur == number:
			ans+=high*factor+1
		else:
			ans +=(high+1)*factor
		factor*=10

	return ans


def main():
	n=howmanyIs(1012,2)
	print n
if __name__ == '__main__':
	main()