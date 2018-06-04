zakupy = {}

zakupy["chemia"] = ["ace", "plyn do naczyn", "szampon"]
zakupy["nabial"] = ["mleko", "maslo", "sereeek"]
print(zakupy)

for k in zakupy.keys():
    print(f"klucz: {k}")

for v in zakupy.values():
    print("wartosci", v)

for i, h in zakupy.items():
    print("klucz", i, "wartosci to ", h)
    
