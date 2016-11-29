""" read .csv file with automat description and put it into graph data structure. That will be used for alghoritm application"""


class Edge():
	""" Edge has member variables:
	cs -> current state : string : edge starts here
	Edge does not have to have current state, because edge is part of State and it hold information about current state

	ns -> next state: string : edge ends here
	e  -> event : string : name of event that takes place 
	o  -> output: string : output symbol """
	def __init__(self,ns,e,o):
		self.ns=ns
		self.e=e
		self.o=o


class State(): 
	""" class State implements node of graph, it holds 
		cs: current state
		le : list of edges 
	"""
	def __init__(self,cs,le):
		""" """
		self.cs=cs
		self.le=le
		



class Graph():
	def __init__(self):
		print("Creating new instance of class Graph")
		self.entryState=State(None,None)
		self.exitState=State(None,None)
		self.defaultOutput=""
		self.listOfEdges=[]
		self.currentState=State(None,None)
		self.lStates=[]
		

	def createGraph(self,data):
		print("Starting the process of graph creation")
		self.parseData(data);

		# add state with list of edges to entry state 
		for s in self.lStates:
			if s.cs == self.entryState.cs:
				self.entryState=s
				# print(self.entryState.__dict__)
				# for e in self.entryState.le:
				# 	print(e.__dict__)

		# add state with list of edges to exit state 
		for s in self.lStates:
			if s.cs == self.exitState.cs:
				self.exitState=s
				# print(self.exitState.__dict__)
				# for e in self.exitState.le:
				# 	print(e.__dict__)
		
		

	def parseData(self,data):
		""" parse input data and create all states and edges and outputs  """
		print("Parsing input data")
		for s in data:
			ls = s.split(',')
			ls=' '.join(ls).split()
			while '' in ls:
				ls.remove('')
				

			# print(ls)
			# get entry state:
			
			# parse entry state
			if "entry" in ls:
				print("Entry state is "+str(ls[2]))
				self.entryState=State(ls[2],[])

			# parse exit state
			if "exit" in ls:
				print("Exit state is "+str(ls[2]))
				self.exitState=State(ls[2],[])

			if "default" in ls:
				print("Default output is "+str(ls[2]))
				self.defaultOutput=ls[2]

	
			if "current" in ls:
				for i in range(0,len(ls)):
					if ls[i].startswith("e"):
						if ls[2] != ls[i]  or i == 2:
							self.listOfEdges.append(ls[i])
						else:
							break
				print("list of edges is "+str(self.listOfEdges))

			# for every current state line create state with current state and edges 
			state = State("",[])
			if len(ls) is not 0 and ls[0].startswith("s"):
				
				j = 0
				for i in range(0,len(ls)):
					if i == 0:
						state.cs=ls[i]
					if i > 0 and ls[i].startswith("s"):
						edge = Edge(ls[i],self.listOfEdges[i-1],"")
						state.le.append(edge)
					if i > 0 and ls[i].startswith("o"):
						state.le[j].o=ls[i]
						#print(state.le[j].__dict__)
						j+=1

				#print(state.__dict__)
				self.lStates.append(state)
						
			






				
		

