from dzien12.kalkulator import *
from unittest import TestCase
from dzien12.testredirect import get_print_output

class TestsKalkulator(TestCase):
    #tu pisze metody jakie chce tesotwac
    #jedna klasa odpowiada jednemu testowi

    def test_dodaj(self):
        #trzy A
        #arrange przypisz
        a = 4
        b = 7
        wynik_oczekiwany = 11
        #act - dzialaj
        wynik_rzeczywisty = dodaj(a, b)

        #assest sprawdzenie czy oczwikwany rowna sie rzecywistemu
        self.assertEqual(wynik_oczekiwany, wynik_rzeczywisty, 'tescik dziala')

    def test_pomnoz(self):
        a = 2
        b = 10
        wynik1 = '20\n'

        wynik2 = get_print_output(pomnoz, a, b)

        self.assertEqual(wynik1, wynik2)