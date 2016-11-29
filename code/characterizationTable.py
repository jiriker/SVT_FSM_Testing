
from tabulate import tabulate 

class CharacterizationTable():
	""" create table for construction of W set as described in lectures 
		save all tables for making backtracking possible later """
	def __init__(self):
		print("Creating characterization table for creation of set W") 

	def rewriteTransitionTable(self,graph,transitionMatrix,outputMatrix,transitionTable):
		""" create P0 table from the transition table that groups group, state, output table and transition matrix!
		this is method for rewriting the table to P from were all other calculation is done
		for the next steps of P from, another method is needed
		TODO: make this alghoritm more generic """

		print("\nRewriting transition table. Creating first table P0\n")

		print("Edges : ",graph.listOfEdges)
		header = ["GROUP","STATE","NEXT GROUP"]	
		lTable= [] # output table
		lGroup= [] # next group table
		firstCol = [row[0] for row in transitionTable] # column with group numbers
		secCol = [row[1] for row in transitionTable] # state of graph list 
		for o in transitionTable: # create matrix of next group assignments for given state and edge 
			ltmp = []
			for i in o[3]:
				ltmp.append(firstCol[secCol.index(i)])
			lGroup.append(ltmp)

		# Create lTable
		for index, item in enumerate(transitionTable):
			lTable.append([transitionTable[index][0],
							transitionTable[index][1],
							lGroup[index]
							])
		print(tabulate(lTable, headers=header))
		return lTable


	def createCharacterizationTable(self,graph,transitionMatrix,outputMatrix,characterizationTable):
		""" take char table and make next on if there are still groups with more than one state"""
		group = [row[0] for row in characterizationTable] # column with group numbers
		state = [row[1] for row in characterizationTable] # state of graph list 
		nextGroup = [row[2] for row in characterizationTable] # next group of graph list 
		print(group)
		print(state)
		print(nextGroup)
		maxGroup = max(group)
		print(maxGroup)


		# get max number of index, get all groups that have more than one member
		from collections import Counter
		notUnique = [k for k,v in Counter(group).items() if v > 1]
		# find minimun of notUnique and in one step work only with that 
		minGroup= min(notUnique)
		lTable= []

		for index,item in enumerate(characterizationTable): 
			if item[0] in notUnique and item[0] == minGroup:
				lTable.append([item[0],
							   item[1],
							   item[2]
					])
				# go over output vector and if there is difference, than take the different one and make new group max+1 
				# look for all other ouput vectors that are the same as the new vector and put them in the new group, return new char table
				# and repeat until not unique list is empty, then stop execution 
				# TODO: make note which transtition makes the difference 

				# need just not unique rows of table, print table for debugging 

		header = ["GROUP","STATE","NEXT GROUP"]	
		print(tabulate(lTable, headers=header))

