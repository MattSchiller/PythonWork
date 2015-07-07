"""Imports a local dictionary, requests up to 7 letters including blanks, and outputs all valid words"""
import string
import re
import fnmatch
import csv
import operator
from Trie import trie
from Stopwatch import stopwatch

def importFile():
	#Imports a specified file for loading.
	with open('C:/Users/Schiller/Desktop/PythonWork/dict.txt') as file:
		theFile = file.read().splitlines()
	return theFile
def importCSV():
	#Reads in a CSV file for use.
	theList = dict()
	theFile = open('C:/Users/Schiller/Desktop/PythonWork/scrabbleValues.csv')
	for row in csv.reader(theFile):
		theList[row[0].lower()] = int(row[1])
	return theList	
def createTrie(myDictionary):
	global Trictionary
	Trictionary = trie()
	createTime = stopwatch()
	createTime.start()
	for i in myDictionary:
		Trictionary.add(i)
	createTime.stop()
	#print(Trictionary)
	print("Trie took {:.2f} seconds to load".format(createTime.duration()))
def acceptLetters():
	#Gets the letters from the user
	global letters 
	while True:
		letters = input("Enter up to 7 letters (including _ for blank): ")
		if re.search("[^A-z*]+", letters):
			print("Invalid characters entered, try again.")
		#elif len(letters) > 7 or len(letters) < 1:
		#	print("Invalid number of characters entered >0 and >7 only.")
		else:
			letters = letters.lower()
			letters = ["?" if X is "_" else X for X in letters]
			break				
def preAppendFilter(word):
	#Massages out any "?"s pre-checking the trictionary
	questionMark = word.find("?")
	if questionMark >= 0:
		for i in string.ascii_lowercase:
			if questionMark is len(word):
				word = word[0:questionMark]+i
			else:
				word = word[0:questionMark]+i+word[questionMark+1:len(word)]
			appendIfLegal(word)
	else:
		appendIfLegal(word)
		
def appendIfLegal(word):
	#Checks if a word is legal against the dictionary and adds to found words
	global validWords
	if Trictionary.contains(word) and getPoints(word) > 0:
		validWords[word] = getPoints(word)
def getPoints(word):
	#Finds the point value of a given word
	global letterPoints
	myPoints = 0
	for letter in word:
		myPoints+=letterPoints[letter]
	return myPoints
def alreadyChecked(word):
	#Checks to see if this path has been 'gone down' before for duplicate letters
	global checkedWords
	if word in checkedWords:
		return True
	else:
		checkedWords.append(word)
		return False	
def permute(word, myLetters):
	#Divides a given string to find all combinations of words
	preAppendFilter(word)
	for i in range(len(myLetters)):
		if alreadyChecked(word + myLetters[i]):
			continue
		elif len(myLetters) is 1:
			permute(word + myLetters[i], "")
		else:
			permute(word + myLetters[i], myLetters[0:i] + myLetters[i+1:])
	
def printValids():
	#Prints global variable validWords{} by points
	global validWords
	currPoints = []
	pointValue = 0
	validWords = sorted(validWords.items(), key=operator.itemgetter(1))
	for item in validWords:
		if pointValue is 0 or pointValue is item[1]:
			currPoints.append(item[0])
			pointValue = item[1]
		else:
			print(pointValue, "point words:", ", ".join(currPoints))
			currPoints = []
			pointValue = 0

dictionary = importFile()
letterPoints = importCSV()
createTrie(dictionary)
acceptLetters()
checkedWords = []
validWords = {}
permuteTime = stopwatch()

permuteTime.start()
permute("", letters)
printValids()

permuteTime.stop()
print("Code took {:.2f} seconds to run".format(permuteTime.duration()))








