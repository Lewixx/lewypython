# czy liczba jest podzielna przez 3 lub 5 lub 7

liczba = input(" podaj liczbe: ")

if liczba.isdigit():
    liczba = int(liczba)
else:
    print("zla liczba")
    exit(1)

if liczba % 3 == 0:
    print("dzieli sie przez 3")
elif liczba % 5 == 0:
    print(f"liczba {liczba} jest podzielna przez 5")
elif liczba % 7 == 0:
    print("liczba", liczba, "dzieli sie przez 7")
