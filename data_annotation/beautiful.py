import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Main_Page'  # Replace with the target website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

games = soup.find_all('th', scope='rowgroup', id='GAME', rowspan=2)
print(games)
for game in games:
    title = game.find('div', class_='fn').find('i').find('a').text
    release_date = game.find_next_sibling('b').text
    print(f"Game: {title}\nRelease Date: {release_date}\n")
