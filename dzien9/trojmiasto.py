import requests
import bs4

adres = 'https://trojmiasto.pl'

response = requests.get(adres)
response.raise_for_status()

with open('trojmiasto.html', 'w') as plik:
    plik.write(response.text)
