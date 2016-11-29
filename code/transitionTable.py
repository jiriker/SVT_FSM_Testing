import characterizationSet
from tabulate import tabulate

class transitionTable():
	""" create transition table as in lecture, it is the first table used as seed for characterization set creation """
	def __init__(self):
		pass

	def createTransitionTable(self,graph,transitionMatrix, outputMatrix):
		print("\nCreating transition table for creation of set W\n") 
		header = ["GROUP","STATE","OUTPUT","NEXT STATE"]	
		lTable= []

		lGroup = self.createOutputGroup(graph,outputMatrix)

		for index, item in enumerate(graph.lStates):
			lTable.append([lGroup[index][0],item.cs,outputMatrix[stoi[item.cs]],transitionMatrix[stoi[item.cs]]])
		print(tabulate(lTable, headers=header))
		return lTable

	def createOutputGroup(self,graph,outputMatrix):
		""" find how many different lists are there in output table and make as much groups """
		lGroup=[]
		checked = []
		for e in outputMatrix:
			if e not in checked:
				checked.append(e)
		print(checked)
		ue = list(enumerate(checked))
		for i in range(0,len(outputMatrix)):
			for j in range(0,len(ue)):
				if outputMatrix[i] == ue[j][1]:
		 			lGroup.append( [ue[j][0]+1,outputMatrix[i]])
		

		# 		#print(tabulate(lGroup))		
		#print(tabulate(lGroup))
		return lGroup

	def createDictionary(self,pstoi,petoi):
		global stoi,etou
		stoi = pstoi
		etoi = petoi
		print(stoi)
		print(etoi)
