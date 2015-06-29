#python
BoardNumbers = [1,2,3,4,5,6,7,8,9]
BoardState = [" "," "," "," "," "," "," "," "," "]
i = 0
CurrentPlayer = "X"
MoveCount = 0
Winner = ""

def printBoard(myBoard):
	i = 0
	while i < len(myBoard):
		print(myBoard[i],"|", myBoard[i+1], "|", myBoard[i+2])
		print("_________")
		i+=3
	print("") 
def checkForWin(myBoard)
	global Winner
	for j in range(0,3):
		if (myBoard[j] is not " ") and (
		#Rows and Cols
			((myBoard[j] == myBoard[j+1] and myBoard[j+1] == myBoard[j+2])
			or (myBoard[j] == myBoard[j+3] and myBoard[j+3] == myBoard[j+6]))
		#Diagonals
			or (j is 0 and myBoard[j] == myBoard[j+4] and myBoard[j+4] == myBoard[j+8])
			or (j is 2 and myBoard[j] == myBoard[j+2] and myBoard[j+2] == myBoard[j+4])):
			Winner = myBoard[j]

while MoveCount < 9 and Winner is "":
	print("Legend for where to put game moves")
	printBoard(BoardNumbers)

	print("")
	print("Current board state:")
	printBoard(BoardState)
	
	#Accept new move
	moveIsValid = 0
	while moveIsValid is 0:
		myMove = input("Current player is " + CurrentPlayer + ". Please enter your move: ")
		myMove = int(myMove)-1
		if BoardState[myMove] is " ":
			BoardState[myMove] = CurrentPlayer
			moveIsValid = 1
		else:
			print("Invalid move, let's try again")
	MoveCount+=1
	#Move entered, check for win
	checkForWin(BoardState)
	if CurrentPlayer == "X":
		CurrentPlayer = "O"
	else:
		CurrentPlayer = "X"
print("")
#Print results of game
if Winner is not "":
	print("Game is over! "+Winner+" wins in "+str(MoveCount)+" moves!")
else:
	print("Game is over, but nobody won =(")
printBoard(BoardState)