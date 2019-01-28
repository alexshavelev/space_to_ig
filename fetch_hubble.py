import requests
from .config import HUBBLE_API_URL, HUBBLE_FILE_TEMPLATE
from .utils import download_and_save_image


def get_hubble_collection_photos_ids(collection_name):
    url = HUBBLE_API_URL.format('images', collection_name)
    res = requests.get(url)
    images_ids = []
    if res.ok:
        for photo in res.json():
            images_ids.append(photo['id'])
    return images_ids


def get_hubble_image_url(image_id):
    url = HUBBLE_API_URL.format('image', image_id)
    res = requests.get(url)
    image_urls = []
    if res.ok:
        for image_file in res.json()['image_files']:
            image_urls.append(image_file['file_url'])
    return image_urls[-1]


def get_image_format(image_url):
    _, image_format = image_url[-10:].split('.')
    return image_format


def get_hubble_image_name(image_url, image_id):
    image_format = get_image_format(image_url)
    return HUBBLE_FILE_TEMPLATE.format(image_id, image_format)


if __name__ == '__main__':
    hubble_collection_ids = get_hubble_collection_photos_ids('holiday_cards')

    for hubble_id in hubble_collection_ids:
        hubble_image_url = get_hubble_image_url(hubble_id)
        hubble_image_name = get_hubble_image_name(hubble_image_url, hubble_id)
        download_and_save_image(hubble_image_name, hubble_image_url)
        print('downloaded', str(hubble_id))
