import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.instagram.com/cristiano/')
soup = BeautifulSoup(html.text,'lxml')
item = soup.select_one("meta[property='og:description']")
name = item.find_previous_sibling().get("content").split(",")[0]
followers = item.get("content").split(",")[0]
following = item.get("content").split(",")[1].strip()
print(f'{name}\n{followers}\n{following}')