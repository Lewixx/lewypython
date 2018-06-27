import json, os, requests

api_key = ""
api_url = "https://westeurope.api.cognitive.microsoft.com/vision/v1.0/analyze"

headers = {
    'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': api_key
}
param = {'visualFeatures': 'Categories,Description,Faces,Adult', 'details': 'Celebrities'}

def get_pic_info(pic_url, pic_name):
    body = {'url': pic_url}
    r = requests.post(api_url, json=body, headers=headers, params=param)

    r.raise_for_status()
    response_json = json.loads(r.text)
    f_info = os.path.splitext(pic_name)

    with open(f'{f_info[0]}.json', 'w') as file:
        json.dump(response_json,  file, indent=4, ensure_ascii=False)
    return response_json

def has_faces(data: dict):
    if len(data['faces']):
        return True
    else:
        return False

def get_face_rect(face_data: dict):
    rect = face_data['faceRectangle']
    return [
        rect['left'],
        rect['top'],
        rect['left'] + rect['width'],
        rect['top'] + rect['height']
    ]

def get_caption(data):
    captions = data['description']['captions']

    if len(captions):
        return captions[0]['text']
    else:
        return 'no caption'