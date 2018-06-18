from dzien10.towary import Towar

class RTV(Towar):
    def __init__(self, nazwa, producent, ekran):
        self.ekran = ekran
        kolor = 'biały'
        Towar.__init__(self, nazwa, producent, None)

    def __str__(self):
        return f'{self.nazwa} -- {self.producent} -- {self.ekran} -- {self.cena}'

def main():
    r1 = RTV('super monitor', 'LG','LCD')
    r2 = RTV('stary dziad', 'samsung', 'kineskop')
    r1.cena = 423
    print(r1)
    print(r2)
    r2.producent = 'BOSSSCH'
    r2.cena = 11
    print(r2)

if __name__ == '__main__':
    main()
