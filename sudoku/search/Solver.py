from execute import *
from bfs import *
from helper import *

#def Solver(puzzle, r, c, search='bfs', printSolution=False):
class Problem:
    def initial(selfs, puzzle, printSolution):
        return initialPuzzle(puzzle, printSolution)
    def prune(self, puzzle, printSolution):
        return prune(puzzle, printSolution)
    def getActions(self, puzzle):
        print()
    def isGoal(self, puzzle):
        print()
#Prints array puzzle
def printPuzzle(puzzle):
    d = len(puzzle[0])
    for i in range (0, d):
        print(puzzle[i])
    print()

def removeZeros(puzzle):
    d = len(puzzle[0])
    #replaces zeros with a list of ints 1 to d
    for i in range(0, d):
        for j in range(0, d):
            if puzzle[i][j] == 0:
                puzzle[i][j] = list(range(1, d + 1))
                for l in range(0, d):
                    if isinstance(puzzle[l][j], int) and puzzle[l][j] != 0:
                        puzzle[i][j].remove(puzzle[l][j])
                for m in range(0, d):
                    if isinstance(puzzle[i][m], int) and puzzle[i][m] != 0:
                        if puzzle[i][m] in puzzle[i][j]:
                            puzzle[i][j].remove(puzzle[i][m])
    return puzzle

def cullAction(puzzle):
    d = len(puzzle[0])
    #turns lists of 1 element into integers
    for i in range(0, d):
        for j in range(0, d):
            if isinstance(puzzle[i][j], list) and len(puzzle[i][j]) == 1:
                puzzle[i][j] = puzzle[i][j][0]
    #checks lists for possible eliminations
    for i in range(0, d):
        for j in range(0, d):
            if isinstance(puzzle[i][j], list):
                for k in range(0, d):
                    if isinstance(puzzle[k][j], int) and puzzle[k][j] in puzzle[i][j]:
                        puzzle[i][j].remove(puzzle[k][j])
                for l in range(0, d):
                    if isinstance(puzzle[i][l], int)and puzzle[i][l] in puzzle[i][j]:
                        puzzle[i][j].remove(puzzle[i][l])
    return puzzle

def cullLists(puzzle):
    d = len(puzzle[0])
    temp = []
    done = False
    while not done: #for x in range(0, 6):
        if temp != puzzle:
            temp = puzzle
            puzzle = cullAction(puzzle)
        else:
            puzzle = cullAction(puzzle)
            done = True
        puzzle = cullAction(puzzle)
    puzzle = cullAction(puzzle)

    sum = 0
    for i in range(0, d):
        for j in range(0, d):
            if isinstance(puzzle[i][j], list): sum += 1
    if sum == 0:
        print("Completed Sudoku puzzle:")
        printPuzzle(puzzle)

    return puzzle

def makeListOfPossibilities(puzzle, printSolution):
    d = len(puzzle[0])
    possible = []
    for i in range(0, d):
        for j in range(0, d):
            if isinstance(puzzle[i][j], list):
                possible.insert(len(possible), puzzle[i][j])
    #if printSolution == True:
    if printSolution == True: print(possible)
    if printSolution == True: print("blanks to be filled: ", len(possible))
    permutations = 1
    for x in range(0, len(possible)):
        permutations = permutations * len(possible[x])
    if printSolution == True: print("total permutations: ", permutations)
    return possible

def initialPuzzle(puzzle, printSolution):
    if printSolution == True: printPuzzle(puzzle)
    return puzzle

def prune(puzzle, printSolution):
    if printSolution == True: print("Calling removeZeros:")
    puzzle = removeZeros(puzzle)
    if printSolution == True: printPuzzle(puzzle)

    if printSolution == True: print("Calling cullLists:")
    puzzle = cullLists(puzzle)
    if printSolution == True: printPuzzle(puzzle)

    return puzzle

def test1(puzzle, printSolution):
    puzzle = prune(puzzle, printSolution)
    print(puzzle)
    BFS(puzzle)

    z = permute(puzzle)
    print(z)
    #puzzle = prune(puzzle, printSolution)
    #puzzleList = makeListOfPossibilities(puzzle, printSolution)
    #permute(puzzleList)
def test2(puzzle, printSolution):
    puzzle = prune(puzzle, printSolution)
    possible = makeListOfPossibilities(puzzle, printSolution)
    if printSolution == True: print(possible)
    #for i in range(0, len(possible)):
     #   if printSolution == True: print(possible[i][0], end =":")
      #  for j in range(0, len(possible[i])):
       #     if printSolution == True: print(possible[i][j])

problem = Problem()
#problem.initial(p1, True)
#problem.prune(p1, True)
BFS(problem)
#test1(p1, False)
#test2(p2, False)
#prune(p2, False)
#test1(p1 , False)
#test2(p3, True)
