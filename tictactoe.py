# Design an algorithm to figure out if someone has won in a game of tic-tac-toe.

def HasWon(l):
	won = False
	m= len(l)
	for i in range(m):
		for j in range(1,m):
			if (l[i][j-1] == l[i][j]) or (l[j-1][i] == l[j][i]):
				won = True
			else:
				won = False
				break
		if won:
			return True

	for i in range(1,m):
		if l[i-1][i-1] == l[i][i] or l[i-1][m-i]==l[i][m-i-1] :
			won = True
		else:
			won = False
			break
	return won

def main():
	# l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	# l[0][:] = [0,0,0,0]
	# # for i in range(4):
	# 	l[i][i]=0
	l = [[2,2,1],[2,1,1,],[1,2,0]]
	won = HasWon(l)
	print won

if __name__ == '__main__':
	main()





