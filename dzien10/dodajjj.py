class Mojaklasa(object):

    def dodaj(self, a, b):
        return a + b

aa = Mojaklasa()
#wywolujemy funkcji z klasy
x = aa.dodaj(2,3)
print(x)
#nie wywolujemy funckji bo nie ma nawiasow, ale przypisujemy do miejsca w pamieci tę funkcje bez agrumentow
xx = aa.dodaj
print(xx)
#wywolujemy te funcje na innych zmiennych
xxx = xx(44,2)
print(xxx)

def odejmij(a, b):
    return a - b

z = odejmij(22,1)
print(z)
