import requests
from config import SPACEX_API_URL, SPACEX_FILE_TEMPLATE
from utils import download_and_save_image


def fetch_spacex_last_launch():
    images_urls = []
    res = requests.get(SPACEX_API_URL)
    if res.ok:
        data = res.json()
        images_urls += data['links']['flickr_images']
    return images_urls


if __name__ == '__main__':
    spacex_images_urls = fetch_spacex_last_launch()
    spacex_images_urls_with_counters = list(enumerate(spacex_images_urls, 1))
    for image_num, image_url in spacex_images_urls_with_counters:
        download_and_save_image(SPACEX_FILE_TEMPLATE.format(image_num), image_url)