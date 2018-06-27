import requests
import json
import os

from dzien14.pobieracz import pobierz

current = "http://xkcd.com/info.0.json"
comic_pattern = "http://xkcd.com/{num}/info.0.json"
json_data = None

folder = os.path.join(os.getcwd(), "xkcd_comics")

def get_current_comic():
    #pobieram info o aktualnym komiksie
    #upewniam sie zeJEST OK dobra odpowiedz
    global json_data
    response = requests.get(current)
    response.raise_for_status()
    #zapisuje json z info
    json_data = json.loads(response.text, encoding='utf-8')
    with open('current.json', 'w') as plik:
        json.dump(json_data, plik, ensure_ascii=False, indent=4)
    #sprawdze numer aktualnego komiksu

    #pobiore x komikwos wstecz

def get_comic_link(url):
    response = requests.get(url)
    return json.loads(response.text)['img']

def main():
    get_current_comic()
    pic_url = json_data['img']
    last_comic_num = json_data['num']
    pobierz(pic_url, 'komiks0.png')
    if not os.path.exists(folder):
        os.mkdir(folder)

    for x in range(1, 6):
        comic_url = comic_pattern.format(num=last_comic_num - x)
        pic_link = get_comic_link(comic_url)
        pic_name = os.path.basename(pic_link)
        pic_path = os.path.join(folder, pic_name)
        pobierz(pic_link, pic_path)
        print(f'zapisalem komiks nr {x}')
        print(f"scizka zapisu: {pic_path}")

if __name__ == '__main__':
    main()