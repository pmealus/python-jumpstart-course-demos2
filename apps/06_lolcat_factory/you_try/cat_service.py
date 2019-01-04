import requests
import os
import shutil


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)  # call get data and pass it url, save data in var
    save_image(folder, name, data)  # pass save_image folder, name, and data


def get_data_from_url(url):
    response = requests.get(url, stream=True)  # call requests.get on url, store response
    return response.raw  # return response.raw which is a raw file stream?


def save_image(folder, name, data):
    filename = os.path.join(folder, name + '.jpg')
    with open(filename, 'wb') as fout:
        shutil.copyfileobj(data, fout)
