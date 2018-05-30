zdanie = input("podaj zdanie: ")

if "a" in zdanie:
    print("jest mala a.")
elif "A" in zdanie:
    print("jest duza A.")
    if zdanie.count("A")>2:
        print("za duzo duzych liter")
elif "o" in zdanie:
    print("jest litera o w zdaniu")
else:
    print("nic nie ma ciekawego")
