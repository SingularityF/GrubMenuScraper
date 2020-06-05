from pyvirtualdisplay import Display
import pandas as pd
import os
import sys
import glob
import time
import requests
import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


#url = "https://google.com"
url = "https://www.yayoiken.com/menu_list/"

print("Initializing...")
display = Display(visible=0, size=(1280, 720))
display.start()

firefox_profile = FirefoxProfile()
driver = webdriver.Firefox(firefox_profile)
driver.set_page_load_timeout(90)
driver.implicitly_wait(30)
print("Initialization completed")

driver.get(url)

try:
    elems = driver.find_elements_by_css_selector('h3')
except:
    print("NOT FOUND")
#for elem in elems:
    #print(elem.text)

elems[-1].location_once_scrolled_into_view
driver.save_screenshot('abc.png')

print("Running Garbage Collection")
driver.quit()
display.stop()
