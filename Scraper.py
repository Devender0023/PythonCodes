import requests
from bs4 import BeautifulSoup
from random import choice


def scraping():
    print("Here")
    quotes_data = []
    HaveNext = True
    count = 1
    # print(soup.contents)
    while(HaveNext):
        url = "http://quotes.toscrape.com"
        new_url = f'{url}/page/{count}'
        response = requests.get(new_url)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")
            # print(quotes)
            # HaveNext = False

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small").get_text()
            # print(author)
            link = quote.find("a")["href"]
            new_link = f'{url}{link}'
            new_response = requests.get(new_link)
            new_soup = BeautifulSoup(new_response.text, "html.parser")
            # print(new_soup.contents)
            BirthDate = new_soup.find("span", class_="author-born-date").get_text()
            BirthPlace = new_soup.find("span", class_="author-born-location").get_text()
            author_list = [text, author, BirthDate, BirthPlace]
            # print(author_list)
            quotes_data.append(author_list)
        if soup.find("li",class_="next") is None:
            HaveNext = False
        count+=1
            # time.sleep(3)
    print("Scraping finished.")
    return quotes_data

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
