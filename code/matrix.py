

class Matrix():
	def __init__(self):
		table=[]


	def createTransitionMatrix(self,graph):
		""" create table of transitions were rows are states of graph and columns are inputs, that means edges 
		Table of transitions have next state in their fields
		Table of outputs have output for given edge in their field"""
		numRow = len(graph.lStates)
		#print(numRow)
		numCol = len(graph.listOfEdges)
		#print(numCol)

		table=[]
		col=[]

		for i in range(0,numRow):
			col=[]
			for j in range(0,numCol):
				try:
					col.append(graph.lStates[i].le[j].ns)
				except IndexError:
					col.append("0")
			table.append(col)
		#print(table)
		return table


	def createOutputMatrix(self,graph):
		""" create table of transitions were rows are states of graph and columns are inputs, that means edges 
		Table of transitions have next state in their fields
		Table of outputs have output for given edge in their field"""
		numRow = len(graph.lStates)
		#print(numRow)
		numCol = len(graph.listOfEdges)
		#print(numCol)

		table=[]
		col=[]

		for i in range(0,numRow):
			col=[]
			for j in range(0,numCol):
				try:
					col.append(graph.lStates[i].le[j].o)
				except IndexError:
					col.append("0")
			table.append(col)
		#print(table)		
		return table