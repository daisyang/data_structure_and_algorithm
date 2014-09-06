# you are given an array of integers (both positive and negative). Find the continuous sequence with the largest sum. Return the sum.
import sys
def max_sum(l):
	current = 0
	max_val = -sys.maxint - 1
	for i in range(len(l)):
		if current <= 0:
			current = l[i]
		else:
			current = current + l[i]

		if max_val < current:
			max_val=current



