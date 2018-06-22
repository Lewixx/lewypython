class Pracownik(object):

    ilosc_pracownikow = 0
    miesiac_bezurlopow = 'lipiec'
    premia = 2432
    roczna_podwyzka = 0.05
    _dobra_praca = True


    def __init__(self, imie, stanowisko, pensja):
        self.imie = imie
        self.stanowisko = stanowisko
        self.pensja = pensja
        Pracownik.ilosc_pracownikow += 1
        #zadko dajemy metodom instancji mozliwosc zmiany pola instancji

    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1

    def __str__(self):
        return f'pracownik {self.imie} -- pracuje jako {self.stanowisko} i zarabia {self.pensja}'

    def urlop(self):
        print('jutro biore urlop  dont care')
    def podwyzka(self, kwota):
        if self.pensja / kwota > 0.1:
            self.pensja *= 1.1
        else:
            self.pensja += kwota

    #metody klasy clasmethod i potem zmiana cls sie daje jako automat
    #dekorator classmetod
    @classmethod
    def zmienipodyzke(cls, wartosc):
        if wartosc > 0.1:
            print('na pewno? ')
            return False
        else:
            cls.roczna_podwyzka = wartosc
            return True
    @classmethod
    def obnizka(cls, liczba, _dobra_praca):
        if _dobra_praca:
            cls.premia += liczba
        else:
            cls.premia = 0

    @staticmethod
    def mojametoda():
        pass
        #metody pomocniczne, nie potrzebuja metody klasy, sprawdzajace cos
        #logicznie uzupelniaja prace modulu

    @staticmethod
    def sprawdz_pesel(pesel):
        if not pesel is not str:
            return False

        if len(pesel) != 11:
            return False
        else:
            return True
        assert isinstance(pesel, str)
        #zaloz ze pesel jest stringiem inczej wywal wyjatek, blad

