import os
import time
import cx_Oracle
import requests
from bs4 import BeautifulSoup
# #보배드림 사이트 - 국산차
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin # url 조인 활용
# url='https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
# res = requests.get(url)
# # print(res)
# # 사이트 정책보기 https://www.bobaedream.co.kr/robots.txt
# # 상세페이지의 기본정보(차이름, 가격, 연식, 배기량, 주행거리, 색상, 변속기, 보증정보, 연료, 확인사항)를 db에 입력, 이미지 저장.
# # 첫 번째 페이지에서 링크를 수집해서 for문 돌려서 수집.
# dom = BeautifulSoup(res.text,'lxml')        # 파싱
# # copy css selector
# #listCont > div.wrap-thumb-list > ul > li:nth-child(1) > div > div.mode-cell.title > p.tit > a
# #listCont div > div.mode-cell.title > p.tit > a
# alist = dom.select('#listCont div > div.mode-cell.title > p.tit > a')
# # print(len(alist))
# baseurl='https://www.bobaedream.co.kr/'
# urllist = []   # 빈 리스트
# #bs13 join 활용. join
# for a in alist:
#     # print(baseurl+a['href'])      # 각 상세페이지 링크 추출
#     # print(urljoin(baseurl,a['href'])) # 둘이 같은거
#     urllist.append(baseurl+a['href'])
# # print(urllist)
# for detailurl in urllist:
#     r=requests.get(detailurl) # 해당 페이지에서 request 한후 dom 처리
#     detaildom=BeautifulSoup(r.text,'lxml')
# # 제목 bobaeConent > div.component.page-detail > div.container-detail > div.wrap-detail-spot.js-object-fit > div.group-info > div.info-price.box.mode-basic > div.title-area > h3
#     title=detaildom.select_one('#bobaeConent div.title-area > h3').text
#     # print(title)
# # 가격 #bobaeConent > div.component.page-detail > div.container-detail > div.wrap-detail-spot.js-object-fit > div.group-info > div.info-price.box.mode-basic > div.price-area > span > b
#     price = detaildom.select_one('#bobaeConent div.price-area > span > b').text
#     # print(price)
# # 이미지 #bx-pager 아래 img
#     imgs=detaildom.select('#bx-pager img')
#     # print(imgs)
#     imglist=[]
#     for img in imgs:
#         # print(img['src'][2:7])
#         # print()
#         # 이미지가 없는 주소도 있어서 file 있는 애들만 저장
#         if img['src'][2:6]=='file':   # 속성값은 [] 로 접근
#             imglist.append("http:"+img['src'])
#     # print(imglist)
#     # bobaeConent > div.component.page-detail > div.container-detail > div.detail-section.mode-half > div:nth-child(1) > div.info-basic > div > table > colgroup
#     infos = detaildom.select('#bobaeConent div.info-basic div > table tr')
#     # print(len(infos))
#     # print(infos[0])
#     # print(infos[0].text)
#     infolist = infos[0].text.strip().split('\n')        #데이터 좌우 공백 자르고 공백도 자름;
#     # print(infolist)
#     year=infolist[1]
#     cc=infolist[3]
#     infolist1 = infos[1].text.strip().split('\n')
#     distance = infolist1[1]
#     color = infolist1[-1]
#     infolist2 = infos[2].text.strip().split('\n')
#     trans = infolist2[1]
#     guarantee = infolist2[-1]
#     infolist3 = infos[3].text.strip().split('\n')
#     fuel = infolist3[1]
#     confirm = infolist3[-1]  # 확인사항
#     if confirm =="확인사항":    # 확인사항이 없으면 검증없음으로 치환
#         confirm='검증안됨'
#     str = "{},{},{},{},{},{},{},{},{},{}".format(title,price,year,cc,distance,color,trans,guarantee,fuel,confirm)
#     print(str)

import datetime
# 테이블 쿼리문
# create table car(
#     no number constraint car_no_p primary key,
#     title varchar2(200),
#     price varchar2(200),
#     year varchar2(200),
#     cc varchar2(200),
#     distance varchar2(200),
#     color varchar2(200),
#     trans varchar2(200),
#     guarantee varchar2(200),
#     fuel varchar2(200),
#     confirm varchar2(200)
# );
# create sequence car_seq;


# 1페이지
# https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page=1&order=S11&view_size=20
# 2페이지
# https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page=2&order=S11&view_size=20
# 3페이지
# https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page=3&order=S11&view_size=20url='
def saveImg(imglist,title):
    # print(imglist) # 리스트 형태라 뽑아내야함 // 이미지들의 경로
    # print(title)
    i = 0
    for imgurl in imglist:
        i=i+1
        filename = os.path.join('d:/','study','pj1','car',title.strip() + str(i) + imgurl[-4:])# 양쪽끝 띄어쓰기 제거
        # filename=os.path.join('car',title.strip()+'_'+now.strftime('%y%m%d %H%M%S')+'_'+str(i)+imgurl[-4:])
        print(filename)
        r1=requests.get(imgurl) # 경로 받기
        with open(filename,mode='wb')as f:
            f.write(r1.content)  # 경로에 있는 이미지를 받아라
    time.sleep(1)

# 테이블에 넣기
con=cx_Oracle.connect("happy/day@localhost:1521/xe")
cur = con.cursor()
sql= "insert into car values (car_seq.nextval,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') "
url='https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page={}&order=S11&view_size=20'
for page in range(1,4):
    res = requests.get(url.format(page))
    dom = BeautifulSoup(res.text,'lxml')        # 파싱
    alist = dom.select('#listCont div > div.mode-cell.title > p.tit > a')
    baseurl='https://www.bobaedream.co.kr/'
    urllist = []   # 빈 리스트
    for a in alist:
        urllist.append(baseurl+a['href'])
    for detailurl in urllist:
        r=requests.get(detailurl) # 해당 페이지에서 request 한후 dom 처리
        detaildom=BeautifulSoup(r.text,'lxml')
        title=detaildom.select_one('#bobaeConent div.title-area > h3').text
        price = detaildom.select_one('#bobaeConent div.price-area > span > b').text
        imgs=detaildom.select('#bx-pager img')
        imglist=[]
        for img in imgs:
            if img['src'][2:6]=='file':
                imglist.append("http:"+img['src'])
        # saveImg(imglist,title)  # 내가 만든 이미지리스트 , 제목 가지고 가기
        infos = detaildom.select('#bobaeConent div.info-basic div > table tr')
        infolist = infos[0].text.strip().split('\n')        #데이터 좌우 공백 자르고 공백도 자름;
        year=infolist[1]
        cc=infolist[3]
        infolist1 = infos[1].text.strip().split('\n')
        distance = infolist1[1]
        color = infolist1[-1]
        infolist2 = infos[2].text.strip().split('\n')
        trans = infolist2[1]
        guarantee = infolist2[-1]
        infolist3 = infos[3].text.strip().split('\n')
        fuel = infolist3[1]
        confirm = infolist3[-1]  # 확인사항
        if confirm =="확인사항":    # 확인사항이 없으면 검증없음으로 치환
            confirm='검증안됨'
        # str = "{},{},{},{},{},{},{},{},{},{}".format(title,price,year,cc,distance,color,trans,guarantee,fuel,confirm)
        # print(str)
        # print(sql.format(title,price,year,cc,distance,color,trans,guarantee,fuel,confirm))
        cur.execute(sql.format(title,price,year,cc,distance,color,trans,guarantee,fuel,confirm))
    time.sleep(0.3)
con.commit()
con.close()



import datetime
# now=datetime.datetime(2020,12,25)
now=datetime.datetime.now()
print(type(now),now)
print(now.strftime('%y%m%d %H%M%S'))



















