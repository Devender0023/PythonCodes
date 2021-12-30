import random
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player score: {player_wins} Computer score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    choice1 = input("Please enter your choice: ").lower()
    if choice1 == "quit" or choice1 == "q":
        break
    if choice1:
        play = ['rock', 'paper', 'scissors']
        choice2 = random.choice(play)
        print("Computer plays " + choice2)
        if choice1 == 'rock' and choice2 == 'scissors':
            print("You won!")
            player_wins += 1
        elif choice1 == 'paper' and choice2 == 'rock':
            print("You Won!")
            player_wins += 1
        elif choice1 == 'scissors' and choice2 == 'paper':
            print("You won!")
            player_wins += 1
        elif choice1 == choice2:
            print("it's a tie!")
        else:
            print("Computer Wins!")
            computer_wins += 1
    else:
        print("You didn't make a move!")
print(
    f"FINAL SCORE.....  Player score: {player_wins} Computer score: {computer_wins}")
if player_wins > computer_wins:
    print("Congrats! You won!")
elif player_wins == computer_wins:
    print("IT'S A TIE")
else:
    print("OH NO! :-( Computer won!")
