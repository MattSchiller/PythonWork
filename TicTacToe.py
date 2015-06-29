#python

BoardNumbers = [1,2,3,4,5,6,7,8,9]
BoardState = [" "," "," "," "," "," "," "," "," "]
i = 0
while i < len(BoardNumbers):
	print(BoardNumbers[i],"|", BoardNumbers[i+1], "|", BoardNumbers[i+2])
	print("_________")
	i = i+3


	
