import requests
from bs4 import BeautifulSoup
from random import choice


def scraping():
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
            print(author)
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

    return quotes_data

def game(quotes):
    while()
    quote = choice(quotes)
    print("Let's play a game!")


