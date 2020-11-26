# show databases;   : 데이타베이스목록확인.
# use pythondb;     : 사용할 데이터베이스 선택.
# show tables;      : 테이블목록 확인.

import pymysql as my
# 1) 데이터베이스 연결
con=my.connect(host='localhost',user='root',password='1234',db='pythondb',charset='utf8')
# 2) 커서 생성
cur=con.cursor(my.cursors.DictCursor)
# 3) 쿼리 생성
sql='select * from member'
# 4) 실행 처리
cur.execute(sql)
rows=cur.fetchall()
for row in rows:
    print(row)
# for i in cur.execute(sql):
#     print(i)
# 5) 자원해제
con.close()

#----------------------------------------딕셔너리 커서~----------------- 딕셔너리로 반환.
# # 1) 데이터베이스 연결
# con=my.connect(host='localhost',user='root',password='1234',db='pythondb',charset='utf8')
# # 2) 커서 생성
# cur=con.cursor(my.cursors.DictCursor)
# # 3) 쿼리 생성
# sql='select * from member'
# # 4) 실행 처리
# cur.execute(sql)
# rows=cur.fetchall()
# for row in rows:
#     # print(row)
#     print(row['no'],row['name'],row['age'],row['email'],row['birthyear'])
# # for i in cur.execute(sql):
# #     print(i)
# # 5) 자원해제
# con.close()

#------------------------데이터 삽입-----------------------------------

# # 1) 데이터베이스 연결
# con=my.connect(host='localhost',user='root',password='1234',db='pythondb',charset='utf8')
# # 2) 커서 생성
# cur=con.cursor(my.cursors.DictCursor)
#
# # 3) 쿼리 생성
# while(True):
#     name=input('사용자이름=')
#     if name=="":          #name 입력란에서 enter 입력하면 종료되는 조건문.
#         break
#     age=input('사용자나이=')
#     email=input('사용자이메일=')
#     birthyear=input('사용자출생년도=')
#     sql='insert into member (name,age,email,birthyear) values(%s,%s,%s,%s)'
#     # 4) 실행 처리
#     cur.execute(sql,(name,age,email,birthyear))
# con.commit()
# # 5) 자원해제
# con.close()

#------------------------수정 및 삭제------------------------------------------------

# # 1) 데이터베이스 연결
# con=my.connect(host='localhost',user='root',password='1234',db='pythondb',charset='utf8')
# # 2) 커서 생성
# cur=con.cursor(my.cursors.DictCursor)
# # 3) 쿼리 생성
# age=input('나이=')
# sql='delete from member where age<=%s'
# # 4) 실행 처리
# cur.execute(sql,(age,))      # 튜플의 경우는 , 찍어주는게 관례임. 튜플은 혼자 있을때 콤마를 찍어준다.
# con.commit()
# # 5) 자원해제
# con.close()

# 이름과 태어난 년도를 입력받아 이름,나이, 태어난년도를 수정하세요.

# 1) 데이터베이스 연결
# con=my.connect(host='localhost',user='root',password='1234',db='pythondb',charset='utf8')
# # 2) 커서 생성
# cur=con.cursor(my.cursors.DictCursor)
# # 3) 쿼리 생성
# name=input('이름=')
# birthyear=input('태어난년도=')
# sql='update member set age=%s,birthyear=%s where name=%s'
# nai=2020-int(birthyear)+1
# # # 4) 실행 처리
# cur.execute(sql,(nai,birthyear,name))
# con.commit()
# # 5) 자원해제
# con.close()

#---------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
import os
import pymysql as my
# con=my.connect(host='localhost',user='root',password='1234',db='pythondb',charset='utf8')
# cur=con.cursor(my.cursors.DictCursor)
# sql='insert into movie (title,rating,reserv,playtime) values (%s,%s,%s,%s)'
#
# url='https://movie.naver.com/movie/running/current.nhn'
# re=requests.get(url)
# dom=BeautifulSoup(re.text,'lxml')   #파싱의 종류는 3가지가 있음.
# # <ul class="lst_detail_t1">
# ul=dom.find('ul',class_='lst_detail_t1')
# lis=ul.find_all('li') #[li,li,li,...,li] 197개
# for li in lis:
#     img=li.find('img')['src']       # 이미지 경로 추출.
#     title = li.find('dt',class_='tit').find('a').text # 영화제목 추출
#     rating = li.find('span',class_='num').text #별점 추출
#     # ---------------------------------------------------------- 아래 긴 코드를 이렇게 수정.
#     reserv = li.find('div', class_='star_t1 b_star')
#     if reserv==None :
#         temp=''
#     else:
#         temp=reserv.find('span',class_='num').text
#     reserv=temp
#     # reserve = li.find('div',class_='star_t1 b_star').find('span',class_='num').text #예매율 추출 //전체를 돌리니 예매율이 없는게 있음.
#     #class ="info_txt1" >
#     play = li.find('dl',class_='info_txt1').text    #상영시간 추출
#     playlist=play.split('|') #[]
#     playtime=''
#     for p in playlist:
#         if p.count('분')==1:             #분만 추출하기
#             if p.count('개요')==1:        # 미정상 데이터 있을시 변수처리.
#                 p=p.replace('개요','')
#             playtime=p.strip()
#             break
#     cur.execute(sql,(title,rating,reserv,playtime))
# con.commit()
# con.close()