#listy sa mutowalne

zakupy = ["piwo", "kielba", "cebula", "krewetki", "jajka"]
print(zakupy[0])

zakupy[2] = "Reds"
print(zakupy[2])
print(zakupy[2:4])
print(zakupy[::2])
print(zakupy[-1])

zakupy.append("widelce")
zakupy.append("kubki")

print(zakupy)
zakupy.insert(0,"PIWOO")
print(zakupy)
zakupy.remove("piwo")
print(zakupy)
#del usuwa dowolne element
del zakupy[4]
print(zakupy)
smieciAAA = zakupy.pop(2)
print(smieciAAA)
print(zakupy)
