#po podaniu nazwy miesiaca program pdoa liczbe dni
m = input("podaj miesiac: ")

if m == "styczen" or m == "marzec" or m == "maj" or m == "lipiec" or m =="sierpien" or m =="pazdziernik" or m == "grudzien":
    print(f" {m} ma 31 dni")
elif m == "kwiecien" or m == "czerwiec" or m == "wrzesien" or m == "listopad":
    print("mieisac ma 30 dni")
elif m=="luty":
    print(f" {m} ma 28 lub 29 dni")
else:
    print("nie podales meisiaca")

