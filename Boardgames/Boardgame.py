"""Plays checkers with the user in the console."""
from Boardstate import board
import string
from colorama import init, Fore, Back, Style

def initGame():
	global theBoard
	"""acceptableGames = ["checkers"]
	enteredGame = ""
	while enteredGame not in acceptableGames:
		enteredGame = input("Please choose a game to play. Acceptable games: Checkers: ")
		enteredGame = enteredGame.lower()"""
	theBoard.setupGame("checkers")

def initPlayers():
	global theBoard
	numHumans = -1
	while numHumans > theBoard.maxHumans or numHumans < theBoard.minHumans:		#gets how many humans are playing
		try:
			numHumans = int(input("Please select the number of human players ({} to {}): ".format(theBoard.minHumans, theBoard.maxHumans)))
		except ValueError:
			print("Please enter a number between {} and {}".format(theBoard.minPlayers, theBoard.maxPlayers))
			continue
	for i in range(numHumans):														#assigns human players priority		
		while True:
			try:
				humanPriority = int(input("Please select priority for Player {} from {} to {}: ".format(i+1, 1, theBoard.maxHumans)))
			except ValueError:
				print("Please enter an unused number between {} and {}.".format(1, theBoard.maxHumans))
				continue
			if humanPriority > len(theBoard.players) or humanPriority < 1:
				print("Please enter a unused number between {} and {}.".format(1, theBoard.maxHumans))
				continue
			elif theBoard.playerType(humanPriority-1) is theBoard.unspecPlayer:
				theBoard.assignPlayer(humanPriority-1, theBoard.humanPlayer)
				break
			else:
				print("That player priority is already taken, please try again.")
	for j in range(theBoard.maxPlayers):																			#assigns comp players priority
		if theBoard.playerType(j) is theBoard.unspecPlayer:
			theBoard.assignPlayer(j, theBoard.compPlayer)

def takeTurn(currPlayer):
	#Solicits the user for a move and returns the value of the next player to make a move
	global theBoard
	if theBoard.game == "checkers":
		myPiece = (-1,-1)
		while True:
			myPiece = getPiece(currPlayer)
			myDest = getDestination(currPlayer, myPiece)
			if myDest != (-1, -1):
				break	
		nextPlayer = currPlayer
		while nextPlayer == currPlayer and myDest != (-1, -1):		#Double-jump recursion
			nextPlayer = theBoard.makeMove(currPlayer, myPiece[0], myPiece[1], myDest[0], myDest[1])
			if nextPlayer == currPlayer:							#Double-jump available
				myPiece = myDest
				myDest = getDestination(currPlayer, myPiece, nextPlayer==currPlayer)
		if myDest == (-1, -1):
			if nextPlayer == currPlayer:
				return int(not nextPlayer)							#Double-jump cancellation
			return currPlayer										#Piece reselection
		return nextPlayer	

def getPiece(currPlayer):
	global theBoard
	tempPiece = 0
	theBoard.printBoard(currPlayer)
	if theBoard.playerType(currPlayer) == theBoard.humanPlayer:
		while True:
			try:
				tempPiece = int(input("Player {}, please enter which piece to move: ".format(theBoard.players[currPlayer].color)))
			except ValueError:
				print("Please enter a valid number from the legend")
			if not str(tempPiece).strip():
				print("You cannot pass a turn.")
				continue
			pieceRow = int(tempPiece / len(theBoard.square))
			pieceCol = int(tempPiece % len(theBoard.square))
			if pieceRow < 0 or pieceCol < 0 or pieceRow > len(theBoard.square)-1 or pieceCol > len(theBoard.square[0])-1:
				print("Please enter a valid number from the legend")
			elif not theBoard.hasValidMoves(pieceRow, pieceCol, currPlayer):
				print("Please pick your pieces/a piece with valid moves.")
			else:
				break
	elif theBoard.playerType(currPlayer) == theBoard.compPlayer:
		#SOMETHING
		print("beep boop.")
	return (pieceRow, pieceCol)

def getDestination(currPlayer, currPiece, jumping=False):
	global theBoard
	theBoard.printBoard(currPlayer, True, currPiece[0], currPiece[1], jumping)
	if theBoard.playerType(currPlayer) == theBoard.humanPlayer:
		while True:
			try:
				destination = int(input("Player {}, please enter where to move piece {} ('-1' to choose a different piece; or cancel move if double-jumping): ".format(theBoard.players[currPlayer].color, currPiece[0]*len(theBoard.square)+currPiece[1])))
			except ValueError:
				print("Please enter a valid number from the legend")		
			if not str(destination).strip():
				print("You cannot pass a turn.")
				continue				
			destRow = int(destination / len(theBoard.square))
			destCol = int(destination % len(theBoard.square))
			if destination > ((len(theBoard.square)*len(theBoard.square[0]))-1) or destination < -2:
				print("Please enter a valid number from the legend")
			elif destination == -1:
				return (-1,-1)
			elif [destRow, destCol] not in theBoard.generateMoveList(currPiece[0], currPiece[1], jumping):
				print("Please enter a valid move option")
			else:
				break
	elif theBoard.playerType(currPlayer) == theBoard.compPlayer:
		#SOMETHING
		print("beep boop.")
	return (destRow, destCol)
	
def playGame():
	global theBoard 
	theBoard = board()
	initGame()
	initPlayers()
	gameOver = False
	currentPlayer = 0
	while not gameOver:
		currentPlayer = takeTurn(currentPlayer)
		gameOver = theBoard.isGameOver(currentPlayer)
	theBoard.printBoard(0)
	print("Game over! {} wins!".format(theBoard.winner))
		
	
	
playGame()	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
