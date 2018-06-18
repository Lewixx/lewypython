from dzien10.towary import Towar
#obiekty moga byc poliformiczne, moga meic weiele typow
#Polainstancji jakie sa mu rodzica tez musza byc u dziecka
class AGD(Towar):
    def __init__(self, nazwa, producent, cena, typ):
        self.typ = typ
        super().__init__(nazwa, producent, cena)
        self.wlaczony = False

    def wlacz(self):
        if not self.wlaczony:
            self.wlaczony = True
    def __repr__(self):
        return f'{self.nazwa} {self.typ}'

def main():
    lodowka = AGD('Ladowka', 'LG', 5345, 'do zabudowy')
    mixer  = AGD('Mixer', 'BOSCH', 100, ' wolny')

    agd = [lodowka, mixer]
    print(agd)

if __name__ == '__main__':
    main()