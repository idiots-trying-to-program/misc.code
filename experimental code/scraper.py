#this doesnt work, im trying to fix it - rumodeus
from bs4 import BeautifulSoup
import urllib.request

import requests
from bs4 import BeautifulSoup
url = 'https://www.pixiv.net/en/tags/rumia/artworks'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
i = 0
for img in soup.find_all('img'):
    try:
        img_url = img.get('src')
        response = requests.get(img_url)
        with open(f'./image_{i}.jpg', 'wb') as f:
            f.write(response.content)
        i += 1
    except ValueError:
        continue
