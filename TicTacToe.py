#python
BoardNumbers = [1,2,3,4,5,6,7,8,9]
BoardState = [" "," "," "," "," "," "," "," "," "]
i = 0
CurrentPlayer = "X"
MoveCount = 0
Winner = ""

def printBoard(myBoard):
	print(str(myBoard[0]) +"|" +str(myBoard[1]) +"|" +str(myBoard[2]))
	print("-+-+-")
	print(str(myBoard[3]) +"|" +str(myBoard[4]) +"|" +str(myBoard[5]))
	print("-+-+-")
	print(str(myBoard[6]) +"|" +str(myBoard[7]) +"|" +str(myBoard[8]))
	print("") 
	
def checkForWin(myBoard):
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
			
def acceptNewMove():
	global MoveCount
	moveIsValid = False
	while moveIsValid is False:
		myMove = input("Current player is " + CurrentPlayer + ". Please enter your move: ")
		myMove = int(myMove)-1
		if BoardState[myMove] is " ":
			BoardState[myMove] = CurrentPlayer
			moveIsValid = True
		else:
			print("Invalid move, let's try again")
	MoveCount+=1

while MoveCount < 9 and Winner is "":
	print("Legend for where to put game moves")
	printBoard(BoardNumbers)

	print("")
	print("Current board state:")
	printBoard(BoardState)
	acceptNewMove()
	checkForWin(BoardState)
	if CurrentPlayer == "X":
		CurrentPlayer = "O"
	else:
		CurrentPlayer = "X"
print("")

#Print results of game
if Winner is not "":
	print("Game is over! "+Winner+" won in "+str(MoveCount)+" moves!")
else:
	print("Game is over, but nobody won =(")
printBoard(BoardState)