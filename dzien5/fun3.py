zakupy = ["ser", "wino", "bulka"]

def niespodzianka(lista):
    lista.append("naszyjnik")
#funkcja mi zmodyfikwoala obiekt, dzialaja modyfikujaco
#funckaj nie musi nic oddawac, tylko dzialac w tle
# aby uzyskac informacje z funckji uzywamy return
niespodzianka(zakupy)
print(zakupy)

def l(x):
    return x**2

w = l(2)
print(w)
#KISS, DRY-dont repeat youself, SOLID , single responsibility

# argumenty domyslne
#mozemy przypisywac zmienne nie pokolei ale musimy wtedy podad x=4, 5, y=29
def nic(x, h, z="ola", y=10):
    pass
