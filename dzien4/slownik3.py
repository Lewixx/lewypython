aktorzy = [["john", "travolta", 523, "nowy"], ["john", "rambo", 66445, "stary"], ["johny", "bravo", 7623232, "super"]]
print(aktorzy)
print(aktorzy[0])
aktorzy.append(["joohny", "turko", 11, "slaby"])
print(aktorzy)
szukany = "rambo"

for a in aktorzy:
    if a[1] == szukany:
        print(szukany, "ma stawke", a[2])

