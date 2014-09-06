import random
def shuffle(arr):
	if arr is None:
		return
	m = len(arr)
	print m
	for i in range(m-1,0,-1):
		temp = arr[i]
		j = random.randrange(0,i+1)
		print j
		arr[i] = arr[j]
		arr[j] = temp

def test():
	arr = [1,2,3,4,5]
	shuffle(arr)
	print arr

test()