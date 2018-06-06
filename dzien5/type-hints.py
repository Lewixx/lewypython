# type hints
# w python typy sa dynamiczne, nie deklarujemy typow zmiennych
#po nazwie argumenty dac drukrotpek i dac nazwe zmiennej
def pole_trojkata(podstawa: float, wysokosc: float):
    """
    oblicza pole trojkata
    :param podstawa: podstawa
    :param wysokosc: wysokosc trojkata
    :return: wyliczy pole trojkata
    """
    return 0.5 * podstawa * wysokosc

p = pole_trojkata(123, 4.234)
print(p)

def czy_duplikaty(kolekcja: list) -> bool:
    """
    sprawdza czy sa duplkaty w liscie
    :param kolekcja: podaj liste
    :return: prawda lub fałsz
    """
    kolekcja.append("marek")
    return True

#print(czy_duplikaty(2))
print(czy_duplikaty(["ala"]))

