import graph as gr
import itertools
from tabulate import tabulate
import transitionTable as tt
import characterizationTable as ct



class CharacterizationSet():
	def __init__(self):
		self.ctab = ct.CharacterizationTable()
		self.ttab = tt.transitionTable()
		pass

	def createCharacterizationSet(self,graph,outputMatrix,transitionMatrix):
		"""  L in right composition with ( input union "0" ) , letst call that U   """
		print("Creating characterization set - W set ")
		
		# first find out what states can be differentiate in one step
		# then two steps
		# and so on

		# differentitaon is made that for two states and given sequence, the output is different. 
		# make all pairs of states

		W = []
		self.createDictionary(graph)
		self.ttab.createDictionary(stoi,etoi)
		tranTab = self.ttab.createTransitionTable(graph,transitionMatrix,outputMatrix)
		charTab = self.ctab.rewriteTransitionTable(graph,transitionMatrix,outputMatrix,tranTab)
		charTab = self.ctab.createCharacterizationTable(graph,transitionMatrix,outputMatrix,charTab)
		#self.ctab.createFirstTable(graph,transitionMatrix)

		# lStatePair = self.createPair(graph.lStates)
		# self.createDictionary(graph)
		
		# #lSequences = self.createSequences(graph.listOfEdges,4)
		# #self.compareSequence("s00","s01",["ea","ea"],outputMatrix,transitionMatrix,W)

		# depth = 4 #  actual is -1 lower, indexing magic ... 
		# for i in range(1,depth):
		# 	# for multiple depths 
		# 	lSequences = self.createSequences(graph.listOfEdges,i)

		# 	# for all state pairs and all sequences 
		# 	for j in range(0,len(lStatePair)):
		# 		for k in range(0,len(lSequences)):
		# 			W = self.compareSequence(lStatePair[j][0],lStatePair[j][1],lSequences[k],outputMatrix,transitionMatrix,W)
					
		print(W)
		# for cycle : take all inputs e.g. ea, eb
		#		      take all pairs of inouts e.g. ea::ea, ea::eb e.t.c.
		# 			  take all triplets and so on. 
		# stop adding when for example triplet is make and no sequence is able to distinguish states 

 	
	def createPair(self,lStates):
		""" Create all pairs of states of graph"""
		print("Creating all state pairs for W set creation")
		tmp = []
		for i in lStates:
			for j in lStates:
				if i.cs != j.cs:
					if [j.cs,i.cs] not in tmp:
						tmp.append([i.cs,j.cs])
		print(tmp,"\n")
		return tmp


	def createSequences(self,inputs,depth):
		""" Create all combinations of sequences for given input list and depth, that means how many iterations we do. """
		print("Creating test sequences for depth ",depth)
		#print(inputs)

		tmp = []
		for i in inputs:
			tmp.append([i])
		# need inputs and starting tmp as list of lists 
		inputs = tmp

		# will do this recursively, define function for it here 
		def addNextLayer(tmp,inputs):
			innerTmp=[]
			for i in inputs:
				for j in tmp:
					innerTmp.append(i+j)
			return innerTmp

		#print(tmp)
		for i in range(1,depth):
			tmp=addNextLayer(tmp,inputs);

		print(tmp,"\n")
		# list of list of all sequences for current depth 
		return tmp
				
			

	# make function that takes state, graph and output table on return output of state 
	def compareSequence(self,s1,s2,sequence,outputMatrix, transitionMatrix,W):
		""" Compares two outputs for given sequence and given two states 
		s1 -state one
		s2 - state two
		sequence - list of edges to take 
		table - output table, rows states, column edge 
		return True if outputs are the same """
		# print("Comparing sequence ")
		# print(s1,s2,sequence)
		# print(outputMatrix)
		# print(transitionMatrix)
		hs1 = s1 # helper variable for indexing 
		hs2 = s2 # helper varibale for indexing 
		o1=[]
		o2=[]
		# tak current state, take sequence and make transition, save new state as current state, save output 
		for i in range(0,len(sequence)):
			# make transtition from state 1 over iths edge in sequence to new state and name it curS1
			#print(stoi[s1],etoi[sequence[i]])

			hs1 = transitionMatrix[stoi[s1]][etoi[sequence[i]]]
			hs2 = transitionMatrix[stoi[s2]][etoi[sequence[i]]]
			o1.append(outputMatrix[stoi[s1]][etoi[sequence[i]]])
			o2.append(outputMatrix[stoi[s2]][etoi[sequence[i]]])

			print(s1,o1,hs1,s2,o2,hs2)
			s1 = hs1
			s2 = hs2


			#print(s1,o1,s2,o2)
		
		if o1 == o2:
			# print(o1)
			# print(o2)
			# return true if outputs are the same 
			# if outputs are the same, check also if sequence is not already in W, because if it is, it has to be removew

			if sequence  in W:
				print("W: ",W)
				print("removing",sequence)
				W.remove(sequence)
			return W
		else:

			# print(o1)
			# print(o2)
			if sequence not in W:
				print("W: ",W)
				print("appending",sequence)
				W.append(sequence)
			return W





	def createDictionary(self,graph):
		""" create dictionary of states and edges, so table of output and transition can be reference easyly"""
		print("Creating dictionary for indexing in table ")
		tmp=[]
		for i in graph.lStates:
			tmp.append(i.cs)
		listOfEdges = list(enumerate(graph.listOfEdges))
		listOfStates = list(enumerate(tmp))
		
		global etoi,stoi
		lsi = [(item,index) for index,item in listOfEdges]
		#edge to integer
		etoi= dict(lsi)
		print(etoi)

		lsi = [(item,index) for index,item in listOfStates]
		#state to integer
		stoi= dict(lsi)
		print(stoi)

	
	


	def testCharacterizationSet(self):
		""" TODO: take transtition table and list of sequences and test that all states of the graph are achieveable """
		pass


