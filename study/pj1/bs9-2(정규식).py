# ---------------------정 규 식 -----------------------

# import requests
# from bs4 import BeautifulSoup
#
# url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108' #? 있으니 get방식
# res = requests.get(url)
# print(res.text)

import re   # 정규표현식 사용 import

str ="""
3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
15418  yttKsa 5134
"""
# re.findall('패턴',위치)
r1 = re.findall('[0-9]',str)   # 전부 다 찾겠다.
# print(r1)
# [0-9] 까지 숫자가 한번 이상 나오는 경우 +  넣어서 검색.
r1 = re.findall(r'[0-9]+',str)   # 이스케이프 문자가 있을 경우 r 을 넣어줘야한다.
# print(r1)
r1 = re.findall(r'[a-zA-Z1-9]+',str)
# print(r1)

url1 ='https://ko.wikipedia.org/wiki/%EC%A0%95%EA%B7%9C_%ED%91%9C%ED%98%84%EC%8B%9D'
# * = 0개이상)  + = 1개이상 )  | = 선택)
# . = (줄바꿈을 제외한)한글자 ? = 0 또는 1

# [] {m,n} = m번이상 최대n 번까지 {1,3} <- 1번이상 3번이하 {,3} <-3번이하 {1,} <- 1번이상 {3} <-3번
#---------------------------------------------------
# . 줄바꿈을 제외한 한 글자.
# print(re.match('a.b','aab'))
# print(re.match('a.b','a0b'))
# print(re.match('a.b','c0b'))
# print(re.findall('a.b','a0brrrr'))      # 원하는 값 찾을때 사용;
# print(re.search('a.b','aab'))
str1 = '3pink dress'
# print(re.match('[a-z]+',str1))      # 문자열 처음부터 일치할 때만 찾아줌;  # None
# print(re.search('[a-z]+',str1))     # 문자열 전체를 검색  # <re.Match object; span=(1, 5), match='pink'>
# print(re.findall('[a-z]+',str1))    # 정규식에 일치하는 문자열 반환  # ['pink', 'dress']

# group() 정규식에 일치하는 문자열 추출.

# print(re.match('[a-z]+',str1).group())    # 일차하는게 없으니 주석처리
# print(re.search('[a-z]+',str1).group())  # pink

str2 = 'pink333 dress444'

# print(re.match('[a-z]+',str2).group())  # 처음에 발견되는 하나만 추출;
# print(re.search('[a-z]+',str2).group()) # 처음에 발견되는 하나만 추출;
# print(re.findall('[a-z]+',str2))        # 모두 추출

str3 = 'My handphone number 010-8484-2950'

# print(re.findall('[0-9]+',str3))            # ['010', '8484', '2950']
# print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d',str3).group()) # 010-8484-2950
# print(re.match('\d\d\d-\d\d\d\d-\d\d\d\d',str3).group())  # 못 찾음;
# print(re.findall('\d\d\d-\d\d\d\d-\d\d\d\d',str3))      # ['010-8484-2950']
# print(re.search('[0-9]{3,4}-[0-9]{3,4}-[0-9]{3,4}',str3).group()) # 010-8484-2950


str4 ="""
3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
15418  yttKsa 5134
"""

# t1 = re.compile('[a-z]+',re.I)
# print(t1.findall(str4))
# re.I 대소문자 구별없이 추출;
# print(re.findall('[a-z]+',str4,re.I))
# 옵션
# re.IGNORECASE(I)   : 대소문자 구분 없이 적용
# re.I
# re.DOTALL(S) : 줄바꿈 포함
# re.VERBOSE(X) : 정규식에 주석을 사용할 수 있다.

import pyperclip
# pyperclip.copy('hello hellllllllloooooooooo')  # 파이썬 내용을 복사해서 나갈때 클립보드에 복사하는 명령어
# print(pyperclip.paste())                # 다른 곳에서 복사한 내용을 파이썬으로 붙여넣을때 사용하는 명령어

# print(text)
# email 만 추출하기

email_regex = re.compile(r"""(
                             [a-zA-Z0-9_.-]+    #이메일이름 (username)
                             @                   # @ 기호
                             [a-zA-Z0-9_.-]+     # 도메인
                             (\.[a-zA-Z]{2,4}) #com, net, etc...
                             
                             
)""",re.VERBOSE)

# text = pyperclip.paste()
# print(text)
# result = email_regex.findall(text)
# print(result)   # [ (),(),() ]
# for i in result:
#     print(i[0])

# ===================

f=open('data\\test.html',encoding='utf-8')
text=f.read()
# print(text)

# tag=re.compile('<.+>')        # 탐욕적 방식
tag=re.compile('<.+?>')       # 게으른 방식
# print(tag.match(text))
# print(tag.search(text))
print(tag.findall(text))
# --------------------------------------------------------------
tag=re.compile('<(.+?)>')       # 꺽새빼고 출력

print(tag.findall(text))
#--------------------------------------------------------------------------

# i로 시작해서 n으로 끝나는 모든 문자 찾기
str = 'internationalization'
test = re.compile(r'i.+n')  # 탐욕적 방식 ['internationalization']
# print(test.findall(str))
test = re.compile(r'i.+?n') # 게으른 방식
# print(test.findall(str))    # ? 넣어주면  3개 모두 다 나옴; ['intern', 'ion', 'ization']

