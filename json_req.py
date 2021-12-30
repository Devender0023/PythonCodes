import requests
url = "https://icanhazdadjoke.com/search"
keyword = input("Please enter a search term for jokes: ")
response = requests.get(
	url, 
	headers = {"Accept" : "application/json"},
	params = {"term": keyword, "limit":1}
)

#print(f"your request to {url} came back with status code {response.status_code}")
#print(response.text)
data = response.json()
print(type(data["results"]))