def licz_samogloski(zdanie: str):
    zdanie.strip().lower()
    #funcion chaining, kolka funkcji naraz strip a potem lower
    x = 0
    #kolekcja samoglosek
    #dla kazdego znaku w zdaniu
        #jesli znak w samogloskach zwieksz licznik o 1
    #x = x + zdanie.count("a")
    #x = x + zdanie.count("u")
    lista = ["e", "a", "i"," u", "o"]
    for znak in zdanie:
        if znak in lista:
            x = x +1

    return x
x = licz_samogloski("ala ma konta a marekcz ma piwko")
print(x)