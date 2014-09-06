# Write a method that returns all subsets of a set.

def Getallsets(s,level,subl,l):
	if len(s) == level:
		return
	for i in range (level,len(s)):
		subl.append(s[i])
		l.append(list(subl))
		Getallsets(s,i+1,subl,l)
		subl.pop()


def main():
	l=[]
	l.append([])
	subl=list([])
	Getallsets([1,2,3],0,subl,l)
	print l
if __name__== '__main__':
	main()
