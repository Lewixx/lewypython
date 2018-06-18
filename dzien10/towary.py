#najbardziej ogolna klasa dziedziczaca po obiekcie
class Towar(object):
    def __init__(self, nazwa, producent, cena):
        self.nazwa = nazwa
        self.producent = producent
        self.cena = cena

    def __str__(self):
        return f'{self.nazwa} - {self.producent} - {self.cena}'
    #reprezentacja dla programisty ladniej sie drukuje w princie instancje
    def __repr__(self):
        return f'{self.nazwa} // {self.cena}'

def main():
    t1 = Towar('krzeszlo', 'czarne', 234.76)
    t2 = Towar('stoleczek', 'niebieskie', 6433)
    t3 = Towar('fotel', "bialy", 121)
    sklep = [t1, t2, t3]
    print(t1)
    print(sklep)

if __name__ == '__main__':
    main()

