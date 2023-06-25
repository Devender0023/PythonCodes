while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError:
		print("The number should be an integer")
	else:
		print("Good job you entered a number! This is a test.")
		break
	finally:
		print("RUNS NO MATTER WHAT!")