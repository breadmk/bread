import requests
from bs4 import BeautifulSoup

# def saveImg(imgurl,title):
#     # print(imgurl)
#     # print(imgurl[-4:])
#     # print(title)
#     title=title.replace(' :','')
#     title = title.replace(')','')
#     title = title.replace('(', '')
#     title = title.replace('/', '')
#     filename='img\\'+title+imgurl[-4:]
#     # print(filename)
#     r=requests.get(imgurl)
#     with open(filename,mode='wb') as f1:
#         f1.write(r.content)
#
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
        # saveImg(img,title)
        div=trs[i].find('div',class_="rating_type")
        rating=div.find('strong').text
        date=trs[i].find('td',class_='num').text
        date = trs[i].find('td', class_='num').text
        f.write('{},{},{}\n'.format(title,rating,date))

# 모든 페이지의 이미지를 다운로드하고 제목, 평점, 등록일을 webtoon.csv 파일로 저장.
# 단 한 페이지 수집후 1초 쉬기.

#--------------------------------------------------------------

# import time
#
# def saveImg(imgurl,title):
#     # print(imgurl)
#     # print(imgurl[-4:])
#     # print(title)
#     title=title.replace(' :','')
#     title = title.replace(')','')
#     title = title.replace('(', '')
#     title = title.replace('/', '')
#     title = title.replace('?', '')
#     title = title.replace(': ', '')
#     filename='img\\'+title+imgurl[-4:]
#     # print(filename)
#     r=requests.get(imgurl)
#     with open(filename,mode='wb') as f1:
#         f1.write(r.content)
#
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
#             # print(img)
#             td1=trs[i].find('td', class_='title')
#             title = td1.find('a').text
#             saveImg(img, title)
#             # print(title)
#             div=trs[i].find('div',class_="rating_type")
#             rating=div.find('strong').text
#             # print(rating)
#             date=trs[i].find('td',class_='num').text
#             date = trs[i].find('td', class_='num').text
#             # print(date)
#             f.write('{},{},{},{}\n'.format(img,title, rating, date))
#         time.sleep(1)



