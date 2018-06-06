def info_kursant(imie, nazwisko, kurs="python", tryb="wieczorowy"):
    """
    zwaraca informacje o kursancie
    :param imie: imie kursant
    :param nazwisko: nazwisko
    :param kurs: kurs
    :param tryb:
    :return:
    """
    return f"{imie.title()} {nazwisko.title()} kurs: {kurs} w trybie: {tryb}"
kursant1 = info_kursant("marek", "mazurek")
print(info_kursant("lukasz", "lewicki"))
print(kursant1)
kursant2 = info_kursant("anna", "mazurek", "java", "dzienny")
print(kursant2)
kursant3 = info_kursant("kuba", tryb="dzien", kurs="javascript", nazwisko="rzepka")
print(kursant3)
