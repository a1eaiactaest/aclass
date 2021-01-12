#!/usr/bin/env python3
import urllib.request
import tqdm
import platform
from zipfile import ZipFile


def download(url):
    urllib.request.urlretrieve(url, '/mnt/c/Users/piotr/chromedriver_win32.zip')

def download_webdriver(browser):
  if browser == 'chrome88':
    with ZipFile(download('https://chromedriver.storage.googleapis.com/88.0.4324.27/chromedriver_win32.zip'),'r') as obj:
      obj.extractall()

download_webdriver('chrome88')
