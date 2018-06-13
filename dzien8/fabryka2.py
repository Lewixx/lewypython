from dzien8.samochod import Samochod
from dzien8.samochod import Silnik


a1 = Samochod('Volvo', True, 'polestar blue')
s1 = Silnik(2200, 'Pb98')

a1.silnik = s1
print(a1)
print(s1)

print(f'samochod {a1.producent} ma kolor {a1.kolor} ma silnik {a1.silnik.paliwo}')
a1.silnik.uruchom
