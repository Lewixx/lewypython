
class Pracownik(object):

    #zmienne klasy - wspolne dla wszytkich obietkow
    zarobki = {'monter': 4000, 'tokarz': 65564}
    il_pracownikow = 0

    def __init__(self, imie, pesel, stanowisko):
        self.imie = imie
        self.pesel = pesel
        self.stanowisko = stanowisko
        #self.pensja = None
        self.pensja = Pracownik.zarobki[stanowisko]
        Pracownik.il_pracownikow += 1

    def __str__(self):
        return f'{self.imie} - {self.stanowisko} - {self.pensja} - {self.pesel}'

    def ustal_zarobki(self):
        if self.stanowisko == 'monter':
            self.pensja = 5675
        elif self.stanowisko == 'tokarz':
            self.pensja = 89782
        else:
            self.pensja = 'nie ma takiego stanowska'

    def __del__(self):
        Pracownik.il_pracownikow -= 1
        print(f'Pracownik {self.imie} został usuniety, zostalo nam {self.il_pracownikow} pracownikow')
