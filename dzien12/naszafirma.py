from dzien12.pracownik import Pracownik

p1 = Pracownik('dan', 'monter', 4566, 1)
p2 = Pracownik('  ger wa  zy ', 'IT Dev', 10000, 3)

p1._pensja ='blaaa nie wpisuj tak'
print(p1._pensja)
#konwencja i tak moge zmienic
#print(p1.__pensja2)
print(p1._Pracownik__pensja2)

p1.__pensja2 = 3
print(p1.__pensja2)
p1.__pensja2 = 's'
print(p1.__pensja2)

print(p1.imie)
print(p2)

x = Pracownik._Pracownik__czyscstaticimie(' asd sad')
print(x)
p2.imie = Pracownik._Pracownik__czyscstaticimie(p2.imie)
print(p2)

print(p2.pesel)
p2.__pesel = 3238293089
print(p2.pesel)

p2.pesel = '472398479842'
print(p2.pesel)



