class Ekran(object):

    def __init__(self, typ, producent, cale):
        self.typ = typ
        self.producent = producent
        self.__cale = cale

    def __str__(self):
        return f'{self.producent} -- {self.typ}'

    @property
    def czyduzy(self):
        if self.__cale > 0:
            return self.__cale
        else:
            return 'chyba zle stworzyles instancje monitor'

    @czyduzy.setter
    def zmiencale(self, nowecale):
        if self.__cale < 17:
            self.__cale = nowecale
            return  self.__cale
        else:
            return f'dobre sa cale :D '