
from dodaj import dodaj

print('Witaj w moim programie.')
#teraz instrukcja
print('Podaj wybór: ')
print('W co chcesz zagrac')
print('1 - dodaj osobe')
print('2 - usun osobe')
print('3 - zakoncz program')

opcje = """Podaj wybór: 
1 - dodaj osobe
2 - usun osobe
3 - wyjdz z programu"""
print(opcje)
wybor = None


while wybor != 3:
    print(opcje)
    wybor = input('Twój wybór: ')
    
    if wybor == '1':
        osoba = input('Podaj imie: ')
        dodaj(osoba)

