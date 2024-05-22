from bs4 import BeautifulSoup
import requests

url = "par.html"
# url = "https://www.pythonanywhere.com/forums/topic/7002/"
with open(url) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
# from bs4 import BeautifulSoup
# import requests
#
# # Replace 'url' with the URL of the website you want to scrape
# url = 'https://example.com'
# response = requests.get(url)
# html_content = response.text


# Find all <th> tags with scope="rowgroup"
rowgroup_th_tags = soup.find_all('th', {'scope': 'rowgroup'})

game_data = []

for th_tag in rowgroup_th_tags:
    # Extract game name
    game_name = th_tag.find('a').text

    # Extract release date
    release_date = th_tag.find('b').find_next_sibling().strip()

    game_data.append({
        'game_name': game_name,
        'release_date': release_date
    })

# Print the extracted data
for game in game_data:
    print(f"Game: {game['game_name']}")
    print(f"Release Date: {game['release_date']}\n")