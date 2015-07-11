"""Class to describe a given 8x8 board state."""
from colorama import init, Fore, Back, Style

class board(object):
	def __init__(self):
		self.supportedGames = ["checkers"]
		self.maxPlayers = 0
		self.minPlayers = 0
		self.maxHumans = 0
		self.minHumans = 0
		self.square = []
		self.unspecPlayer = "_UNSPEC"
		self.humanPlayer = "_HUMAN"
		self.compPlayer = "_COMP"
		self.emptySpace = " "
		self.game = ""		
		self.winner = ""
	
	def setupGame(self, game):
		self.game = game.lower()
		if game in self.supportedGames:
			self.setupPlayers()
			self.setupBoard()
		else:
			print("Error! Only the game {} is supported.".format(self.supportedGames))	
	
	def setupBoard(self):
		if self.game == "checkers":
			self.square = [[piece(self.game, self.emptySpace) for i in range(8)] for j in range(8)]
			self.emptyPiece = piece(self.game, self.emptySpace)
			for i in range(len(self.square)):
				for j in range(len(self.square[i])):
					if i in [0,1,2] and (i+j) % 2 == 0:
						self.square[i][j].updatePiece(self.square[i][j], self.square[i][j].topDir)
					elif i in [5,6,7] and (i+j) % 2 == 0:
						self.square[i][j].updatePiece(self.square[i][j], self.square[i][j].botDir)	
	
	def setupPlayers(self):
		if self.game == "checkers":
			self.maxPlayers = 2
			self.minPlayers = 0
			self.maxHumans = self.maxPlayers
			self.minHumans = self.minPlayers
			self.xPlayer = "X"
			self.oPlayer = "O"
			self.players = [player(self.unspecPlayer) for i in range(self.maxPlayers)]
			self.players[0].updateColor(self.xPlayer)
			self.players[1].updateColor(self.oPlayer)			
	
	def assignPlayer(self, playerNum, Type):
		self.players[playerNum].updateType(Type)
	
	def playerType(self, playerNum):
		try:
			self.players[playerNum].type
		except IndexError:
			return "Out of range!"
	
	def printBoard(self, player, gettingDest=False, pieceRow=-1, pieceCol=-1, jumping=False):
		init(autoreset=True)
		padding = 2
		print("Current board state:")
		for i in range(len(self.square)):
			printRow = ''
			for j in range(len(self.square[i])):
				printValue = ''
				padding = 1
				if i % 2 != j % 2:
					printValue = printValue + Fore.BLACK											#Remove unusable squares
				if self.square[i][j].color != self.players[player].color and self.square[i][j].color != self.square[i][j].empty:
					printValue = printValue + Style.BRIGHT + Fore.RED								#Highlight opponent pieces
				if self.square[i][j].color == self.players[player].color:
					printValue = printValue + Style.DIM + Fore.GREEN								#Color and dim all player pieces
					if not gettingDest and self.hasValidMoves(i, j, player):
						printValue = printValue + Style.BRIGHT										#Highlight available player pieces
				if gettingDest:
					if pieceRow > -1 and pieceCol > -1 and pieceRow < len(self.square) and pieceCol < len(self.square[i]):	#Valid square
						if [i,j] in self.generateMoveList(pieceRow, pieceCol, jumping):
							printValue = printValue + Style.BRIGHT + Fore.YELLOW					#Highlight available destinations
						if i == pieceRow and j == pieceCol:	
							printValue = printValue + Style.BRIGHT + Fore.GREEN						#Highlight current piece [redundant, but available to be changed]
				printValue = printValue + (2-len(str((i*len(self.square[i]))+j)))*' ' + str((i*len(self.square[i]))+j) + ' '	#Include Legend
				if self.square[i][j].topDir in self.square[i][j].myDir and self.square[i][j].botDir in self.square[i][j].myDir:
					printValue = printValue + str(self.square[i][j].color) 							#King Piece, double print
					padding = 0
				printValue = printValue + str(self.square[i][j].color) + Fore.RESET
				printRow = printRow + Style.DIM + '[' + printValue + ' '*padding + Style.DIM +  ']' + Style.RESET_ALL
			print(printRow)	
				
	def hasValidMoves(self, row, col, player):
		if self.game == "checkers":
			if self.square[row][col].color != self.players[player].color:				#Not player's piece
				return False
			else:															
				destination = self.generateMoveList(row, col)
				if len(destination) > 0:
					return True			
		
	def generateMoveList(self, row, col, needJump=False):
		init()
		if self.game == "checkers":
			##KINGS CAN LOOP AROUND THE BOARD LEFT-RIGHT??
			moveList = []
			if self.square[row][col].topDir in self.square[row][col].myDir:				#Top-style movement
				if not needJump:
					if col < len(self.square[row])-1 and row < len(self.square)-1:		#Down-right
						moveList.append([row+1, col+1])
					if col > 0 and row < len(self.square)-1:							#Down-left
						moveList.append([row+1, col-1])
				if row < len(self.square)-2 and col > 1:								#Top-style jumping (left)
					if self.square[row+1][col-1].color not in [self.square[row][col].color, self.square[row][col].empty]:
						moveList.append([row+2, col-2])
				if row < len(self.square)-2 and col < len(self.square[row])-2:			#Top-style jumping (right)
					##THIS BUGGED OUT, DIDN'T FIND MOVE INTO BOTTOM RIGHTMOST CORNER
					if self.square[row+1][col+1].color not in [self.square[row][col].color, self.square[row][col].empty]:
						moveList.append([row+2, col+2])		
			if self.square[row][col].botDir in self.square[row][col].myDir:				#Bot-style movement
				if not needJump:
					if col < len(self.square[row])-1 and row > 0:						#Up-right
						moveList.append([row-1, col+1])
					if col > 0 and row > 0:												#Up-left
						moveList.append([row-1, col-1])
				if row > 1 and col > 1:													#Bot-style jumping (left)
					if self.square[row-1][col-1].color not in [self.square[row][col].color, self.square[row][col].empty]:
						moveList.append([row-2, col-2])
				if row > 1 and col < len(self.square[row])-2:							#Bot-style jumping (right)
					if self.square[row-1][col+1].color not in [self.square[row][col].color, self.square[row][col].empty]:
						moveList.append([row-2, col+2])
			
			validMoves = []
			for i in moveList:														#Is that square empty/on the board?
				if self.square[i[0]][i[1]].color == self.emptySpace:
					validMoves.append(i)
			return validMoves
	
	def makeMove(self, player, fromRow, fromCol, toRow, toCol):
		if self.game == "checkers":
			self.square[toRow][toCol].updatePiece(self.square[fromRow][fromCol])
			self.square[fromRow][fromCol].updatePiece(self.emptyPiece)
			if abs(fromRow-toRow) > 1:
				isJumpMove = True										#Now, remove the taken piece
				self.square[int((fromRow+toRow)/2)][int((fromCol+toCol)/2)].updatePiece(self.emptyPiece)
			else:
				isJumpMove = False
			if (toRow == len(self.square)-1 and self.square[toRow][toCol].topDir in self.square[toRow][toCol].myDir) or (toRow == 0 and self.square[toRow][toCol].botDir in self.square[toRow][toCol].myDir):			#Makes a king
				self.square[toRow][toCol].updatePiece(self.square[toRow][toCol], self.square[toRow][toCol].king)
			if isJumpMove and self.generateMoveList(toRow, toCol, isJumpMove):
				return player
			return int(not player)			
	
	def isGameOver(self, player):
		#Checks if there are any valid moves for the current player or at all
		if self.playerPieces(player) == 0:
			self.winner = self.players[int(not player)].color					#Lost with no pieces and not to a double-jump
			return True
		elif self.playerPieces(int(not player)) == 0:							#Won by taking all opp's pieces
			self.winner = self.players[player].color
			return True
		else:																	#Both players on board
			for row in range(len(self.square)):
				for col in range(len(self.square[row])):
					if self.hasValidMoves(row, col, player):
						return False											#Player on the play has a move, not Game Over
			for row in range(len(self.square)):
				for col in range(len(self.square[row])):
					if self.hasValidMoves(row, col, int(not player)):
						print("Player {} has no moves and Player {} has a move!".format(self.players[player].color, self.players[int(not player)].color))
						self.winner = self.players[int(not player)].color		#Lost due to opponent having moves when you don't
						return True	
			print("Player {} and {} have no moves!".format(self.players[player].color, self.players[int(not player)].color))
			self.winner = "No one"												#No one has moves
			return True
	
	def playerPieces(self, player):
		#Returns the number of pieces a player has
		count = 0
		for row in range(len(self.square)):
			for col in range(len(self.square[row])):
				if self.square[row][col].color == self.players[player].color:
					count+=1
		return count			
	
class player(object):								#Player definition	
	def __init__(self, myType):
		self.type = myType
		self.color = ""
		self.winner = False
	def updateType(self, newType):
		self.type = newType
	def updateColor(self, newColor):
		self.color = newColor
		
class piece(object):								#Pieces definition
	def __init__(self, myGame, sentDir):
		self.game = myGame
		self.topDir = "_DOWN"
		self.botDir = "_UP"
		self.empty = " "
		self.pieceValues = {}
		if myGame == "checkers":
			self.setupCheckers(sentDir)
	def setupCheckers(self, sentDir):
		self.king = self.topDir + self.botDir
		self.pieceValues[self.topDir] = "X"
		self.pieceValues[self.botDir] = "O"
		self.pieceValues[self.empty] = " "
		self.pieceValues[self.king] = self.topDir + self.botDir
		self.color = self.pieceValues[sentDir]
		self.myDir = sentDir
	def updatePiece(self, clonePiece, action = ""):
		self.color = clonePiece.color
		self.myDir = clonePiece.myDir
		if action in self.pieceValues.keys():
			if action != self.king:
				self.color = self.pieceValues[action]
			self.myDir = action