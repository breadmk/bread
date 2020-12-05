# import os
# import sys
# import json
# import urllib.request
# import os
# import cx_Oracle
# con=cx_Oracle.connect("happy/day@localhost:1521/xe")
# cur = con.cursor()
# sql="insert into book values (book_seq.nextval,'{}','{}','{}','{}','{}','{}')"
# client_id = "7CAC11uBnXpcEgjr8qR7"
# client_secret = "vosC6CrO49"
# encText = urllib.parse.quote("머신러닝")
# with open (os.path.join('data','book.csv'),mode='w',encoding='utf-8')as f:
#     url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
#     # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
#     request = urllib.request.Request(url)
#     request.add_header("X-Naver-Client-Id",client_id)
#     request.add_header("X-Naver-Client-Secret",client_secret)
#     response = urllib.request.urlopen(request)
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         result = response_body.decode('utf-8')
#         # print(response_body.decode('utf-8'))
#     else:
#         print("Error Code:" + rescode)
#     dic=json.loads(result)
#
#     for i in dic['items']:
#         title=i['title']
#         image=i['image']
#         author=i['author']
#         price=i['price']
#         publisher=i['publisher']
#         description=i['description']
#         # print(i['title'],i['image'],i['author'],i['price'],i['publisher'],i['description'])
#         # str = '{}::{}::{}::{}::{}::{}\n\n'.format(i['title'],i['image'],i['author'],i['price'],i['publisher'],i['description'])
#         # f.write(str)
#         cur.execute(sql.format(title,image,author,price,publisher,description))
# con.commit()
# con.close()

#------------------------------------------

import os
import sys
import json
import urllib.request
import os
import pymysql as my
con=my.connect(host='localhost',user='root',password='1234',db='pkc',charset='utf8')
cur = con.cursor()
sql="insert into book (title,image,author,price,publisher,description) values (%s,%s,%s,%s,%s,%s)"
client_id = "7CAC11uBnXpcEgjr8qR7"
client_secret = "vosC6CrO49"
encText = urllib.parse.quote("머신러닝")
with open (os.path.join('data','book.csv'),mode='w',encoding='utf-8')as f:
    for page in range(0,2):
        url = "https://openapi.naver.com/v1/search/book?start{}01&display=100&query=" + encText # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url.format(url))
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            # print(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
        dic=json.loads(result)

        for i in dic['items']:
            title=i['title']
            image=i['image']
            author=i['author']
            price=i['price']
            publisher=i['publisher']
            description=i['description']
            # print(i['title'],i['image'],i['author'],i['price'],i['publisher'],i['description'])
            # str = '{}::{}::{}::{}::{}::{}\n\n'.format(i['title'],i['image'],i['author'],i['price'],i['publisher'],i['description'])
            # f.write(str)
            cur.execute(sql,(title,image,author,price,publisher,description))
    con.commit()
    con.close()


