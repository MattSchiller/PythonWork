"""Imports a local dictionary, requests up to 7 letters including blanks, and outputs all valid words"""
import time
import string
import re
import fnmatch

def importFile():
	#Imports a specified file for loading.
	global dictionary
	with open('C:/Users/Schiller/Desktop/PythonWork/dict.txt') as file:
		dictionary = file.read().splitlines()

def acceptLetters():
	#Gets the letters from the user
	global letters 
	while True:
		letters = input("Enter up to 7 letters (including _ for blank): ")
		if re.search("[^A-z*]+", letters):
			print("Invalid characters entered, try again.")
		elif len(letters) > 7 or len(letters) < 1:
			print("Invalid number of characters entered >0 and >7 only.")
		else:
			letters = letters.lower()
			letters = ["?" if X is "_" else X for X in letters]
			break		

def appendIfLegal(word):
	#Checks if a word is legal against the dictionary and adds to found words
	global validWords	
	matches = fnmatch.filter(dictionary, word)
	matches = list(set(matches) - set(validWords))
	validWords = validWords + matches

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
	appendIfLegal(word)
	for i in range(len(myLetters)):
		if alreadyChecked(word + myLetters[i]):
			continue
		elif len(myLetters) is 1:
			permute(word + myLetters[i], "")
		else:
			permute(word + myLetters[i], myLetters[0:i] + myLetters[i+1:])

importFile()
acceptLetters()
checkedWords = []
validWords = []
start_time = time.time()
permute("", letters)
validWords.sort()
print("Code took {:.2f} seconds to run".format((time.time() - start_time)))
print(len(validWords), "valid words: ", ", ".join(validWords))








