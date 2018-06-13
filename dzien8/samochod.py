#klasa
class Samochod(object):
    #dodajemy cechy do obiektu
    #self . POLE = arguemtn
    def __init__(self, marka, klima, kolor):
        self.producent = marka
        self.klima = klima
        self.kolor = kolor
        self.kolor2 = 'czarny'
        self.uruchomiony = False
        self.silnik = None

    def uruchom(self):
        if self.uruchomiony:
            print('samochod jest już wlaczony')
        else:
            self.uruchomiony = True
            print(f'{self.producent}wlasnie odpaliles swoja fure')

    def __str__(self):
        return f'{self.producent} kolor {self.kolor}'
