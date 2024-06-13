import requests
from bs4 import BeautifulSoup


def get_news_content(URL):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    result = requests.get(URL, headers=headers)
    try:
        soup = BeautifulSoup(result.content,'html.parser')
        print(soup)
        target = soup.find('div', {'class' :'caas-body'})
        time = soup.find_all('time')
        if len(target) <1:
            target = soup.find('div', {'id' :'Page'})
            time = soup.find_all('time')
        return target.get_text(), time
    except:
        return "failed connection", "no date available"


print(get_news_content("https://spare-parts.tiger-corporation-us.com/pages/where-to-find-model-number-for-electric-products"))