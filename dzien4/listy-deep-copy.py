import copy
chemia = ["ace", "plyn do naczyn", "szampon"]
nabial = ["mleko", "maslo", "sereeek"]

zakupy5 = [chemia, nabial]
zakupy6 = copy.deepcopy(zakupy5)
zakupy7 = copy.deepcopy(zakupy5)
zakupy6[0].append("zeeeeeeel")
zakupy7.append("yooooooo")
print(zakupy5)
print(zakupy6)
print(zakupy7)

osoby.update