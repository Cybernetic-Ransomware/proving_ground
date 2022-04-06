import requests
from bs4 import BeautifulSoup
from googletrans import Translator          # instal by: pip install googletrans==4.0.0-rc1


html_text = requests.get('https://genius.com/Mokoma-toinen-ihminen-lyrics').text
soup = BeautifulSoup(html_text, 'lxml')

origin = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-6 jYfhrf')
origin_text = ''

for x in origin:
    for br in soup.find_all("br"):
        br.replace_with("\n")
    origin_text += x.text

translator = Translator()
result = translator.translate(origin_text, src='fi', dest='en')

# print(result.origin)
print(result.text)
