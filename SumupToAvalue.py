# You are given a binary tree in which each node contains a value. Design an algorithm to print all paths 
# which sum up to that value. Note that it can be any path in the tree - it does not have to start at the root.

# # question of this one:
# 0
# /\
# 1 2
# /\
# 3 4
# does 3-1-4 path count?
# http://hawstein.com/posts/4.8.html it seems like only consider straight path but not something like 3-1-3

def Printpath(root,val):
	if not root:
		return


def helper (root,val,l):	
	if not root:
		return 
	helper(root.left,val,l)
	if (root.val + sum(l) + val==0):
		Print2(l)
	elif root.val+sum(l) > val:
		l.clear()
	else:
		l.append(root)

	helper(root.right,val,lh)

	