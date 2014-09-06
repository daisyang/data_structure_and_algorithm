# How would you design the data structures for a very large social network (Facebook,LinkedIn, etc)? 
# Describe how you would design an algorithm to show the connection, or path, between two people (e.g., Me -> Bob -> Susan -> Jason -> You).
class Person:
	def __init__(self,ID,Friendlist=[]):
		self.ID=ID
		self.Friendlist=Friendlist
	def __str__(self,):
		return str(self.ID)
	def Addfriends(self,friendid):
		self.Friendlist.append(friendid)

class Machine:
	max_personnb = 1000 # maximum number of people each machine can hold
	def __init__(self,ID):
		self.ID=ID
		self.PersonList=[None]* Machine.max_personnb

	def AddPerson(self,ind, person):
		if self.PersonList[ind] is not None:
			print "Position at " , ind , "at Machine ", self.ID, "is already occupied"
			return False
		self.PersonList[ind]=person
		return True

	def GetPerson(self,personid):
		return self.PersonList[personid]


class Server:
	count =50 # machine counts
	def __init__(self):
		self.machines=[]
		for i in range (Server.count):
			self.machines.append(Machine(i))
	
	def AddPerson(self,person):
		# id = person.ID
		# print "id : " , id
		which = person.ID / Server.count
		print "which: " , which
		machine = self.machines[which]
		machine.AddPerson(person.ID - which * Server.count,person)
		
	def GetPerson(self,personid):
		which,ind = divmod(personid, Server.count)
		machine = self.machines[which]
		print "machine.ID:" ,machine.ID
		person = machine.GetPerson(personid - which * Server.count)
		return person

def main():
	server = Server()
	for i in range (20):
		person = Person(i)
		server.AddPerson(person)
	
	# print server.machines
	for i in range(20):
		p = server.GetPerson(i)
		print "p is ", p


if __name__== '__main__':
	main()