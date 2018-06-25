class Pracownik(object):

    @staticmethod
    def __czyscstaticimie(imie):
        return imie.strip().title()

    def __init__(self, imie, stanowisko, pensja, pensja2):
        self.imie = imie
        self.stanowisko = stanowisko
        self._pensja = pensja
        self.__pensja2 = pensja2
        self.__pesel = None

    def __czyscimie(self, imie):
        return imie

    def __str__(self):
        return f'{self.imie} -- {self.stanowisko} -- {self._pensja}'

    def zmienpensje(self, nowa_pensja):
        if nowa_pensja is int and nowa_pensja <= 6000:
            self.__pensja2 = nowa_pensja

    def pokazpensje(self):
        return self.__pensja2

    @property
    def pesel(self):
        if self.__pesel:
            return self.__pesel
        else:
            return f'cos zle'

    @pesel.setter
    def pesel(self, wartosc2):
        if not isinstance(wartosc2, str) and len(wartosc2) != 11:
            return f'cos zle wpisales'
        self.__pesel = wartosc2