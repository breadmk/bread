from selenium import webdriver
# 웹드라이버:크롤러와 브라우져를 연결시켜주는 프로그램
# 크롬드라이버 다운로드
# 크롬 chrom://version 에 맞춰서 설치.

# 첫번째 찾기
# driver.find_element_by_class_name()
# driver.find_element_by_css_selector()
# 전부 다 찾기
# driver.find_elements_by_css_selector()
# driver.find_elements_by_class_name()

# 마우스 제어 click()
# driver.click()
# 키보드 제어 send_keys()
# driver.send_keys()
# 자바스크립트 실행 execute_script()
# driver.execute_script()

# copy selector ( css 내용 나옴 )
# a = driver.find_element_by_css_selector('body > main > div > div > div:nth-child(9) > h3 > a')
# print(a.tag_name)
# print(a.text)
# a.click()
import time
driver=webdriver.Chrome('data\\chromedriver')   # 브라우져 접속
url='http://pjt3591oo.github.io'                # 접속 url
driver.get(url)                                 # 해당 페이지 접속
# print(driver.page_source)                       # html 소스 가져오기
# print("현재 page url : ",driver.current_url)
# print("현재 page title 태그 : ",driver.title)
# time.sleep(1)
search= driver.find_element_by_css_selector('body > header > div > nav > div > a:nth-child(4)')
search.click()
# 박스에 값 넣기
box=driver.find_element_by_css_selector('#search-box')
box.send_keys('python')
# 버튼클릭
# click=driver.find_element_by_css_selector('body > main > div > div > form > input[type=submit]:nth-child(3)')
btn=driver.find_element_by_css_selector('input[type=submit]:nth-child(3)')
btn.click()
# 파랑 제목들 출력
# search-results > li:nth-child(2) > a > h3   <---------- 여기서 모든 li 로 수정해서 출력.#####
h3s=driver.find_elements_by_css_selector('#search-results > li > a > h3')
for h3 in h3s:
    print(h3.text)
