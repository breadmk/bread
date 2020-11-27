# from selenium import webdriver
# import time
# def getPw():
#     with open('data\\pwd.txt',mode='r') as f:
#         pw=f.readline()
#     return pw.strip()  # 좌우의 공백제거.
#
# driver=webdriver.PhantomJS('data\\phantomjs') # 브라우져 띄우지 않고 내용만 빼오기
# url='https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
# driver.get(url)
# idbox=driver.find_element_by_css_selector('#id')
# idbox.send_keys('mgk1059')
# time.sleep(2)
# pwbox=driver.find_element_by_css_selector('#inputPwd')
# pwbox.send_keys(getPw())
# time.sleep(2)
# btn=driver.find_element_by_css_selector('#loginBtn')
# btn.click()
# time.sleep(3)
# email = driver.get('https://mail.daum.net/')
# time.sleep(2)
# source = driver.page_source
# # print(source)
# emailtitle = driver.find_elements_by_css_selector('#mailList > div.scroll > div > ul > li > div.info_from > a')
# emailcontent = driver.find_elements_by_css_selector('#mailList > div.scroll > div > ul > li > div.info_subject > a.link_subject > strong')
# for p,t in zip(emailtitle,emailcontent):        # zip 함수를 통해서 붙이자!!!!! 외어서 써먹어야겠다.
#     print(p.text,t.text)

#-------------------------------------------------------------------

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# def getPw():
#     with open('data\\pwd.txt',mode='r') as f:
#         pw=f.readline()
#     return pw.strip()  # 좌우의 공백제거.
#
# driver=webdriver.PhantomJS('data\\phantomjs') # 브라우져 띄우지 않고 내용만 빼오기
# url='https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
# driver.get(url)
# idbox=driver.find_element_by_css_selector('#id')
# idbox.send_keys('mgk1059')
# time.sleep(2)
# pwbox=driver.find_element_by_css_selector('#inputPwd')
# pwbox.send_keys(getPw())
# time.sleep(2)
# btn=driver.find_element_by_css_selector('#loginBtn')
# btn.click()
# time.sleep(3)
# email = driver.get('https://mail.daum.net/')
# time.sleep(2)
# source = driver.page_source
# # print(source)
# dom = BeautifulSoup(driver.page_source,'lxml')
# # print(dom)
# title = dom.select('#mailList > div.scroll > div > ul > li > div.info_from > a')
# for tit in title:
#     print(tit.text)

#-------------------------------------
import fake_useragent   # 403 에러가 나와서 fake_useragent 를 사용해서 숨겨서 접근
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import json
ua=UserAgent()
headers={'user-agent':ua.chrome,'referer' : 'https://finance.daum.net/'}
url='https://finance.daum.net/content/news/news_top'
res = requests.get(url,headers=headers)
# print(res)
dom = BeautifulSoup(res.text,'lxml')
# print(dom.text)
news = dom.text
json_new = json.loads(news)
# print(news)
for i in json_new:
    print(i['title'])
# for title in dom.text:
#     print(title)
# news = dom.select('#boxTodayNews > div.halfB > ul.fl > li > a')
# print(news)
# for newstext in news:
#     print(newstext.text)
