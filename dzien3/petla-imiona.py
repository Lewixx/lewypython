imiona = ["ala", "ola", "marek", "karol"]
nazwisko = ["pokor", "lewix", "zepa", "szałwa"]

index = 0

for i in imiona:
    print(f"{index + 1}: {i}")
    index += 1

for index, i in enumerate(imiona):
    print(f"{index + 1}: {i}")

wpis = 0
for i in imiona:
    print(f"{i} {nazwisko[wpis]}")
    i =+ 1
    wpis =+ 1
    zip