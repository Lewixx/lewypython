class Towar(object):
    def __init__(self, nazwa, kolor, cena):
        self.nazwa = nazwa
        self.kolor = kolor
        self.cena = cena

    #overright - nadpisana metoda w obiekcie
    def __str__(self):
        return f'{self.nazwa.capitalize} {self.kolor} {self.cena}'

  #  def __add__(self, other):
   #     return self.cena + other.cena

    def __lt__(self, other):
        if self.cena < other.cena:
            return True

def main():
    t1 = Towar('krzeszlo', 'czarne', 234.76)
    t2 = Towar('stoleczek', 'niebieskie', 6433)
    t3 = Towar('fotel', "bialy", 121)
    print(t1)
    sklep = [t1, t2, t3]
    wartosc = 0
    #for przedmiot in sklep:
     #   wartosc =+ przedmiot
    if t1 < t2:
        True

if __name__ == '__main__':
    main()

main()

