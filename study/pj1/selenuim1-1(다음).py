from selenium import webdriver
import time
def getPw():
    with open('data\\pwd.txt',mode='r') as f:
        pw=f.readline()
    return pw.strip()  # 좌우의 공백제거.

driver = webdriver.Chrome('data\\chromedriver')
url='https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
driver.get(url)
idbox=driver.find_element_by_css_selector('#id')
idbox.send_keys('mgk1059')
time.sleep(2)
pwbox=driver.find_element_by_css_selector('#inputPwd')
pwbox.send_keys(getPw())
time.sleep(2)
btn=driver.find_element_by_css_selector('#loginBtn')
btn.click()
time.sleep(3)
# email = driver.get('https://mail.daum.net/')
time.sleep(2)
emailtitle = driver.find_elements_by_css_selector('#mailList > div.scroll > div > ul > li > div.info_from > a')
emailcontent = driver.find_elements_by_css_selector('#mailList > div.scroll > div > ul > li > div.info_subject > a.link_subject > strong')
# for p,t in zip(emailtitle,emailcontent):        # zip 함수를 통해서 붙이자!!!!! 외어서 써먹어야겠다.
#     print(p.text,t.text)




stock=driver.get('https://finance.daum.net/')
texts = driver.find_elements_by_css_selector('#boxTodayNews > div.halfB > ul.fl > li > a')
#boxTodayNews > div.halfB > ul.fl > li > a
for text in texts:
    print(text.text)
