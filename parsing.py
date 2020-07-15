import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time, os, sys
import zipfile, glob, shutil

DOWNLOAD_PATH = 'C:\\CSDigitalSignage'
All_File_PATH = 'C:\\Users\\Parkjinyoung\\Desktop\\ds\\temp'
Image_PATH = 'C:\\Users\\Parkjinyoung\\Desktop\\ds\\image'

#Remove all download file in download directory
if os.path.exists(DOWNLOAD_PATH):
    for file in os.scandir(DOWNLOAD_PATH):
        os.remove(file.path)
else:
    print("directory not exist")
    sys.exit()

#Remove all extract file in temp directory
if os.path.exists(All_File_PATH):
    for file in os.scandir(All_File_PATH):
        os.remove(file.path)
else:
    print("directory not exist")
    sys.exit()

#Remove all image file in images directory
if os.path.exists(Image_PATH):
    for file in os.scandir(Image_PATH):
        os.remove(file.path)
else:
    print("directory not exist")
    sys.exit()

#Make webdriver for Chrome
option = webdriver.ChromeOptions()
prefs = {'download.default_directory': DOWNLOAD_PATH}
option.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome('C:\\chromedriver.exe', chrome_options=option)

#Login
driver.get('link')
delay = 3
driver.implicitly_wait(delay)

driver.find_element_by_name("account").send_keys('id')
driver.find_element_by_name("passwd").send_keys('password')
driver.find_element_by_xpath('//*[@id="signInSpan"]').click()

time.sleep(1)

#Download link
driver.get('download link')

time.sleep(1)

#Extract zip file
targetFile = glob.glob(DOWNLOAD_PATH+'\\*.zip')
image_zip = zipfile.ZipFile(targetFile[0])
image_zip.extractall(All_File_PATH)

#Select image file 
imageFile = glob.glob(All_File_PATH+'\\*.jpg')
imageFile += glob.glob(All_File_PATH+'\\*.png')
imageFile += glob.glob(All_File_PATH+'\\*.jpeg')
imageFile += glob.glob(All_File_PATH+'\\*.gif')

for image in imageFile:
    if not 'thumb' in image:
        shutil.copy(image, Image_PATH)
