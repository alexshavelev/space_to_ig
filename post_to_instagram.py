from dotenv import load_dotenv
import os
from instabot import Bot
from config import IMAGES_FOLDER

if __name__ == '__main__':
    load_dotenv()
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    bot = Bot()
    bot.login(username=username, password=password)

    for file_name in os.listdir(IMAGES_FOLDER):
        image_path = os.path.join(IMAGES_FOLDER, file_name)
        bot.upload_photo(image_path, caption='wow! space!')
