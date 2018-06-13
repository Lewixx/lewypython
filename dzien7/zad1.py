#wydawanie reszty

monety = {5:0, 2:0, 1:0, 0.5:0, 0.2:0, 0.1:0}

zakupy = 32.70
banknot = 50

reszta = round(banknot - zakupy, 2)

wydano = 0
print(reszta)
for moneta in monety.keys():
    if reszta >= moneta:
        il_monet = round(reszta // moneta, 2)
        monety[moneta] = il_monet
        reszta = reszta - round(il_monet * moneta, 2)
        wydano += round(il_monet * moneta, 2)
        print(f'wydano {il_monet} monet {moneta}')
        print(round(reszta, 2))
        print(round(wydano, 2))

L =[1,2]
aa = L.count(L)
print(aa)
qqq = 4
qq = str(qqq)
print(qqq)
print(qq)
del qqq
