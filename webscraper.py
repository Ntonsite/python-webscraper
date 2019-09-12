from bs4 import BeautifulSoup
import requests
import json

url = 'http://accessbank.co.tz/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

with open('twitterData.json', 'w') as outfile:
    json.dump(content, outfile)