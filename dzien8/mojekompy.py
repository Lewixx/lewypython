from dzien8.komputer import Komputer
from dzien8.zestaw import Zestaw

ibm = Komputer('IBM', 'laptop', 'czarny', 342, 434 )

ibm.opis()
ibm.wlacz()
ibm.wlacz()
ibm.podkrec()

superzestaw = Zestaw('monitor 24cali', 'myszka logitech')
Zestaw.komp = ibm
superzestaw.komp = ibm

#print(superzestaw.komp.procesor)
print(f'Koputer marki {superzestaw.komp.producent} ma teraz {superzestaw.komp.procesor} MHz')
#print(superzestaw.komp.typ)
print(f'Ten komputer został oddany do uzytku w {superzestaw.komp.rok} roku')
print(f'ten magiczny komputer ma {superzestaw.komp.ram} pamieci RAM')
print(f'Przesyłamy tobie wielki {superzestaw.monitor} więc możesz ogladacz mecz Polski')
print(f'W zestawie jest myszka {superzestaw.myszka}')
print(superzestaw)
