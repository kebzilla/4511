# This example is a simplistic "puzzle" in which the objective is to fill an nxn grid
# such that each row and each column contains exactly 1 instance of each of the numbers 1-n.
# It is a demonstration of how to code a puzzle solver using a generic BFS framework.

from copy import deepcopy
from functools import reduce

from helper import permute
from helper import flatten
from bfs import *

class UF2problem(object):
	def __init__(self, initial, size, goal=None):
		# These values are specific to the problem you are solving (i.e. sudoku, nQueens, ...)
		self.size = size
		self.initial = initial
		self.goal = goal

		# For this example, an action is the assignment of a single box
		# thus, the set of legal actions for all states is all numbers 1 to n
		self.actions = [ i for i in range(1,self.size+1) ]

	def getActions( self, state ) :
		# Because all actions are legal for this example, they were generated once
		# in init, then are passed along here.
		# It might be that you generate only legal actions here, OR you generate all
		# actions, then test for legality in applyAction()
		if ( self.size == len(state) ):
			#print(state)
			if ( len(state[self.size-1]) == self.size ) :
				return []
		return self.actions

	def applyAction ( self, state, action ) :
		# It is very important that you generate a new variable with deepcopy for the new state
		# This code is problem specific. An action is applied by adding a number to the next
		# box (which is slightly complicated to determine given the state representation
		newState = deepcopy(state)
		# first flatten the list to determine the row and column in which to place the number
		flat = flatten(state)
		idx = len(flat)
		row = idx // self.size
		col = idx % self.size
		# if it is the first element of a new row, the number is added as a list
		if ( 0 == col ):
			newState.append( [action] )
		else :
			newState[row].append( action )
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
		# duplicates across columns or rows
		for row in state :
			if len(list(set(row))) < self.size :
				return False
		for col in range(self.size):
			if len( list(set([ row[col] for row in state ] ) )) < self.size :
				#print('State ',state,' not goal')
				return False

		# If we got here, the board is complete and legal
		print('WINNER')
		for i in range(self.size):
			output = ''
			for j in range(self.size):
				output += '   '+str(state[i][j])
			print(output)
		return True

if __name__ == "__main__" :
	BFS(UF2problem([],4))

#------------------------------------------------------------------------------------
def testv2():
	n = 3
	p = UF2problem([],n)

	answer = [ i for i in range(1,n+1)]
	input = [ [], [[1,2,3]]]
	for i in input:
		a = p.getActions(i)
		msg = 'getActions('+str(i)+') ='+str(a)+' Expected '+str(answer)
		if not a == answer:
			msg = '**** FAIL **** : '+msg
		else:
			msg = ' pass : '+msg
		print(msg)

	if 3 == n :
		io = [ [ [], 1, [[1]] ],
			   [ [[1]], 2, [[1,2]] ],
			   [ [[1,2,3]], 1, [[1,2,3],[1]] ],
			   [ [[1,2,3],[1]], 2, [[1,2,3],[1,2]] ]
			   ]
		for i in io:
			a = p.applyAction( i[0], i[1] )
			msg = 'applyActions('+str(i[0])+','+str(i[1])+') = '+str(a)+' Expected '+str(i[2])
			if not a == i[2]:
				msg = '**** FAIL **** : '+msg
			else:
				msg = ' pass : '+msg
			print(msg)
#testv2()

