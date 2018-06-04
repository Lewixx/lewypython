with open("wier123.txt, ","w") as plik:
    plik.write("eloo dzien dobry jestem \n")
    plik.write("wlasnie programuje\n")

    linia = ["ola\n", "ala\n", "marek", "janek"]
    linia2 = [f"{wyraz}\n" for wyraz in linia]
    plik.writelines(linia)
    plik.writelines(linia2)

    plik.seek(25)
    plik.write("\n yoo byku \n")

