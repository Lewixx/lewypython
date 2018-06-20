from dzien11.pracownik import Pracownik

p1 = Pracownik('john' , 'malarz', 4234)
p2 = Pracownik('marek', 'piekarz', 6756)
p3 = Pracownik('kuba', 'it dev', 11144)

print(p1)
print(p2)
print(p3)

Pracownik.miesiac_bezurlopow = 'sierpien'

print(p1.miesiac_bezurlopow)
p2.miesiac_bezurlopow = 'czerwiec'
x = p2.miesiac_bezurlopow
print(x)
print(Pracownik.miesiac_bezurlopow)
#po zmienie trzeba usunac to poolem instacji aby worcila wartosc domyslna pola klasy
del p2.miesiac_bezurlopow
print('yoo----')
print(p2.miesiac_bezurlopow)

