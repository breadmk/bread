import os
import sys
import urllib.request
import json
import cx_Oracle
con=cx_Oracle.connect("happy/day@localhost:1521/xe")
cur = con.cursor()
sql="insert into book values (book_seq.nextval,'{}','{}','{}','{}','{}','{}')"
client_id = "7CAC11uBnXpcEgjr8qR7"
client_secret = "vosC6CrO49"
encText = urllib.parse.quote("머신러닝")
# url = "https://openapi.naver.com/v1/search/book.json?statr=1&display=100&query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/book.json?statr=101&display=100&query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/book.json?start={}&display=100&query=" + encText # json 결과

for s in range(1,200,100):  # s= 1,101  1부터 200까지 100씩 증가

    # https://openapi.naver.com/v1/search/book.json
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url.format(s))
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result=response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
    dic=json.loads(result)
    # print(dic)
    # print(dic['items'])
    # 책제목, 책이미지url,저자,가격,출판사,상세설명
    for d in dic['items']:
        title=d['title']
        title=title.replace('<b>머신러닝</b>','머신러닝').replace('<b>러닝</b>','러닝').replace('<b>머신 러닝</b>','머신러닝')
        title=title.replace("'","")
        image=d['image'] #이미지 크기가 작아서 원본 가져오려고 자름.
        if image.find('?')!= -1:
            image = image[:image.index('?')]
            # ? 뒤에 다 짜름.
        # print(image.index('?'))  # 62번째에 ? 가 있음
        author = d['author']
        price = d['price']
        publisher = d['publisher']
        description = d['description'].replace('<b>머신러닝</b>','머신러닝')
        description = description.replace('■','').replace('▶','').replace('*','').replace('<b>러닝</b>','러닝')
        description=description.replace("'","")
        # print('제목:',title)
        # print('이미지:', image)
        # print('저자:', author)
        # print('가격:', price)
        # print('출판사:', publisher)
        # print('상세설명:', description)

        print(sql.format(title,image,author,price,publisher,description))
        cur.execute(sql.format(title,image,author,price,publisher,description))
con.commit()
con.close()

a='abc1234'
# print(a.index('c'))
# print(a.find('c'))
# print(a.index('z'))       #없으면 없다가 아니라 에러를 발생시킴
# print(a.find('z'))          #없으면 -1
# print(a[:a.find('z')])         #abc123


#--------------------------------------------


import cx_Oracle
import os
import sys
import urllib.request
import json
client_id = ""
client_secret = ""
encText = urllib.parse.quote("머신러닝")
# # url = "https://openapi.naver.com/v1/search/book.json?start=1&display=100&query=" + encText # json 결과
# # url = "https://openapi.naver.com/v1/search/book.json?start=101&display=100&query=" + encText # json 결과
con=cx_Oracle.connect('happy/day@localhost:1521/xe')
cur=con.cursor()
sql="insert into book values (book_seq.nextval,'{}','{}','{}','{}','{}','{}')"
url = "https://openapi.naver.com/v1/search/book.json?start={}&display=100&query=" + encText # json 결과
for s in range(1,200,100):  # s=1,101
    request = urllib.request.Request(url.format(s))
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result=response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
    dic=json.loads(result)
    # print(dic)
    # print(dic['items'])
    # 책제목,책이미지url,저자,가격,출판사,상세설명
    for d in dic['items']:
        title=d['title'].replace('<b>머신러닝</b>','머신러닝').replace('<b>머신 러닝</b>','머신러닝')
        title=title.replace("'","")
        img=d['image']
        if img.find('?')!=-1:
            img=img[:img.index('?')]
        author=d['author']
        price=d['price']
        publisher=d['publisher']
        description=d['description'].replace('<b>머신러닝</b>','머신러닝').replace('<b>머신 러닝</b>','머신러닝')
        description=description.replace("'","")
        description=description.replace('■ ','').replace('★','')
        # print(sql.format(title,img,price,publisher,author,description))
        cur.execute(sql.format(title,img,price,publisher,author,description))

        # print('제목:'+title)
        # print('이미지경로:'+img)
        # print('가격:'+price)
        # print('출판사:'+publisher)
        # print('저자:'+author)
        # print('상세내용:'+description)
con.commit()
con.close()

