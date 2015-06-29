for i in range(1, 100):
	if i % 3 is 0:
		if i % 5 is 0:
			print("CracklePop")
		else: 
			print("Crackle")
	elif i % 5 is 0:
		print("Pop")
	else:
		print(i)
		