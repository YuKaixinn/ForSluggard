from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep
import json

driver = webdriver.Chrome()
driver.get('https://www.douyin.com/')
sleep(30)
with open('cookies.txt','w') as file:
    file.write(json.dumps(driver.get_cookies()))
driver.close()