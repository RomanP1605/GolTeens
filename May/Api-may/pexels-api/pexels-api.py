import requests
from tqdm import tqdm
import json
import os
import math
from pprint import pprint

# headers={"Authorization": f"xii5ahquzY22jj7mkQxTJS8CLKm8fd8SlQeOWIxRCavl6hxOueb62Hh7"}
def download_images(img_list=[],img_dir_path=''):
    for item_url in tqdm(img_list):
        response=requests.get(url=item_url)
        if response.status_code == 200:
            with open(f'./{img_dir_path}/{item_url.split("-")[-1]}','wb') as file:
                file.write(response.content)

def scrap_pixels(query=''):
    headers = {"Authorization": f"xii5ahquzY22jj7mkQxTJS8CLKm8fd8SlQeOWIxRCavl6hxOueb62Hh7"}
    query_str = f"https://api.pexels.com/v1/search?query={query}&per_page=8"
    response = requests.get(url=query_str, headers=headers)
    if response.status_code != 200:
        return f"Помилка: Статус код {response.status_code} . response.json()"
    print(response.json())
    img_dir_path = ' '.join(i for i in query.split(' ') if i.isalnum())
    # print(img_dir_path)
    if not os.path.exists(img_dir_path):
        os.mkdir(img_dir_path)
    json_data=response.json()
    with open(f'result_{query}.json','w') as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)
    img_urls = [item.get('src').get('original') for item in json_data.get('photos')]
    download_images(img_list=img_urls,img_dir_path=img_dir_path)


def main():
    query=input('Введіть слово для пошуку')
    scrap_pixels(query=query)



if __name__=='__main__':
    main()