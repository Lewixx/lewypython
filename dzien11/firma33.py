from dzien11.pracownik import Pracownik
from pprint import pprint


p1 = Pracownik('john' , 'malarz', 4234)
p2 = Pracownik('marek', 'piekarz', 6756)
p3 = Pracownik('kuba', 'it dev', 11144)

p1.podwyzka(123)
print(p1.pensja)

Pracownik.zmienipodyzke(0.11)
#tak nie robimz nie ymieniamz pola klasz metodamz instancji
#p1.zmienipodyzke(0.2)
#p2.zmienipodyzke(0.02)
#p3.zmienipodyzke(0.05)
print(p1.roczna_podwyzka)
print(p2.roczna_podwyzka)
print(p3.roczna_podwyzka)

print(p1)
print(p1.premia)
p1.obnizka(325, True)
print(p1.premia)
p1.obnizka(123, False)
print(p1.premia)
#python  jezyk otwarty, artybuty publicznie dostepne
#jedno podkreslenei prywatna metoda, pole nie zmieniaj jej

wynik = Pracownik.sprawdz_pesel('111231')
Pracownik.sprawdz_pesel('123123')
print(wynik)
wynik2 = Pracownik.sprawdz_pesel('82467548029')
print(wynik2)
