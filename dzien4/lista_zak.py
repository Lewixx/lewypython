chemia = ["ace", "plyn do naczyn", "szampon"]
nabial = ["mleko", "maslo", "sereeek"]

zakupy6 = [chemia, nabial]
zakupy7 = [chemia, nabial]
zakupy8 = [chemia, nabial]
#zakupy7[0].append("zel pod przysznic")

zakupy7 = zakupy6[:]
zakupy10 = zakupy6.copy()
zakupy10.append("zelll")
print(zakupy6)
print(zakupy7)
print(zakupy8)
print(zakupy10)

zakupy9 = []
zakupy9.append([])
for z in chemia:
    zakupy9[0].append(z)
print(zakupy9)
