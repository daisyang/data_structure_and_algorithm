# A circus is designing a tower routine consisting of people standing atop one another s shoulders. For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method to compute the largest possible number of people in such a tower.
# EXAMPLE:
# Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
# Output: The longest tower is length 6 and includes from top to bottom: (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)

# dynamicprogramming

			
def towerdesign(l):
	l.sort(reverse=True)
	print l 
	o = [None] * len(l)
	o[0] = 1
	for i in range (1,len(l)):
		key ,value = l[i]
		max_seq = o[i-1]
		for j in range (0,i):
			k,val = l[j]
			if (key <k) and (value < val):
				max_seq=max(max_seq,o[j]+1)
		o[i]= max_seq
	return o

def test():
	l=[(65, 100) ,(70, 90), (56, 90), (75, 190), (60, 95) ,(68, 110)]
	o = towerdesign(l)
	print o

			
test()



