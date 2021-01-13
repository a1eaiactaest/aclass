#!/usr/bin/env python3
from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader
ChromeDriverDownloader().download_and_install()

browser = webdriver.Chrome()
browser.get('http://seleniumhq.org/')
