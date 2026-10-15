import requests
res = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')
print(res.status_code)
print(res.content)

from urlib.request import urlopen
html = urlopen ("https://id.wikipedia.org/wiki/Daftar_kabupaten_dan_kota_di_Sulawesi_Selatan")
print(html.read())

from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html")
content = html.read()
print(content)

