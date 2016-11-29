import graph as gr
import itertools

class Node():
	def __init__(self,seq,par,stat):
		self.sequence=seq
		self.parent=par
		self.state=stat

class TransitionSet():
	def __init__(self):
		pass

	def createTransitionSet(self,graph,lSequences):
		"""  L in right composition with ( input union "0" ) , letst call that U   """
		print("Creating transtition set from U and L sets")
		U = graph.listOfEdges
		L = lSequences
		# remove "0" so it does not play role in composition, add it in the and to result again 
		#L.remove(["0"])
		#print(U)
		#print(L)

		T = self.compose(L,U)
		return T

	def compose(self,L,U):
		print("Creating composition from sets U and L ")
		T = []
		""" Lets do combination of every element with every element and then remove duplicities
		maybe in the end order them by length of sequence """

		for l in L:
			for u in U:
				# just create all combinations 
				T.append(l+[u])
				# remember to also add just members from input, duplicities will be deleted 
				T.append([u])
		#print(T)
		# remember to add zero input 
		#T += [["0"]]

		# remove duplicties 
		# sort alphabetically
		T.sort()
		# filter duplicates 
		T = list(T for T,_ in itertools.groupby(T))	
		# and sort by len after
		T.sort(key=len)
	
		print("\nSet T of current graph is : ")
		print(T,"\n")
		
		return T


	def testTransitionSet(self,lSequences,table):
		""" TODO: take transtition table and list of sequences and test that all states of the graph are achieveable """
		pass