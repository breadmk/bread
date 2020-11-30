from selenium import webdriver
import time
from  selenium.webdriver.common.keys import Keys        # 특수 키 사용
# driver=webdriver.Chrome('data\\chromedriver')   # 브라우져 접속
# url='http://pjt3591oo.github.io'                # 접속 url
# driver.get(url)                                 # 해당 페이지 접속
# driver.execute_script("alert('happy day')")     # javascript 실행되는 것을 확인했음.
# time.sleep(1)
# search= driver.find_element_by_css_selector('body > header > div > nav > div > a:nth-child(4)')
# search.click()
# 박스에 값 넣기
# box=driver.find_element_by_css_selector('#search-box')
# box.send_keys('nosql')
# box.send_keys(Keys.ENTER)       # 엔터키를 눌러라.
# 버튼클릭
# click=driver.find_element_by_css_selector('body > main > div > div > form > input[type=submit]:nth-child(3)')
# btn=driver.find_element_by_css_selector('input[type=submit]:nth-child(3)')
# btn.click()
# 파랑 제목들 출력
# search-results > li:nth-child(2) > a > h3   <---------- 여기서 모든 li 로 수정해서 출력.#####
# h3s=driver.find_elements_by_css_selector('#search-results > li > a > h3')
# for h3 in h3s:
#     print(h3.text)

#-----------------------------------------------------------------------------


# driver=webdriver.Chrome('data\\chromedriver')   # 브라우져 접속
# url='https://www.10000recipe.com/recipe/list.html'                # 접속 url
# driver.get(url)                                 # 해당 페이지 접속
# id_search_category > table > tbody > tr:nth-child(1) > td > div > div:nth-child(1) > a:nth-child(2)
# a2=driver.find_element_by_css_selector('#id_search_category div.cate_list > a:nth-child(2)')
# a3=driver.find_element_by_css_selector('id_search_category > table > tbody > tr:nth-child(1) > td > div > div:nth-child(1) > a:nth-child(2)')
#id_search_category > table > tbody > tr:nth-child(1) > td > div > div:nth-child(1) > a:nth-child(10)
# print(a2.text)
# print(a2.get_attribute('href'))     # 속성값을 가져올때.
# driver.execute_script(a2.get_attribute('href'))

#------------------------------------------------------------------

# 경로의 이미지 다운 로드 html 복사해서 따와서 넣기
# import urllib.request
# url="https://shared-comic.pstatic.net/thumb/webtoon/758150/thumbnail/thumbnail_IMAG04_6a803d87-cf63-4ecc-8ad7-accf2588747b.jpg"
# filename='img\\webtoon.jpg'
# urllib.request.urlretrieve(url,filename)            # url 에 해당 되는 내용을 다운 받아라

from urllib.parse import urlparse
url='https://www.ml5.co.kr:1621/a502/index.html?student=14&area=60#title'
pr=urlparse(url)    #네임드튜플 반환
print(pr)
# print(pr.scheme)    # http,ftp,....
# print(pr.netloc)    # 포트 번호까지 따오기
# print(pr.path)      # 경로
# print(pr.query)     # ?뒤에 내용
# print(urlparse(url))    # 네임드 튜플로 출력 ( 키=값 )
from  urllib.parse import urljoin

# baseurl= 'https://www.ml5.co.kr:1621/a502/index.html'
# print(1,urljoin(baseurl,'a.html'))
# print(2,urljoin(baseurl,'b.html'))      # html 을 넣으면 아래만 바뀜
# print(3,urljoin(baseurl,'/c.jpg'))      # 확장자 바꾸면 위치가 달라짐.
# print(4,urljoin(baseurl,'//d.jpg'))     # //2개는 프로토콜 밑부터 바뀜
# print(5,urljoin(baseurl,'../blue/e.jpg'))     # .. 찍으면 위로 붙음
# print(6,urljoin(baseurl,'blue/e.jpg'))          # 안 붙이면 아래 붙음
# print(7,urljoin(baseurl,'http://f.html'))       # 걍 다 바꾸는거
import os
# filename='d:\\study\\pj1\\data\\Beauty.smi'
# name1=os.path.join('d:\\','study','pj1','data','Beauty.smi')
# print('name1=',name1)
# print("nama1의 dirname=",os.path.dirname(name1))
# print("nama1의 basename=",os.path.basename(name1))
# print("-"*50)
# name2=os.path.join('d:\\','study','pj1','data')
# print('name2=',name2)
# print('name2의 dirname=',os.path.dirname(name2))
# print("nama2의 basename=",os.path.basename(name2))

# print(os.path.exists('d:\\study\\pj1\\data'))       # True
# print(os.path.exists('d:\\study\\pj1\\data2'))      # 파일이 있는지 없는지 확인 T/F

# if not os.path.exists('d:\\study\\pj1\\data2'):
#     os.mkdir('d:\\study\\pj1\\data2')           # 폴더가 없으면 만들어라.

a=[i for i in range(5)]
print(a)
b=['one','two','three']
print(b)
a=a+b
print(a)
a.append(b)
print(a)
