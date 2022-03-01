from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
import json
from selenium.webdriver.common.action_chains import ActionChains

MyUrl = 'https://www.douyin.com/user/MS4wLjABAAAAL9-2PNSwsCPBXIYC9EGqU-JM7ZAA7qq8KWXV1nPbVkIyreYGw5p29WmB1R2f4vtr'
NameXpath = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[2]/h1/span/span/span/span/span'
NumberXpath = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/p[1]'
FansXpath = '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]'
ImgXpath = '//*[@id="root"]/div/div[2]/div[1]/div/header/div/div/div[2]/div/div/div[2]/ul[1]/li[4]/a/div/img'
LoginXpath = '//*[@id="qdblhsHs"]/button'
WinXpath = '/html/body/div[4]/div/div/div[2]/div/div[3]/div[1]/div[4]/div[3]/button[2]/div[1]/div'

def GetName(UserUrl):
    Name = driver.find_element(By.XPATH,NameXpath).text
    Number = driver.find_element(By.XPATH,NumberXpath).text
    return Name,Number

def Login():
    driver.get('https://www.douyin.com/')
    driver.find_element(By.XPATH,LoginXpath).click()
    WebDriverWait(driver, 60).until(lambda the_driver: the_driver.find_element(By.XPATH,ImgXpath))

def Cookie():
    driver.get('https://www.douyin.com/')
    driver.delete_all_cookies()
    with open('D:/cls1277/GitHub/ForSluggard/DouyinDeleteFans/cookies.txt','r') as file:
        cookielist = json.load(file)
    for cookie in cookielist:
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)
    driver.refresh()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    Cookie()
    driver.get(MyUrl)
    # sleep(1)
    driver.find_element(By.XPATH,FansXpath).click()
    sleep(1)
    driver.find_element(By.XPATH,WinXpath).click()
    # for i in range(1000):
    sleep(1)
    actions = ActionChains(driver)
    for _ in range(100):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        sleep(1)