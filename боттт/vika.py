import requests
from bs4 import BeautifulSoup as bs

def reqst(url):
    response = requests.get(url)
    html = response.content

    soup = bs(html,"html.parser")

    result = soup.find_all(class_="hp-c4-elem")
    text = '\n'.join(paragraph.text for paragraph in result)
    with open("cookie", 'w', encoding='utf-8') as file:
        file.write(text)


