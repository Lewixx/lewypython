from dzien11.pracownik import Pracownik
from pprint import pprint


p1 = Pracownik('john' , 'malarz', 4234)
p2 = Pracownik('marek', 'piekarz', 6756)
p3 = Pracownik('kuba', 'it dev', 11144)

p1.miesiac_bezurlopow = 'grudzien'
p2.wlasnietododalem = True
pprint('klasa:')

pprint(Pracownik.__dict__, indent=4)

print('instancja 1')
pprint(p1.__dict__, indent=4)

print('instancja 2')
pprint(p2.__dict__, indent=4)