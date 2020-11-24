# C:\Users\admin>sqlplus happy/day
# create table webtoon(
#     no number primary key,
#     title varchar2(100),
#     rating varchar2(20),
#     regdate varchar2(20)
# );
# create sequence webtoon_seq;
# insert into webtoon values (webtoon_seq.nextval,제목,평점,등록일);

# import time
# from bs4 import BeautifulSoup
# import requests
# import cx_Oracle
# import os
# con=cx_Oracle.connect("happy/day@localhost:1521/xe")
# cur = con.cursor()
# sql='insert into webtoon values (webtoon_seq.nextval,:1,:2,:3)'
# url='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon'
# recvd=requests.get(url)
# dom=BeautifulSoup(recvd.text,'lxml')
# table=dom.find('table',class_='viewList')
# trs=table.find_all('tr')
#
# for i in range(2,len(trs)):     # 2번째부터 리스트 길이만큼 돌아라.
#     td=trs[i].find('td')
#     # img=(td.find('img')['src'])     #이미지경로
#     td1=trs[i].find('td', class_='title')
#     title = td1.find('a').text
#     div=trs[i].find('div',class_="rating_type")
#     rating=div.find('strong').text
#     # regdate=trs[i].find('td',class_='num').text
#     regdate = trs[i].find('td', class_='num').text
# cur.execute(sql,(title,rating,regdate))
# con.commit()
# con.close()

#--------------쿼리문 방법 2 ----------------------------

import time
from bs4 import BeautifulSoup
import requests
import cx_Oracle
import os
con=cx_Oracle.connect("happy/day@localhost:1521/xe")
cur = con.cursor()
sql = "insert into webtoon values (webtoon_seq.nextval,'{}','{}','{}')"
url='https://comic.naver.com/webtoon/list.nhn?titleId=733766&weekday=mon'
recvd=requests.get(url)
dom=BeautifulSoup(recvd.text,'lxml')
table=dom.find('table',class_='viewList')
trs=table.find_all('tr')

for i in range(2,len(trs)):     # 2번째부터 리스트 길이만큼 돌아라.
    td=trs[i].find('td')
    # img=(td.find('img')['src'])     #이미지경로
    td1=trs[i].find('td', class_='title')
    title = td1.find('a').text
    div=trs[i].find('div',class_="rating_type")
    rating=div.find('strong').text
    # regdate=trs[i].find('td',class_='num').text
    regdate = trs[i].find('td', class_='num').text
    cur.execute(sql.format(title,rating,regdate))
# cur.execute(sql,(title,rating,regdate))
con.commit()
con.close()

#-----------------------------------------------

