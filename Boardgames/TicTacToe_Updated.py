#Matt Schiller's TicTacToe Program
from colorama import Fore, Style 

def printBoard(myBoard):
	#Prints the given board state.	
	print((str(myBoard[0]) +"|" +str(myBoard[1]) +"|" +str(myBoard[2])).center(40))
	print(("-+-+-").center(40))
	print((str(myBoard[3]) +"|" +str(myBoard[4]) +"|" +str(myBoard[5])).center(40))
	print(("-+-+-").center(40))
	print((str(myBoard[6]) +"|" +str(myBoard[7]) +"|" +str(myBoard[8])).center(40))
	print("") 
	
def checkForWin(myBoard):
	#Checks for a winner and if one exists, returns the value of a winner
	for j in range(3):				
		if myBoard[j] == myBoard[j+3] and myBoard[j+3] == myBoard[j+6]:				#Cols
			return myBoard[j]
		elif myBoard[3*j] == myBoard[3*j+1] and myBoard[3*j+1] == myBoard[3*j+2]:	#Rows
			return myBoard[3*j]
		elif ((myBoard[0] == myBoard[4] and myBoard[4] == myBoard[8])				#Diagonals
			or (myBoard[2] == myBoard[4] and myBoard[4] == myBoard[6])):
			return myBoard[4]
	for k in BoardNumbers:
		if BoardState[k] == empty:
			return empty	
	return tie
	
def acceptNewMove(MoveCount):
	#Prompts user for a valid move 
	myMove = 0
	if players[CurrentPlayer][0] == human:
		print("Legend for where to put game moves:")
		printBoard(BoardNumbers)
		print("\nCurrent board state:")
		printBoard(BoardState)
		moveIsValid = False
		while not moveIsValid:
			myMove = input("Current player is " + players[CurrentPlayer][1] + ". Please enter your move: ")
			try:
				myMove = int(myMove)
			except:										#Non-number
				print("I need a number, let's try again.")
				continue
			if not str(myMove).strip():					#Null/space entry
				print("You cannot pass a turn, let's try again.")
				continue
			if myMove > 8 or myMove < 0:				#Out of bounds
				print("Out of bounds selection, let's try again.")
			else:
				if BoardState[myMove] is empty:
					BoardState[myMove] = players[CurrentPlayer][1]
					moveIsValid = True
				else:
					print("That space is taken, let's try again.")
	else:												#Accept comp input
		miniMax(CurrentPlayer, BoardState, 0)
		#print(compMove)
		BoardState[compMove] = players[CurrentPlayer][1]	
	return MoveCount+1

def score(scoreBoard, depth):
	#Returns a score value based on depth (to have the comp try and 'play out' the game hoping you make a mistake
	if checkForWin(scoreBoard) == playerX:						#Max for X
		return 10-depth
	elif checkForWin(scoreBoard) == playerO:					#Min for O
		return -10+depth
	elif checkForWin(scoreBoard) == tie:
		return 0				#Tie
	else:
		return None

def listOfEmpties(myBoard):
	count = []
	for i in BoardNumbers:
		if myBoard[i] == empty:
			count.append(i)
	return count
	
def miniMax(simPlayer, simBoard, depth):
	#Creates a simulation board that returns a tuple with the most favorable move for the given player value
	if score(simBoard, depth) != None:
		return score(simBoard, depth)
	global compMove

	#NOT WORKING######### Keeps losing after 2-3 turns
	MMDict = {}
	
	debugBoard = [empty]*9
	for i in listOfEmpties(simBoard):
		simBoard[i] = players[simPlayer][1]
		debugBoard[i] = miniMax(int(not simPlayer), simBoard, depth+1)
		MMDict[debugBoard[i]] = i
		simBoard[i] = empty		

#	if depth in [1]:
#		printBoard(simBoard)
#		printBoard(debugBoard)
#		print(MMDict)
#		print("I predict player {} will go {}".format(players[simPlayer][1], MMDict[max(MMDict.keys())]))
#		wait = input("Enter to continue")

	if players[simPlayer][0] == human:
		#compMove = MMDict[max(MMDict, key=MMDict.get)]
		return max(MMDict.keys())
	else:
		compMove = MMDict[min(MMDict.keys())]
		return min(MMDict.keys())


def initTicTacToe():
	#Initializes the TicTacToe variables
	global BoardNumbers, BoardState, Winner, playerX, playerO, human, comp, players, empty, tie
	playerO, playerX = "O", "X"
	human, comp, tie = "_HUMAN", "_COMP", "No one"
	BoardNumbers = range(9)
	empty = " "
	BoardState = [empty]*9
	Winner = empty
	players = [""]*2
	players[0] = (human, playerX)
	players[1] = (comp, playerO)
	
#Runs the game
initTicTacToe()
MoveCount = 0
CurrentPlayer = 0
while MoveCount < 9 and Winner is empty:
	MoveCount = acceptNewMove(MoveCount)
	Winner = checkForWin(BoardState)
	CurrentPlayer = int(not CurrentPlayer)

#Print results of game
printBoard(BoardState)
print("\nGame is over! {} won in {} moves!".format(Winner, MoveCount))