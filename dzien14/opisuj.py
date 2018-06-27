from dzien14.descriptor_py import describe_picture
import os
from dzien14.pobieracz import pobierz
from dzien14.mscvv import get_pic_info

pics = [
'https://qph.ec.quoracdn.net/main-qimg-71e8b8cddfce751d8e0a8ed45b316731-c',
'https://i.pinimg.com/originals/7c/3a/ed/7c3aedde4dbf1c38e5d34a554a8cb4eb.jpg',
'http://cdn30.us1.fansshare.com/image/vladimirputin/vladimir-putin-walking-away-from-things-2125699510.jpg',
'http://s.eatthis-cdn.com/media/images/ext/543627202/happy-people-friends.jpg',
'http://ocdn.eu/jcmsprzegladsportowy-transforms/1/HpvktoATGh0dHA6Ly9vY2RuLmV1L2pjbXNwcnplZ2xhZHNwb3J0b3d5L2E2YTU1NDJlLThhYjMtNGNjNi1iZGUxLThiOTAyM2QwYzU5OS5qcGeRkwIAzQQa'
]

podfolder = ".//opisane_fotki"

if not os.path.exists(podfolder):
    os.mkdir(podfolder)

name_pattern = '{katalog}//pic{nr}.jpg'

for i, pic in enumerate(pics):
    img_saved = name_pattern.format(katalog=podfolder, nr=i+1)
    print(f'----------------------Zdjecie {i+1}------------')
    print('analizuje zdjecie')
    img_data = get_pic_info(pic, img_saved)

    print('pobieram zdjecie oryginalne')
    pobierz(pic, img_saved)

    describe_picture(img_saved, img_data)