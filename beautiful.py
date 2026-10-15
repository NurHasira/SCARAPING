import requests
from bs4 import BeautifulSoup
url = "https://id.wikipedia.org/wiki/Daftar_kabupaten_dan_kota_di_Sulawesi_Selatan"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title

print(title)

import requests
from bs4 import BeautifulSoup
url = "https://id.wikipedia.org/wiki/Daftar_kabupaten_dan_kota_di_Sulawesi_Selatan"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find('h1')

print(title)

import requests
from bs4 import BeautifulSoup
url = "https://id.wikipedia.org/wiki/Daftar_kabupaten_dan_kota_di_Sulawesi_Selatan"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("div", class_="mw-parser-output")

print(title.get_text(strip=True))

import requests
from bs4 import BeautifulSoup
url = "https://id.wikipedia.org/wiki/Daftar_kabupaten_dan_kota_di_Sulawesi_Selatan"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find_all("div", class_="mw-parser-output")

for item in title:
    print(item.get_text(strip=True))

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://id.wikipedia.org/wiki/Daftar_kabupaten_dan_kota_di_Sulawesi_Selatan"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("li")

data = []

for item in titles:
    data.append(item.get_text(strip=True))

print(data)

df = pd.DataFrame(data, columns=["title"])
df.to_csv("chomsky.csv", index=False)

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")

soup1 = BeautifulSoup(html.read(), "html.parser")
print("Dengan html.parser:", soup1.h1.get_text())

html = urlopen("http://pythonscraping.com/pages/page1.html")
soup2 = BeautifulSoup(html.read(), "lxml")
print("Dengan lxml:", soup2.h1.get_text())

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title is None:
    print('Title could not be found')
else:
    print(title.get_text())