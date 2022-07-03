import requests
from bs4 import BeautifulSoup
import csv


url = f'https://www.rithmschool.com/blog'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("Blog_data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Title","Link","Date"])

    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        # print(article.find("a").attrs["href"])
        link = a_tag["href"]
        date = article.find("time")["datetime"]
        writer.writerow([title,link,date])



