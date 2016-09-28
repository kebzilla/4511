import timeit

class Solution:

	def lowestCommonAncestor(self, root, p, q):
		p = self._dfs(root, p)
		q = self._dfs(root, q)
		answer = root
		while p and q and p[-1] is q.pop():
			answer = p.pop()
		return answer
	
	def _dfs(self, root, n):
		parents = dict()
		stack = [root]
		while stack:
			node = stack.pop()
			if node is None:
				continue
			if node is n:
				break
		stack.append(node.left)
		stack.append(node.right)
		parents[node.left] = node
		parents[node.right] = node

		answer = [n]
		while answer[-1] != root:
			answer.append(parents[answer[-1]])
		return answer

p1 = [[  0,	'+',	0,		'-',	0,		'=',	6	],
	  ['+',	None,	'-',	None,	'+',	None,	None],
	  [  0,	'*',	0,  	'-',	0,		'=',	2	],
	  ['+',	None,	'+',	None,	'/',	None,	None],
	  [  0,	'/',	0,		'+',	0,		'=',	10	],
	  ['=',	None,	'=',	None,	'=',	None, 	None],
	  [ 10,	None,	6,		None,	2,		None,	None]]

p2 = [[  0,	'+',	0,		'+',	0,		'=',	15	],
	  ['+',	None,	'*',	None,	'/',	None,	None],
	  [  0,	'+',	0,  	'*',	0,		'=',	24	],
	  ['-',	None,	'-',	None,	'/',	None,	None],
	  [  0,	'+',	0,		'-',	0,		'=',	14	],
	  ['=',	None,	'=',	None,	'=',	None, 	None],
	  [  3,	None,	12,		None,	4,		None,	None]]

def initialize_values(board):
	d = int((len(board) - 1) / 2)
	values = []
	for i in range(d): values.insert(i, list([0]* d))
	#print(values)
	return values
def initialize_arguments(board):
	d = int(len(board))
	arguments = []
	for i in range(d):
		for j in range(d):
			if board[i][j] == '+' or board[i][j] == '-' or board[i][j] == '*' or board[i][j] == '/':
				arguments.insert(len(arguments), board[i][j])
				#print(arguments)
	#print(arguments)
def initialize_equations(puzzle):
	d = len(puzzle) - 1
	equations = []
	for i in range(d):
		if i % 2 == 0:
			equations.insert(int(i / 2), puzzle[i])
	#for i in range(len(equations)):
		#print(equations[i])
	return equations

def evaluate_equation(equation):
	eq = ""
	for i in range(len(equation) - 2):
		eq = eq + str(equation[i])
		if i % 2 == 0:
			eq = str(eval(eq))
	#print(eq, '=', eval(eq))
	return eval(eq) == equation[len(equation) - 1]
def loop_solve(equation):
	start = timeit.default_timer()
	#print(equation)
	accepted_equations = []
	for i in range(1, 10):
		equation[0] = i
		for j in range(1, 10):
			if i != j:
				equation[2] = j
				for k in range(1, 10):
					if k != i and k != j:
						equation[4] = k
						#print(equation)
						if evaluate_equation(equation):
							#print(equation)
							accepted_equations.insert(len(accepted_equations), list(equation))
							#print(accpeted_equations)
	for i in range(0, len(accepted_equations)):
		print(accepted_equations[i])
	print(len(accepted_equations))
	stop = timeit.default_timer()
	print(stop - start)
	return accepted_equations

		

def test1(puzzle):
	solutions = []
	for i in range(0, len(puzzle) - 1):
		if i % 2 == 0:
			solutions.insert(i, loop_solve(puzzle[i]))
	x = Solution()
	print(x._dfs(puzzle, 3))
	#print(solutions)
	
#initialize_values(p1)
#initialize_arguments(p1)
#test1(p1)
test1(p1)
#print(p2[2])
#loop_solve([0, '+', 0, '-', 0, '=', 14])
