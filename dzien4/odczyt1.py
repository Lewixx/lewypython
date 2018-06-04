plik = open("wierszyk", encoding="utf-8")
tekst = plik.read()

print(tekst)

plik.close()

with open("wierszyk", "r", encoding="utf-8") as pliczek:
    tekst2 = pliczek.read()
    print(tekst2)

with open("wierszyk", "r", encoding="utf-8") as pliczek3:
    tekst3 = pliczek3.read(44)
    print(tekst3)
#pozycja kursowa
with open("wierszyk", "r", encoding="utf-8") as pliczek:
    print(pliczek.tell())
    tekst2 = pliczek.read(44)
    print(pliczek.tell())
    print(tekst2)
