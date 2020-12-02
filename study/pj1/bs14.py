import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os
import datetime
import cx_Oracle
# create table car(
#     no number constraint car_no_p primary key,
#     title varchar2(200),
#     price varchar2(200),
#     year varchar2(200),
#     baegi varchar2(200),
#     distance varchar2(200),
#     color varchar2(200),
#     trans varchar2(200),
#     guarantee varchar2(200),
#     fuel varchar2(200),
#     confirm varchar2(200)
# );
# create sequence car_seq;
# url='https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
# recvd=requests.get(url)
# print(recvd)
# 상세페이지의 차이름,가격,기본정보를 데이터베이스에 입력, 이미지 car폴더에 저장
# dom=BeautifulSoup(recvd.text,'lxml')
# alist=dom.select('#listCont div.mode-cell.title > p.tit > a')
# # print(len(alist))
# baseurl='https://www.bobaedream.co.kr/'
# urllist=[]
# for a in alist:
#     # print(baseurl+a['href'])
#     # print(urljoin(baseurl,a['href']))
#     urllist.append(urljoin(baseurl,a['href']))
# # print(urllist)
# for detailurl in urllist:
#     r=requests.get(detailurl)
#     # print(r)
#     detaildom=BeautifulSoup(r.text,'lxml')
#     title=detaildom.select_one('#bobaeConent div.title-area > h3').text
#     # print(title)
#     price=detaildom.select_one('#bobaeConent div.price-area > span > b').text
#     # print(price)
#     imgs=detaildom.select('#bx-pager img')
#     # print(imgs)
#     imglist=[]
#     for img in imgs:
#         # print('https:'+img['src'])
#         if img['src'][2:6]=='file':
#             imglist.append('https:'+img['src'])
#     # print(imglist)
#     infos=detaildom.select('#bobaeConent div.info-basic div > table tr')
#     # print(len(infos))
#     # print(infos[0].text)
#     infolist=infos[0].text.strip().split('\n')
#     # print(infolist)
#     year=infolist[1]
#     baegi=infolist[3]
#     infolist=infos[1].text.strip().split('\n')
#     distance=infolist[1]
#     color=infolist[3]
#     infolist=infos[2].text.strip().split('\n')
#     # print(infolist)
#     trans=infolist[1]
#     guarantee=infolist[-1]
#     infolist=infos[3].text.strip().split('\n')
#     fuel=infolist[1]
#     confirm=infolist[-1]
#     if confirm=='확인사항':
#         confirm=''
#     str="{},{},{},{},{},{},{},{},{},{}"
#     print(str.format(title,price,year,baegi,distance,color,trans,guarantee,fuel,confirm))
# print('-'*30)
# https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page=2&order=S11&view_size=20
# https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page=3&order=S11&view_size=20
# https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page=1&order=S11&view_size=20

def saveImg(imglist,title):
    # print(imglist)
    now = datetime.datetime.now()
    # print(now.strftime('%y%m%d %H%M%S'))
    i=0
    for imgurl in imglist:
        i=i+1
        # filename=os.path.join('car',title.strip()+str(i)+imgurl[-4:])
        filename=os.path.join('d:\\','study','pj1','img','car',title.strip()+'_'+now.strftime('%y%m%d %H%M%S')+'_'+str(i)+imgurl[-4:])
        # print(filename)
        r1=requests.get(imgurl)
        with open(filename,'wb') as f:
            f.write(r1.content)
    time.sleep(1)
con=cx_Oracle.connect('happy/day@localhost:1521/xe')
cur=con.cursor()
sql="insert into car values " \
    "(car_seq.nextval,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
url='https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page={}&order=S11&view_size=20'
for page in range(1,2):
    recvd=requests.get(url.format(page))
    dom=BeautifulSoup(recvd.text,'lxml')
    alist=dom.select('#listCont div.mode-cell.title > p.tit > a')
    baseurl='https://www.bobaedream.co.kr/'
    urllist=[]
    for a in alist:
        urllist.append(urljoin(baseurl,a['href']))
    for detailurl in urllist:
        r=requests.get(detailurl)
        detaildom=BeautifulSoup(r.text,'lxml')
        title=detaildom.select_one('#bobaeConent div.title-area > h3').text
        price=detaildom.select_one('#bobaeConent div.price-area > span > b').text
        imgs=detaildom.select('#bx-pager img')
        imglist=[]
        for img in imgs:
            if img['src'][2:6]=='file':
                imglist.append('https:'+img['src'])
        saveImg(imglist,title)
        infos=detaildom.select('#bobaeConent div.info-basic div > table tr')
        infolist=infos[0].text.strip().split('\n')
        year=infolist[1]
        baegi=infolist[3]
        infolist=infos[1].text.strip().split('\n')
        distance=infolist[1]
        color=infolist[3]
        infolist=infos[2].text.strip().split('\n')
        trans=infolist[1]
        guarantee=infolist[-1]
        infolist=infos[3].text.strip().split('\n')
        fuel=infolist[1]
        confirm=infolist[-1]
        if confirm=='확인사항':
            confirm=''
        # cur.execute(sql.format(title,price,year,baegi,distance,color,trans,guarantee,fuel,confirm))
    time.sleep(1)
con.commit()
con.close()
# import datetime
# # now=datetime.datetime(2020,12,25)
# now=datetime.datetime.now()
# print(type(now),now)
# print(now.strftime('%y%m%d %H%M%S'))
# (venv) D:\study\pj1>pyinstaller --onefile bs14.py
# 명령프롬프트에서 실행시 윈도우+r - cmd
# C:\Users\admin>d:
# D:\>cd study\pj1\dist
# D:\study\pj1\dist>bs14

