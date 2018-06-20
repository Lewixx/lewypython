from dzien11.diament import Zwierze
from dzien11.diament import KON
from dzien11.diament import Osiol
from dzien11.diament import Mul
#znaczek * importuje wszytko

z1 = Zwierze('Lew')
z1.ruszaj()
print(z1)

k1 = KON('konik', 'Kary', 'bialy')
k1.ruszaj()
print(k1)
k1.dajglos()

o1 = Osiol('stary osiolek')
o1.ruszaj()
o1.dajglos()
#o1.dajglos2()

muu = Mul('san pier')
muu.dajglos()
muu.ruszaj()
muu.pijwode()
print(muu)

help(Mul)