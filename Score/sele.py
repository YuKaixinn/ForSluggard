from lib2to3.pgen2 import driver
from selenium import webdriver
from time import sleep

filepath = "stu1.txt"
url = "https://513574.yichafen.com/public/queryscore/sqcode/MsjcIn5mNjQzOXw0Nzk1M2Q0Y2QwNTBiY2UxOThlMWMzYzllMTQ1Mjc3N3w1MTM1NzQO0O0O.html"
theclass = 7

#xpath-one
classinput = '//*[@id="queryForm"]/table/tbody/tr[1]/td[2]/input'
nameinput = '//*[@id="queryForm"]/table/tbody/tr[2]/td[2]/input'
buttonclick = '//*[@id="yiDunSubmitBtn"]'

#xpath-two
idpath = '//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[2]'
namepath = '//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[3]'
chinesepath = '//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[4]'
chinesestd = '//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[5]'
mathpath = '//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[6]'
mathstd = '//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[7]'
totalstd = '//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[8]'
totalmark = '//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[9]'
rankpath = '//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[10]'

file = open(filepath,'r')
names = file.readlines()
driver = webdriver.Chrome()
driver.get(url)
ans = ""

for name in names:
    driver.refresh()
    driver.find_element_by_xpath(classinput).send_keys(theclass)
    driver.find_element_by_xpath(nameinput).send_keys(name)
    driver.find_element_by_xpath(buttonclick).click()
    sleep(1)
    id = driver.find_element_by_xpath(idpath).text
    name = driver.find_element_by_xpath(namepath).text
    chinese = driver.find_element_by_xpath(chinesepath).text
    chineses = driver.find_element_by_xpath(chinesestd).text
    math = driver.find_element_by_xpath(mathpath).text
    maths = driver.find_element_by_xpath(mathstd).text
    totals = driver.find_element_by_xpath(totalstd).text
    totalm = driver.find_element_by_xpath(totalmark).text
    rank = driver.find_element_by_xpath(rankpath).text
    ans += id+"\t"+name+"\t"+chinese+"\t"+chineses+"\t"+math+"\t"+maths+"\t"+totals+"\t"+totalm+"\t"+rank+"\n"
    driver.back()
    print(ans)
driver.close()


# def F(name):
#     driver = webdriver.Chrome()
#     driver.get("")
#     driver.find_element_by_xpath('').send_keys("7")
#     driver.find_element_by_xpath('').send_keys(name)
#     driver.find_element_by_xpath('').click()
#     sleep(1)
#     id = driver.find_element_by_xpath('//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[2]').text
    
#     score = driver.find_element_by_xpath('//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[9]').text
#     rank = driver.find_element_by_xpath('//*[@id="result_content"]/div[2]/table/tbody/tr[2]/td[10]').text
#     res = ""+str(name)+"\t"+""+str(score)+",名次:"+str(rank)+"\n"
#     driver.close()
#     return res


# f = open('stu1.txt', 'r')
# lines = f.readlines()
# cnt = 0
# ans = ""
# for line in lines:
#     ans+=F(line)
#     print(ans)