from dzien8.komputer import Komputer

class Zestaw(object):
    def __init__(self, monitor, myszka):
        self.komp = None
        self.monitor = monitor
        self.myszka = myszka

    def __str__(self):
        return f'monitor:-- {self.monitor}, myszka:-- {self.myszka}'
    #ten def str pokazuje zwraca jak ma sie printowac POLE tego obiektu gdy wyprintuje sam obiekt