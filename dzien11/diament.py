

class Zwierze(object):

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def ruszaj(self):
        print(f'zwierze {self.nazwa} poruszyło sie')

    def dajglos(self):
        raise NotADirectoryError('zaimplementuj dziadu')
    #chce aby kazda klasa dziecko nadpisala to funckje a nie korzystala z ogolnej
    def dajglos2(self):
        raise NotADirectoryError('zaimplementuj dziadu')

class KON(Zwierze):
    def __init__(self, nazwa, imie, umaszczenie):
        self.imie = imie
        self.umaszczenie = umaszczenie
        Zwierze.__init__(self, nazwa)
    def ruszaj(self):
        print(f'KOn {self.nazwa} {self.imie} hasa po lace')

    def dajglos(self):
        print(f'Kon {self.imie} -- mowie patattaaj')

    def __str__(self):
        return f'{self.nazwa} -- {self.umaszczenie}'

class Osiol(Zwierze):
    def ruszaj(self):
        print(f'jestem stary osiol nie chce mi sie.')

    def dajglos(self):
        print(f'jestem osiol {self.nazwa} muuuuuuuuuu')

    def pijwode(self):
        print('pij wode')

class Mul(Osiol, KON):
    def __init__(self, nazwa):
        Osiol.__init__(self.nazwa)
        self.umaszczenie = None