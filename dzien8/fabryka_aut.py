
from dzien8.samochod import Samochod


#tworze instancje
volvo = Samochod('volvo', True)
#uzywamy kropki aby dostac sie do cech
#volvo.producent

print(type(volvo))
print(volvo.producent)
print(volvo.klima)
print(volvo.kolor)
print(volvo.kolor2)
bmw = Samochod('BMW', True)
print(bmw.producent)
print(bmw.klima)
bmw.kolor2 = 'czerwony'
print(bmw.kolor2)
volvo.uruchom()
volvo.uruchom()
