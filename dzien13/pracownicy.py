from pprint import pprint

p1 = {'imie': 'Adam', "nazwisko": 'Kowalski', 'wiek': 30, 'pensja': 3000}
p2 = {'imie': 'Janek', "nazwisko": 'powarzynska', 'wiek': 22, 'pensja': 12100}
p3 = {'imie': 'Marek', "nazwisko": 'sernec', 'wiek': 40, 'pensja': 6430}
p4 = {'imie': 'Paweł', "nazwisko": 'biernat', 'wiek': 55, 'pensja': 4300}

pracownik = [p1, p2, p3, p4]
#sortowanie po kluczu
#uzywanie lambdy
posortowani = sorted(pracownik, key=lambda pp : pp['wiek'])

print(posortowani)
#drukuje jako slownik
#wlasnie go posortowalem wedlug wieku
pprint(posortowani)

def sortprac(pracownik):
    return pracownik['imie']
p11 = pracownik.sort(key=sortprac(pracownik))
print(p11)