#dwa arguemnty imie i lista domyslna, jak poda to wewnatrz funkcji to imie zostanie dodane do listy
#jak mam argument domyslny jako zlozony to wtedy robic jako None i sprawdzac ifem i tworzyc nowy pusty obiekt np Liste
def dodaj(imie: str, imiona=None):
    if imiona is None:
        imiona = []
    imiona.append(imie.capitalize())
    return imiona

anglicy = dodaj("john")
print(anglicy)
anglicy = dodaj("steven", anglicy)
print(anglicy)
anglicy = dodaj("marex", anglicy)
print(anglicy)

rosjanie = dodaj("sasha", imiona=[])
print(rosjanie)