import os
import requests
from config import IMAGES_FOLDER


def create_images_folder():
    if not os.path.exists(IMAGES_FOLDER):
        os.mkdir(IMAGES_FOLDER)


def download_and_save_image(image_name, image_url):
    res = requests.get(image_url)
    if res.ok:
        image_bin = res.content
        create_images_folder()
        save_image(image_bin, IMAGES_FOLDER, image_name)


def save_image(image, file_path, file_name):
    with open(os.path.join(file_path, file_name), 'wb') as file:
        file.write(image)
