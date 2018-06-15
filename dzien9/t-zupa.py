import requests
from bs4 import BeautifulSoup
from pprint import pprint

adres = 'https://trojmiasto.pl'
odpowiedz = requests.get(adres)

trojmiasto_zupa = BeautifulSoup(odpowiedz.text, 'html.parser')

linki = trojmiasto_zupa.select('.news-list a')
pprint(linki)
#for link in linki:
 #   print(link.get_text()) #dostaje tylko tytuly to co bylo pomidzy " ....... " w liscie
  #  print(link.attrs)

for link in linki:
    print(f"wiadomosci: {link.get('title')}")
    #print(f'wiadomosci: {link['title']}')
    print(link.get('href'))
    print('------------------------')