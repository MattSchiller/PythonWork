"""Class to describe a given 8x8 board state."""

class board(object):
	def __init__(self):
		self.supportedGames = ["checkers"]
		self.maxPlayers = 0
		self.minPlayers = 0
		self.maxHumans = 0
		self.minHumans = 0
		self.square = []
		self.unspecPlayer = "_UNSPEC"
		self.humanPlayer = "HUMAN"
		self.compPlayer = "COMP"
		self.emptySpace = "  "
		self.game = ""
		
	def setupGame(self, game):
		self.game = game.lower()
		if game in self.supportedGames:
			self.setupBoard()
			self.setupPlayers()
		else:
			print("Error! Only the game {} is supported.".format(self.supportedGames))
	
	def setupBoard(self):
		if self.game == "checkers":
			self.square = [[self.emptySpace for i in range(8)] for j in range(8)]
			self.square[0] = ["X", self.emptySpace, "X", self.emptySpace, "X", self.emptySpace, "X", self.emptySpace]
			self.square[1] = [self.emptySpace, "X", self.emptySpace, "X", self.emptySpace, "X", self.emptySpace, "X"]
			self.square[2] = self.square[0]
			self.square[5] = ["O", self.emptySpace, "O", self.emptySpace, "O", self.emptySpace, "O", self.emptySpace]
			self.square[6] = [self.emptySpace, "O", self.emptySpace, "O", self.emptySpace, "O", self.emptySpace, "O"]
			self.square[7] = self.square[5]
			
	def setupPlayers(self):
		if self.game == "checkers":
			self.maxPlayers = 2
			self.minPlayers = 0
			self.maxHumans = self.maxPlayers
			self.minHumans = self.minPlayers
			self.players = [self.unspecPlayer for i in range(self.maxPlayers)]
	
	def assignPlayer(self, playerNum, Type):
		self.players[playerNum] = Type
		
	def playerType(self, playerNum):
		try:
			return self.players[playerNum]
		except IndexError:
			return "Out of range!"
	
	def printBoard(self, printType):
		if printType not in ["Legend", "Actual"]:
			print("Wrong type of print used.")
		else:
			print("Current board state:")
			for i in range(len(self.square)):
				printRow = ""
				for j in range(len(self.square[i])):
					if printType == "Actual":
						printValue = str(self.square[i][j])
					elif printType == "Legend":
						printValue = str((i*len(self.square[i]))+j)
					printRow = printRow + "[" +  " "*(2-len(printValue)) + printValue + "]"
				print(printRow)	
			
			