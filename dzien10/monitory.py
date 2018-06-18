from dzien10.RTV import RTV

class Monitor(RTV):
    def __init__(self, cale, drzemka):
        self.cale = cale
        self.drzemka = drzemka
        self.minut = 5
        self.autoclose = True
        RTV.__init__(self, None, None, None)

    def __str__(self):
        return f'{self.nazwa} - {self.producent} - {self.cena} - {self.ekran} - {self.cale} {self.drzemka} ' \
               f' {self.minut}'

def main():
    m1 = Monitor(23, 'działa')
    m1.nazwa = 'bosch'
    m2 = Monitor(31, 'brak drzemki')
    m2.ekran = 'LCD'
    m2.nazwa = 'super monitor'

    print(m1)
    print(m2)

if __name__ == '__main__':
    main()

