
from dzien9.pracownik import Pracownik

p1 = Pracownik('Jan', 91050610269, 'monter')
p2 = Pracownik('Andrzej', 91060610456, 'monter')
p3 = Pracownik('Adam', 92050412384, 'tokarz')

p1.ustal_zarobki()
p2.ustal_zarobki()
p3.ustal_zarobki()

print(p1)
print(p2)
print(p3)

print(p1.pensja)
print(p2.pensja)
#mozna sie dostac przez cala ke
print(f'obecna liczba pracownikow to: {Pracownik.il_pracownikow}')
print(Pracownik.il_pracownikow)
p2.__del__()
del p1
#mozna przez instancje bo ma dostep
print(p3.il_pracownikow)
#python usuwa na koncu ibiekty