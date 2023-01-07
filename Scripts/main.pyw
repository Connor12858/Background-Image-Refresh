import os
import requests
from bs4 import BeautifulSoup
import random
import ctypes
import json
import saveImage as Save
from pathlib import Path
import http.client as httplib


class Config:
    def __init__(self, path):
        self.path = path
        self.file = open(self.path)
        self.data = json.load(self.file)
        self.collection = self.data["collection"]
        self.sources = self.data["sources"]

    def Run(self):
        pass

    def GetData(self):
        self.data = json.load(self.file)
        self.collection = self.data["collection"]
        self.sources = self.data["sources"]

    def Update(self):
        self.close()
        with open("config.json", "w") as outfile:
            json.dump(self.data, outfile)
        self.file = open(self.path)

    def close(self):
        self.file.close()


urlAddr = "https://wallpaperaccess.com"
headerStr = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36'}


def CheckWifi(url="www.google.com",
                         timeout=3):
    """
    :param url: the url to check for a connection
    :param timeout: How long to wait before determining connection
    :return: the status of a connection
    """
    connection = httplib.HTTPConnection(url,
                                        timeout=timeout)
    try:
        connection.request("HEAD", "/")
        connection.close()
        return True
    except Exception as exp:
        # print(exp)
        return False


def web_call():
    # print(urlAddr + config.collection)
    htmldata = requests.get(urlAddr + config.collection, headers=headerStr).text
    soup = BeautifulSoup(htmldata, 'html.parser')
    for item in soup.find_all('img', class_='thumb'):
        # print(item['data-src'])
        config.data['sources'].append(urlAddr + item['data-src'])
    config.Update()


def get_new_image(use_save=False):
    """
    :param use_save: If we want to use the saved images
    :return:
    """
    print("Getting a random image...")

    if use_save:
        saved = os.listdir('..\\saved/.')
        img = random.choice(saved)
        # print(img)
        path = str(Path(__file__).parent.absolute().parent.absolute()) + "\\saved\\" + img
    else:
        if len(config.data['sources']) == 0 and CheckWifi():
            print("Memory empty, re-fetching from internet...")
            web_call()
        elif len(config.data['sources']) == 0 and not CheckWifi():
            print("Memory empty and no internet, using saved images...")
            get_new_image(use_save=True)
            return

        img = random.choice(config.data['sources'])
        # print(imgSrc)
        response = requests.get(img)
        file = open("..\\random_wallpaper.jpg", "wb")
        file.write(response.content)
        file.close()
        path = str(Path(__file__).parent.absolute().parent.absolute()) + "\\random_wallpaper.jpg"
    # print(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


if __name__ == "__main__":
    global config
    config = Config('config.json')

    if config.data['ask_for_collection']:
        print("Asking for a collection name...")
        if CheckWifi():
            name = input("Collection name from " + urlAddr + "\n-> ")
            config.data['collection'] = "/" + name
            config.data['ask_for_collection'] = False
            if config.data['clear_on_new_collection']:
                config.data['sources'] = []
            config.Update()
            config.GetData()
            web_call()
        else:
            print("No Internet Available")

    collection_name = "/" + config.data['collection']
    list_of_source = config.data['sources']

    if not config.data['use_save']:
        get_new_image()
        if config.data['save_all_new']:
            Save.run()
    else:
        get_new_image(use_save=True)
    config.close()
