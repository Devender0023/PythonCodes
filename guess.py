import random

random_number = random.randint(1, 10)
while True:
	guess = int(input("Guess a number between 1 and 10: "))
	if guess > random_number:
		print("TOO HIGH!")
	elif guess < random_number:
		print("TOO LOW!")
	else: 
		print("YOU GOT IT!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1, 10)
			guess = ""
		else:
			print("Thank you for playing!")
			break

