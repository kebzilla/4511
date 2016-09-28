# This example is a simplistic "puzzle" in which the objective is to fill an nxn grid
# such that each row and column contains exactly 1 instance of each of the numbers 1-n.
# It is a demonstration of how to code a puzzle solver using a generic BFS framework.

from copy import deepcopy

from helper import permute
from bfs import *

class UF1problem(object):
	def __init__(self, initial, size, goal=None):
		# These values are specific to the problem you are solving (i.e. sudoku, nQueens, ...)
		self.size = size
		self.initial = initial
		self.goal = goal

		# For this example, an action is the assignment of an entire row
		# thus, the set of legal actions for all states is all permutations of viable numbers
		# Example: [[1,2,3],[1,3,2],[2,1,3],...]
		self.actions = permute( [ i for i in range(1,size+1) ] )

	def getActions( self, state ) :
		# Because all actions are legal for this example, they were generated once
		# in init, then are passed along here.
		# It might be that you generate only legal actions here, OR you generate all
		# actions, then test for legality in applyAction()
		if ( self.size == len(state) ):
			return []
		return self.actions

	def applyAction ( self, state, action ) :
		# It is very important that you generate a new variable with deepcopy for the new state
		# This code is problem specific. An action is applied by adding the configured
		# row (a permutation of numbers) to the state.
		newState = deepcopy(state)
		newState.append(action)
		return newState

	def isGoal ( self, state ):
		# Again, problem specific code.

		# If the state is empty, not done yet
		if not state:
			return False

		# If all rows have not yet been filled, not done yet
		if len(state) < self.size:
			return False

		# We have a completely filled in board. Check if there are any
		# duplicates across columns (our actions were defined such that duplicates
		# never appear in a given row)
		for col in range(self.size):
			if len( list(set([ row[col] for row in state ] ) )) < self.size :
				#print('State ',state,' not goal')
				return False

		# If we got here, the board is complete and legal
		print('WINNER')
		for i in range(self.size):
			boardrow = ''
			for j in range(self.size):
				boardrow += '   '+str(state[i][j])
			print(boardrow)
		return True

if __name__ == "__main__" :
	BFS(UF1problem([],4))

def testv1():
	# This is testing code. Currently it only tests 2 methods, but ideally, there should be a test
	# for each method. Many IDEs provide a test framework that makes this a lot easier,
	# but you can always create your own

	n = 3
	p = UF1problem([],n)

	# ------  TESTING getActions() --------------------
	answer = permute( [ i for i in range(1,n+1) ] )
	input = [ [], [[1,2,3]]]
	for i in input:
		a = p.getActions(i)
		msg = 'getActions('+str(i)+') ='+str(a)+' Expected '+str(answer)
		if not a == answer:
			msg = '**** FAIL **** : '+msg
		else:
			msg = ' pass : '+msg
		print(msg)

	# ------  TESTING applyActions() for 3x3 board  --------------------
	if 3 == n :
		io = [ [ [], [1,2,3], [[1,2,3]] ],
			   [ [[1,2,3]], [1,2,3], [[1,2,3],[1,2,3]] ],
			   [ [[1,2,3],[1,2,3]], [1,2,3], [[1,2,3],[1,2,3],[1,2,3]] ]
			   ]
		for i in io:
			a = p.applyAction( i[0], i[1] )
			msg = 'applyActions('+str(i[0])+','+str(i[1])+') = '+str(a)+' Expected '+str(i[2])
			if not a == i[2]:
				msg = '**** FAIL **** : '+msg
			else:
				msg = ' pass : '+msg
			print(msg)
#testv1()
