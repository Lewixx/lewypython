with open("wierszyk", "r", encoding="utf-8") as plik:
    linijka = plik.readlines()
    print(linijka)
    print(plik.readline(), end="")
    for wers in linijka:
        print(wers)
     