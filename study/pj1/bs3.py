# www.naver.com/robots.txt 정책확인하기
import requests
from bs4 import BeautifulSoup

# url = 'https://finance.naver.com/marketindex/'
# recvd = requests.get(url)
# # print(recvd)
# # print(recvd.text)
# dom = BeautifulSoup(recvd.text, 'lxml')
#
# # <span class="value">1,106.60</span>
# # 네이버 환율의 환율값만 가져오기.
# span = dom.find('span', class_='value')
# print(span.text)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ------------------------

# url='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon'
# recvd=requests.get(url)
# # print(recvd)
# # print(recvd.text)
# dom=BeautifulSoup(recvd.text,'lxml')
# table=dom.find('table',class_='viewList')
# # print(table)
# trs=table.find_all('tr')
# # print(trs)
# # print(len(trs)) # 0번째랑 1번째는 필요없는 내용임.
#
# for i in range(2,len(trs)):     # 2번째부터 리스트 길이만큼 돌아라.
#     # print(trs[i])
#     td1=trs[i].find('td', class_='title')
#     title = td1.find('a').text
#     # print(title)
#     div=trs[i].find('div',class_="rating_type")
#     rating=div.find('strong').text
#     # print(rating)
#     date=trs[i].find('td',class_='num').text
#     # print(date)
#     print('{},{},{}'.format(title,rating,date))


#--------------------------------------------------------------------------------------------------
# with open('data\\webtoon.csv',mode='w',encoding='utf-8') as f:
#
#     url='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon'
#     recvd=requests.get(url)
#     # print(recvd)
#     # print(recvd.text)
#     dom=BeautifulSoup(recvd.text,'lxml')
#     table=dom.find('table',class_='viewList')
#     # print(table)
#     trs=table.find_all('tr')
#     # print(trs)
#     # print(len(trs)) # 0번째랑 1번째는 필요없는 내용임.
#
#     for i in range(2,len(trs)):     # 2번째부터 리스트 길이만큼 돌아라.
#         # print(trs[i])
#         td1=trs[i].find('td', class_='title')
#         title = td1.find('a').text
#         # print(title)
#         div=trs[i].find('div',class_="rating_type")
#         rating=div.find('strong').text
#         # print(rating)
#         date=trs[i].find('td',class_='num').text
#         date = trs[i].find('td', class_='num').text
#         # print(date)
#         f.write('{},{},{}\n'.format(title,rating,date))
#------------------------------------------------------------------------------------------------------

# https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon
# https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon&page=1
# https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon&page=2
# https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon&page=3

# str='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon&page={}'
# for page in range(1,7):
#     str='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon&page={}'.format(page)
#     print(str)

#---------------------------------------------------------------------------------------------------------

with open('data\\webtoon.csv',mode='w',encoding='utf-8') as f:
    for page in range(1,7):
        pageurl='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon&page={}'.format(page)
        recvd=requests.get(pageurl)
        # print(recvd)
        # print(recvd.text)
        dom=BeautifulSoup(recvd.text,'lxml')
        table=dom.find('table',class_='viewList')
        # print(table)
        trs=table.find_all('tr')
        # print(trs)
        # print(len(trs)) # 0번째랑 1번째는 필요없는 내용임.

        for i in range(2,len(trs)):     # 2번째부터 리스트 길이만큼 돌아라.
            # print(trs[i])
            td1=trs[i].find('td', class_='title')
            title = td1.find('a').text
            # print(title)
            div=trs[i].find('div',class_="rating_type")
            rating=div.find('strong').text
            # print(rating)
            date=trs[i].find('td',class_='num').text
            date = trs[i].find('td', class_='num').text
            # print(date)
            f.write('{},{},{}\n'.format(title, rating, date))

#--------------------------------------------------------------------------------------------------------

# # 이미지경로,제목,평점,등록일 추출.
# import time
# with open('data\\webtoon.csv',mode='w',encoding='utf-8') as f:
#     for page in range(1,7):
#         pageurl='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon&page={}'.format(page)
#         recvd=requests.get(pageurl)
#         # print(recvd)
#         # print(recvd.text)
#         dom=BeautifulSoup(recvd.text,'lxml')
#         table=dom.find('table',class_='viewList')
#         # print(table)
#         trs=table.find_all('tr')
#         # print(trs)
#         # print(len(trs)) # 0번째랑 1번째는 필요없는 내용임.
#
#
#         for i in range(2,len(trs)):     # 2번째부터 리스트 길이만큼 돌아라.
#             # print(trs[i])
#             img=trs[i].find('img')['src']
#             print(img)
#             td1=trs[i].find('td', class_='title')
#             title = td1.find('a').text
#             # print(title)
#             div=trs[i].find('div',class_="rating_type")
#             rating=div.find('strong').text
#             # print(rating)
#             date=trs[i].find('td',class_='num').text
#             date = trs[i].find('td', class_='num').text
#             # print(date)
#             f.write('{},{},{},{}\n'.format(img,title, rating, date))
#         time.sleep(1)

#-----------------------------------------------------------------------------------------------


def saveImg(imgurl):
    print('저장중')

with open('data\\webtoon.csv',mode='w',encoding='utf-8') as f:

    url='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon'
    recvd=requests.get(url)
    dom=BeautifulSoup(recvd.text,'lxml')
    table=dom.find('table',class_='viewList')
    trs=table.find_all('tr')

    for i in range(2,len(trs)):     # 2번째부터 리스트 길이만큼 돌아라.
        td=trs[i].find('td')
        img=(td.find('img')['src'])     #이미지경로
        td1=trs[i].find('td', class_='title')
        title = td1.find('a').text
        div=trs[i].find('div',class_="rating_type")
        rating=div.find('strong').text
        date=trs[i].find('td',class_='num').text
        date = trs[i].find('td', class_='num').text
        f.write('{},{},{},{}\n'.format(img,title,rating,date))