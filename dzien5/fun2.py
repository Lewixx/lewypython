#funckaj co bedzie drukwoac na ekranie ilosc litery w danym stringu

def licz(litera, zdanie):
    """liczy ile liter jest w zdanie, ma dwa arguemnty, mam podac stringi jako argimenty"""
    ilosc = zdanie.count(litera)
    print(f"Litera {litera} wystepuje {zdanie.count(litera)} razy w zdaniu {zdanie}")
    return ilosc

licz("a", "Ala ma kota a hannia pieska")
ilosc = licz("e", "jasnika rzepungi i bartuhi gaganetsa")
print(ilosc)
# zwraca odrocony string

def odwroc(zdanie):
    """
    odrwaca mi ydanie
    :param zdanie:  str podaj ydanie od odrwocenia
    :return: pddaje odworcene zdanie
    """
    zdaaa = zdanie[::-1]
    return zdaaa

zda = odwroc("eloo jestem na rybach")
print(zda)
print(odwroc("rzepunga ma grubera"))



