#webscraping
#wchodzi na strone i wyciaga wiadomosci
#musimy wiedziec co chcemy z takiej stony sciagac
#sa narzedzia developerskie
# modul jaki sluzy do webstraping, bardzo aktywny, top 3 popularnosci  request

import requests
import bs4

from pprint import pprint

#przypisuje do zmiennej, GET uzywamy do odczytu tej strony
response = requests.get('http://trojmiasto.pl')
print(response.status_code)
#sprawdzam kod odpoweidzi jaki dostajemy 200 - ze wszystko jest w porzadku, 400 - blad po stronie klienta
response.raise_for_status()
pprint(response.text)

#tez sprawdza status
#bs4 - do szukania elelmentow w html

with open('trojmiasto.html', 'w') as plik
    plik.write(odpoiedz.text)