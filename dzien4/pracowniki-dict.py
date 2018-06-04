from pprint import pprint


gwiazdy = {}
gwiazdy[1] = {"imie":"john", "nazwisko":"bravo", "zarobki":2342, "status":"słaby"}
gwiazdy[2] = {"imie":"johny", "nazwisko":"rambo", "zarobki":11, "status":"mocarz"}
gwiazdy[3] = {"imie":"johnyy", "nazwisko":"deep", "zarobki":7645645, "status":"super star"}
pprint(gwiazdy)

poszukiwany = "johny rambo"

for pracownik in gwiazdy.values():
    if pracownik["imie"] + " " + pracownik["nazwisko"] == poszukiwany:
        print({pracownik["zarobki"]})


