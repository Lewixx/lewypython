from dzien10.AGD import AGD

#inicjalizator dowolny, ale potem i tak musze wszystkie przekazac
class lodowka(AGD):
    def __init__(self, nazwa, producent):
        self.pojemnosc = None
        self.kostkarka = None
        #super(lodowka, self).__init__()
        #odowlac sie bezposrednoi do rodzica tutaj jest jeszcze cena i typ
        AGD.__init__(self, nazwa, producent, None, None)

    def uzupelnij(self, cena, typ):
        self.cena = cena
        self.typ = typ
    def montujK(self):
        if self.kostkarka is False or self.kostkarka is None:
            self.kostkarka = True

def main():
    l1 = lodowka('P210', 'samsung')
    print(l1)
    l2 = lodowka('GA200', 'BOSCH')
    l2.montujK()
    print(f'lodowka i kostakrka: {l2.kostkarka}')
    print('-----------------------------')
    print(f'l1 is l2: {l1 is l2}')
    y = l1
    print(f'l1 is y: {l1 is y}')


if __name__ == '__main__':
    main()
