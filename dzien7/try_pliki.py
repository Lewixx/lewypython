
try:
    with open('wierszyk.txt') as plik:
        print('Moj wierszyk')
        print(plik.read())
except ValueError:
    print('zly blad podales jako except')
except Exception as e:
    print('haha poszedl wczesniejszy excep', e)
except FileNotFoundError:
    print('plik nie istenieje, podaj dobry plik ')
    with open('wiersz.txt', 'w') as plik
        pass
    
finally:
    print('i tak jest blad lol')
