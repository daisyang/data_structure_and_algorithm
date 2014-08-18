# 3.1  Describe how you could use a single array to implement three stacks.
class Stacks:
	def __init__(self,size):
		if (size<3):
			size = 3
		self.arr = size*[None]
		self.bottom = [int(size/3)-1,int(size/3*2)-1,size-1]
		self.top = [0,self.bottom[0]+1,self.bottom[1]+1]
		self.Index = [-1,self.bottom[0],self.bottom[1]]

	def Push(self, which,val):
		which = which-1
		self.Index[which]+=1
		if (self.Index[which] > self.bottom[which]):
			self.Index[which]-=1
			print "Stack %d is full ..." %(which+1)
			return False
		self.arr[self.Index[which]]= val
		print "Pushed %s to the Statck %s "  %(val, which+1)
		
		return True
	def Pop (self,which):
		which = which -1
		self.Index[which]-=1
		if (self.Index[which] < self.top[which] - 1 ):
			self.Index[which]+=1
			print "Stack %d is empty ..." %(which+1)
			return False
		print "Poped out from the Statck %s "  %(which+1)
		return True

	def Top(self,which):
		which-=1
		return self.arr[self.Index[which]]

	def Size(self,which):
		which-=1
		return self.bottom[which] - self.Index[which]
def Test(): 

	s = Stacks(30)
	s.Push(1,2)
	print s.Top(1)
	print s.Size(3)

Test()