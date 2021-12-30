for x in range(1,21):
	if x == 4 or x == 13:
		print(x , "is UNLUCKY!")
	elif x % 2 == 0:
		print(x , "is even")
	elif x% 2 != 0:
		print(x , "is odd")