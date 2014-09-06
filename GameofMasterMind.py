def mastermind(solution,guess):
	hits = 0
	for i in range(len(solution)):
		if solution[i]==guess[i]:
			hits+=1
	
