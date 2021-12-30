import requests
url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers = {
	"Accept" : "text/plain"
	})

#print(f"your request to {url} came back with status code {response.status_code}")
print(response.text)