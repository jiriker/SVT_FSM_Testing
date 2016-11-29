import graph as gr


class Node():
	def __init__(self,seq,par,stat):
		self.sequence=seq
		self.parent=par
		self.state=stat

class StateSet():
	def __init__(self):
		pass

	def createStateSet(self,graph):
		""" Take transition table and graph
		find set L, which enables you to go to any state of graph from state entry state
		using Breadth-first search alghorithm
		keep table of states that were already find
		table of all states that are in graph
		table of seque	in the end minimalize sequences and maybe check that all states can be found with minimalized sequences"""
		print("Creating set of states - L set ")




		
		Q = [] # create queue
		# create root node, root node is parent of itself, that protects it against sequence that is just loop from root to root 
		root=Node([],graph.entryState,graph.entryState)
		
		lNode=[]
		for s in graph.lStates:
			# entry state is in root, do not add it to list of nodes 
			if s.cs != graph.entryState.cs:
				lNode.append(Node([],gr.State(None,None),s))
		
		Q.append(root) # add entry state


		### Breadt first search BEGIN ALGORITHM
		while len(Q) != 0 :  # while there are still states in open state queue
			# take first item in queue
			current = Q.pop(0)

			# iterate over edges from current to next state, save all next states to queue
			#iterate over all nodes, that means all states in graph
			for n in lNode:
				
				# iterate over all edges that go out from current state
				for ns in  current.state.le:
					
					# if current state has edge that ends in node n , that is being iterated over 
					if ns.ns == n.state.cs:
						if n.parent.cs == None:
							n.parent=current.state
							n.sequence += (current.sequence)
							n.sequence.append(ns.e)
							Q.append(n)
						#print(ns.__dict__)
						#print(n.state.__dict__,n.__dict__)
		### END OF ALGORITHM	

		# "0" is empty input 
		lSequences = []
		for n in lNode:
			lSequences.append(n.sequence)
			# print(n.sequence)
			# print("parent" , n.parent.__dict__)
			# print("state" , n.state.__dict__)
		print("\nSet L of current graph is : ")
		print(lSequences,"\n")
		return lSequences

	def testStateSet(self,lSequences,table):
		""" TODO: take transtition table and list of sequences and test that all states of the graph are achieveable """
		pass