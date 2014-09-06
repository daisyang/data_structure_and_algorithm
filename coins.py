# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), 
# write code to calculate the number of ways of representing n cents.

def coins(val,opt):
	if val < 0:
		return 0
	if val ==0:
		return 1
	count1=count2=count3=count4=0
	
	if (opt>=25):
		count1= coins(val-25,25)
	if (opt>=10):
		count2= coins(val-10,10)
	if (opt>=5):
		count3= coins(val-5,5)
	if (opt>=1):
		count4= coins(val-1,1)
	# print count1+count2+count3+count4
	return count1+count2+count3+count4



def test():
	a=coins(100,5)
	print a
test()