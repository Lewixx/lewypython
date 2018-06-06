#definicja funckji

def czesc():
    """

    :return:
    """
    print("siema lewix :D ")

czesc()
for i in range(22):
    czesc()

def czesc2(imie):
    """
    siema
    :param imie: str- podaj imie
    :return:
    """
    print(f"Hejj {imie.title()}")
    czesc()
# title - zamienia 1 litere na Duzą#funkcje sa dostepne w zakresie globalnym
# funkcje chcemy definiowac na poczatku programu zeby potem byly dostpe dla innych funkcji
czesc2("łukasz")
