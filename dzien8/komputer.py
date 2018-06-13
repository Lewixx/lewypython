#tworze klase
class Komputer(object):
    def __init__(self, producent, typ, kolor, procesor, ram):
        self.producent = producent
        self.typ = typ
        self.kolor = kolor
        self.procesor = procesor
        self.ram = ram
        self.rok = 2018
        self.stan = False

    def wlacz(self):
        if self.stan:
            print(f'komputer {self.producent} jest juz wlaczony')
        else:
            self.stan = True
            print(f'komputer {self.producent} zostal wlasnie uruchomiony')
    def opis(self):
        print(f'komputer {self.producent} ma typ {self.typ}, zostal wyprodukowany w {self.rok} roku i ma {self.ram} pamieci RAM, jego stan uruchomienia to {self.stan}')

    def podkrec(self):
        print(self.procesor)
        print('o ile chcesz podrecic procesor? max predkos to 1000 ')
        x = input()
        x = int(x)
        if self.procesor + x > 1000:
            print('komputer sie spalil gdy chciales go podkrecic')
        else:
            self.procesor = self.procesor + x
            print(f'wlasnie podkreciles procesor o {x} do wartosci {self.procesor}')
