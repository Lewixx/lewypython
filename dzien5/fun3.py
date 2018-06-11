zakupy = ["ser", "wino", "bulka"]

def niespodzianka(lista):
    lista.append("naszyjnik")
#funkcja mi zmodyfikwoala obiekt, dzialaja modyfikujaco
#funckaj nie musi nic oddawac, tylko dzialac w tle
# aby uzyskac informacje z funckji uzywamy return
niespodzianka(zakupy)
print(zakupy)

def l(x):
    return x**2

w = l(2)
print(w)
#KISS, DRY-dont repeat youself, SOLID , single responsibility

# argumenty domyslne
#mozemy przypisywac zmienne nie pokolei ale musimy wtedy podad x=4, 5, y=29
def nic(x, h, z="ola", y=10):
    pass

imie = "ania"
def wypisz(imie):
    """
    drukuje imie ola
    :param imie: bez znaczenia
    :return:
    """
    imie = "ola"
    print(imie)

wypisz(imie)
print(imie)
wypisz("marek")

#return wyciagnie wartosc
#nie ma konfliktu nazw, funckja jest gdzie indziej w pamieci / zmienna globalna i lokalna funkcji
imie = "ania"
def wypisz2(imie):
    """
    drukuje imie ola
    :param imie: bez znaczenia
    :return:
    """
    global imie
    imie = "ola"
    print(imie)

wypisz2(imie)
print(imie)
