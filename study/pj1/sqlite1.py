# sqllite 사용법 배우기--------------------------------------
# sqlite 다운로드 구글검색.
# sqlite-tools-win32-x86-3330000.zip
# 압축해제하여 D:\sqlite 에 둔다.
# cmd - > d: -> D:\sqlite - sqlite3
# 프롬포트 모양이 sqlite>로 변경됨.

# .open 데이터베이스이름 : 사용할 데이터베이스 지정
# .open pythondb
# .table  : 현재 데이터베이스의 테이블 목록
# create table : 테이블 생성.

# create table member(
#     id char(4),
#     name char(20),
#     age int,
#     email char(30),
#     birthyear int
# );
# .table
# .schema 테이블명   : 테이블 구조 확인 || desc 같은거임.

#  DCM 은 다른 sql문과 같음. (select 문은 삭제함 너무 많아서)
# insert into member values('aaa','kang',20,'aaa@naver.com',2001);
# insert into member values('bbb','kim',25,'bbb@naver.com',1996);
# .header on  : select 사용시 헤더 보여줌
# .mode column : select 사용시 컬럼모드로 출력
# .quit  :  종료.

# 재 접속시마다 설정해줘야함. open 에서 오타나면 테이블 만들어버림 주의;
# sqlite3
# .open pythondb

import sqlite3
# 1) 데이터베이스 연결
con = sqlite3.connect("d:\\sqlite\\pythondb")

# 2) 커서생성
cur = con.cursor()

# 3) 쿼리생성
sql = "select * from member"
# 4) for문을 활용해서 출력하기
for i in con.execute(sql):
    print(i)
# 4) 실행 처리
# cur.execute(sql)
# while(True):
#     row=cur.fetchone()      # 자료 받기 fetchone()하나에 접근 / fetchall  / fetchmany
#     if row==None:           # fetchone()  하나에 접근 하지만 while문으로 돌려서 접근. # 튜플로 반환 ()
#         break
#     print(row)
    # print(row[0],row[1],row[2],row[3],row[4])       # 튜플에서 꺼내오기
# 5) 자원 해제
con.close()

#----------------------입력(insert)----------------------------------
# # 1) 데이터베이스 연결
# con = sqlite3.connect("d:\\sqlite\\pythondb")
#
# # 2) 커서생성
# cur = con.cursor()
# # 데이터 입력은 무한 루프기 때문에 db 연결은 while 밖으로 작성.
# while(True):
#     id=input('사용자id=')
#     if id=="":          #id 입력란에서 enter 입력하면 종료되는 조건문.
#         break
#     name=input('사용자이름=')
#     age=input('사용자나이=')
#     email=input('사용자이메일=')
#     birthyear=input('사용자출생년도=')
#
#     # 3) 쿼리생성
#     # insert into member values('ccc','ccc',11,'ccc@naver.com',2000)
#     sql = "insert into member values('"+id+"','"+name+"',"+age+",'"+email+"',"+birthyear+")"
#     print(sql)
#     # 4) 실행 및 처리
#     cur.execute(sql)
# con.commit()
# # 5) 자원 해제
# con.close()

#----------------- 삭제 -----------------------------------

# 1) 데이터베이스 연결
# con = sqlite3.connect("d:\\sqlite\\pythondb")
#
# # 2) 커서생성
# cur = con.cursor()
# # 3) 쿼리생성
# # insert into member values('ccc','ccc',11,'ccc@naver.com',2000)
# sql = "delete from member"
# # print(sql)
# # 4) 실행 및 처리
# cur.execute(sql)
# con.commit()
# print('삭제완료')
# # 5) 자원 해제
# con.close()