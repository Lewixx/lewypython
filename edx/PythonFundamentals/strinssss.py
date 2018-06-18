
zdanko  = 'elegancko dzisiaj'
for litera in zdanko:
    print(litera)


nowezdanko = ''
for lit in zdanko:
    if lit.lower() == 'a':
        nowezdanko += lit.upper()
    else:
        nowezdanko += lit

print('zamienilem ')
print(zdanko)
print('na ')
print(nowezdanko)

#slice i odwrocenie
print(nowezdanko[::-1])

zd1 = 'zajebisty dzisiaj dzionek byl kupilem duzo co trzeba'
dluosc = len(zd1)
polowoa = int(dluosc / 2)
print(dluosc)
print(zd1)
print(polowoa)
print(zd1[:polowoa])
print(zd1[polowoa:])

liczbaa = zd1.count('a')
liczbai = zd1.count('i')
print('a ', liczbaa)
print('b ', liczbai)

indexxx = zd1.find('a')
print(indexxx)
indexxxx = zd1.find('e',12,45)
print(indexxxx)

