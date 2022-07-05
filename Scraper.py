
from random import choice




def game(quotes):
    quote = choice(quotes)
    count = 3
    while(count > 0):
        if count == 3:
            print(f'Gusses left {count}')
            print(f"Who is the author of this quote: {quote[0]}")
            answer = input("Make a guess about the author of this quote: ")
            if answer == quote[1]:
                print("Great! You did it.")
                count -= 1
                menu(quotes)
            else:
                count-=1
                continue
        elif count == 2:
            print(f'Gusses left {count}')
            print(f'Here is a hint for you, the author was born on {quote[2]}.')
            answer = input("Make a guess about the author of this quote: ")
            if answer == quote[1]:
                print("Great! You did it.")
                count -=1
                menu(quotes)
            else:
                count-=1
                continue
        elif count == 1:
            print(f'Gusses left {count}')
            print(f'Here is another hint for you, the author was born {quote[3]}.')
            answer = input("Make a guess about the author of this quote: ")
            if answer == quote[1]:
                print("Great! You did it.")
                count -= 1
                menu(quotes)
            else:
                print("Better Luck next time..")
                count-=1
                break

    menu(quotes)



def menu(quotes):
    choice = input("Would you like to play again (y/n): ")
    while (choice != 'n'):
        if choice == 'y':
            game(quotes)
        else:
            print("Wrong input..! Please try again!")

    print("Have a nice day!")






quotes = scraping()
print("Let's play a guess game!")
print("Game starts here..")
game(quotes)
