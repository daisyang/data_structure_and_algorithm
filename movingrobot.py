# Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot?

# FOLLOW UP

# Imagine certain squares are off limits, such that the robot can not step on them. 
#Design an algorithm to get all possible paths for the robot.

#recursive
def move1 (x,y):
	if x==1 or y == 1:
		return 1
	return move1(x-1,y) + move1(x,y-1)
#DP
def move2(m,n):
	matrix = [[1 for i in xrange(m)] for i in xrange(n)]
	for i in range (1,m):
		for j in range(1,n):
			matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
	return matrix[m-1][n-1]

#FOLLOW UP
def move3(block,m,n):
	matrix = [[0 for i in xrange(m)] for i in xrange(n)]
	matrix[0] = [1 for i in xrange(n)]
	for i in xrange(m):
		matrix[i][0] = 1

	for i in range (1,m):
		for j in range(1,n):
			if not block[i-1][j]: # if no block
				matrix[i][j] += matrix[i-1][j]
			if not block[i][j-1]:
			 	matrix[i][j] += matrix[i][j-1]
	return matrix[m-1][n-1]
	


def main():
	val = move2(3,3)
	print val

if __name__ == '__main__':
	main()
#DP
# def move2(x,y,n):



