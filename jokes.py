import requests
import random
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("DAD JOKES 3000!")

header = colored(header, color = "magenta")
print(header)
url = "https://icanhazdadjoke.com/search"
keyword = input("Let me tell you a joke! Give me a topic: ")
response = requests.get(url,
	headers = {"Accept" : "application/json"},
	params = {"term": keyword}
).json()
num_jokes = response["total_jokes"]
result = response["results"]
if num_jokes == 0:
	print(f"Sorry, I don't have any jokes about {keyword}! Please try again")
elif num_jokes == 1:
	print(f"I have got 1 joke about {keyword}. Here it is:")
	print(result[0]["joke"])
else:
	print(f"I have got {num_jokes} jokes about {keyword}. Here it is:")
	print(random.choice(result)["joke"])
