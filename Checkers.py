"""Plays checkers with the user in the console."""
from Boardstate import board
import string

def initGame():
	global theBoard
	acceptableGames = ["checkers"]
	enteredGame = ""
	while enteredGame not in acceptableGames:
		enteredGame = input("Please choose a game to play. Acceptable games: Checkers: ")
		enteredGame = enteredGame.lower()
	#theBoard = board()
	theBoard.setupGame(enteredGame)

def initPlayers():
	global theBoard
	numHumans = -1
	while numHumans > theBoard.maxHumans and numHumans < theBoard.minHumans:										#gets how many humans are playing
		try:
			numHumans = int(input("Please select the number of human players: "))
		except ValueError:
			print("Please enter a number between {} and {}".format(theBoard.minPlayers, theBoard.maxPlayers))
			continue
	for i in range(numHumans):																						#assigns human players priority
		humanPriority = 0
		while not humanPriority:
			try:
				humanPriority = int(input("Please select priority for Player {} from 1 to {}: ".format(i+1, theBoard.maxHumans)))
			except ValueError:
				print("Please enter a number between {} and {}".format(i+1, theBoard.maxHumans))
				continue
			if theBoard.playerType([humanPriority-1]) is theBoard.unspecPlayer:
				theBoard.assignPlayer(humanPriority-1, theBoard.humanPlayer)
			else:
				print("That player priority is already taken, please try again.")
	for j in range(theBoard.maxPlayers):																			#assigns comp players priority
		if theBoard.playerType(j) is theBoard.unspecPlayer:
			theBoard.assignPlayer(j, theBoard.compPlayer)

def takeTurns(currPlayer):
	global theBoard
	theBoard.printBoard("Legend")
			
def playGame():
	global theBoard 
	theBoard = board()
	initGame()
	initPlayers()
	takeTurns(0)
		
	
	theBoard.printBoard("Actual")
playGame()	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
