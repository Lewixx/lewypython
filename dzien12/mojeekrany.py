from dzien12.ekrankyyy import Ekran

e1 = Ekran('LCD', 'samsung', 21)
e2 = Ekran('kineskop', ' amiga', 15)
e3 = Ekran('plasma', 'LG', -5)

print(e1)
print(e2)
print(e3)

print(e3.czyduzy)
print(e1.czyduzy)

#getter
#setter
e3.zmiencale = 4
print(e3.zmiencale)
print(e3.czyduzy)
print(e1.zmiencale)
