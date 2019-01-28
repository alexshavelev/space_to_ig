import os
import requests
from config import IMAGES_FOLDER


def create_images_folder():
    if not os.path.exists(IMAGES_FOLDER):
        os.mkdir(IMAGES_FOLDER)


def download_and_save_image(image_name, image_url):
    image_bin = download_image(image_url)
    create_images_folder()
    save_image(image_bin, IMAGES_FOLDER, image_name)


def download_image(url):
    res = requests.get(url)
    return res.content


def save_image(image, file_path, file_name):
    with open(os.path.join(file_path, file_name), 'wb') as file:
        file.write(image)
