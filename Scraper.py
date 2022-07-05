from random import choice
import csv



def game(quotes):
    print("again")
    quote = choice(quotes)
    count = 3
    while(count >= 1):
        if count == 3:
            print(f'Gusses left {count}')
            print(f"Who is the author of this quote: {quote[0]}")
            answer = input("Make a guess about the author of this quote: ")
            if answer == quote[1]:
                print("Great! You did it.")
                count -= 1
                return menu(quotes)
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
                return menu(quotes)
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
                return menu(quotes)
            else:
                print("Better Luck next time..")
                count-=1
                return menu(quotes)


def read_quotes():
    with open("Quotes_data.csv") as file:
        quotes = csv.reader(file)
        next(quotes)
        data = list(quotes)
    return data


def menu(quotes):
    choice = input("Would you like to play again (yes/no): ")
    while (choice.lower() not in ("no","n")):
        if choice.lower() in ("yes","y"):
            print("Yes after No")
            return game(quotes)
        else:
            print("Wrong input..! Please try again!")

    print("Have a nice day!")





quotes = read_quotes()
print("Let's play a game!")
game(quotes)
