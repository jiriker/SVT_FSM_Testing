""" main function for FMS homeworks for SVT subject at CTU FEE Prague 2016/2017


"""

""" IMPORTS """
import graph as gr
import matrix as ma
import stateSet as ss
import transitionSet as ts
import characterizationSet as cs


""" function used in main.py"""
def loadGraphData():
	""" load data in .csv file and """
	#graphData = open("data/test_data.csv").read().splitlines()
	#graphData = open("data/test_data_2.csv").read().splitlines()
	graphData = open("data/test_data_3.csv").read().splitlines()
	#graphData = open("data/g1A05A.csv").read().splitlines()
	return graphData




def main():
	# load data and create graph with networkx library
	data = loadGraphData()
	graph = gr.Graph()
	graph.createGraph(data)
	#print(graph.__dict__)

	# create transition table and output table 
	# rows are states
	# columns are edges 
	transitionMatrix = ma.Matrix().createTransitionMatrix(graph)
	outputMatrix =ma.Matrix().createOutputMatrix(graph)




	# names of sets should be the same as used in lecture 
	# create L set
	L = ss.StateSet().createStateSet(graph)
	# creat T set
	T = ts.TransitionSet().createTransitionSet(graph,L)

	# create W set - that is called characterization set if it can distinguish between any two states of automat 
	W = cs.CharacterizationSet().createCharacterizationSet(graph,outputMatrix,transitionMatrix)

	# create Z set - that is Input compose W union W for k = 1 
	Z = []

	
if __name__ == "__main__":
    
    main()
   