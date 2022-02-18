from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import xlwt

filepath = "stu1.txt"
url = "https://513574.yichafen.com/public/queryscore/sqcode/MsjcIn5mNjQzOXw0Nzk1M2Q0Y2QwNTBiY2UxOThlMWMzYzllMTQ1Mjc3N3w1MTM1NzQO0O0O.html"
theclass = 7
classinput = '//*[@id="queryForm"]/table/tbody/tr[1]/td[2]/input' #XPATH
nameinput = '//*[@id="queryForm"]/table/tbody/tr[2]/td[2]/input'
buttonclick = '//*[@id="yiDunSubmitBtn"]'

file = open(filepath,'r')
names = file.readlines()
driver = webdriver.Chrome()
driver.get(url)
exl = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = exl.add_sheet('score',cell_overwrite_ok=True)
row = 0 #表头自行添加

for name in names:
    row += 1
    driver.refresh()
    driver.find_element(By.XPATH,classinput).send_keys(theclass)
    driver.find_element(By.XPATH,nameinput).send_keys(name)
    driver.find_element(By.XPATH,buttonclick).click()
    sleep(1)
    for i in range(2,11):
        path = '//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td['+str(i)+']'
        mytext = driver.find_element(By.XPATH,path).text
        if i>3:
            sheet.write(row,i-2,float(mytext))
        else:
            sheet.write(row,i-2,mytext)
    driver.back()
driver.close()
exl.save('score.xls')
print("done...")