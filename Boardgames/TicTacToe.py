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
	#Checks for a winner and if one exists, returns the value of a winner if one exists
	for j in range(3):				
		if myBoard[j] == myBoard[j+3] and myBoard[j+3] == myBoard[j+6]:				#Cols
			return myBoard[j]
		elif myBoard[3*j] == myBoard[3*j+1] and myBoard[3*j+1] == myBoard[3*j+2]:	#Rows
			return myBoard[3*j]
		elif ((myBoard[0] == myBoard[4] and myBoard[4] == myBoard[8])				#Diagonals
			or (myBoard[2] == myBoard[4] and myBoard[4] == myBoard[6])):
			return myBoard[4]
	return " "
	
def acceptNewMove(MoveCount):
	#Prompts user for a valid move 
	moveIsValid = False
	while not moveIsValid:
		myMove = input("Current player is " + CurrentPlayer + ". Please enter your move: ")
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
			if BoardState[myMove] is " ":
				BoardState[myMove] = CurrentPlayer
				moveIsValid = True
			else:
				print("That space is taken, let's try again.")
	return MoveCount+1

def initCheckers():
	#Initializes the checkers variables
	global BoardNumbers
	global BoardState
	global Winner
	BoardNumbers = range(9)
	BoardState = [" "]*9
	Winner = " "
	
#Runs the game
initCheckers()
MoveCount = 0
CurrentPlayer = ""
while MoveCount < 9 and Winner is " ":
	if CurrentPlayer == "X":
		CurrentPlayer = "O"
	else:
		CurrentPlayer = "X"
	print("Legend for where to put game moves:")
	printBoard(BoardNumbers)
	print("\nCurrent board state:")
	printBoard(BoardState)
	MoveCount = acceptNewMove(MoveCount)
	Winner = checkForWin(BoardState)

#Print results of game
printBoard(BoardState)
if Winner is not " ":
	print("\nGame is over! {} won in {} moves!".format(Winner, MoveCount))
else:
	print("\nGame is over, but nobody won =(")