import requests
import json
#  제이슨 문서 연습
# with open('data\\sports.csv',mode='w',encoding='utf-8')as f:
#
#     url='https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
#     res = requests.get(url)
#     # print(res.text)
#     dic=json.loads(res.text)
#     # print(dic)
#     # json web viewer 로 format 하기.
#
#     # 기사제목, 내용 출력.
#
#     # print(dic['list'])      # 결과값이 리스트안에 출력 [{},{},{},...]
#
#     for i in dic['list']: # i={},{},{},....
#         str='{}::{}\n'.format(i['title'],i['subContent'])     #구분 기호로 제목과 내용 나눔. 형식 자유
#         # print(str)       # json 문서에 접근
#         f.write(str)

#----------------------------------다음에서 증권 긁기------------------------------------
# # import fake_useragent   # 403 에러가 나와서 fake_useragent 를 사용해서 숨겨서 접근
# from fake_useragent import UserAgent
# with open('data\\money.csv',mode='w',encoding='utf-8')as f:
#     ua=UserAgent()      #UserAgent ua= new UserAgent() 자바소스로 보면 이 소스임. 객체생성.
#     # print(ua.chrome)    # 크롬 객체 생성.
#     # print(ua.ie)        # 인터넷익스플로러 객체 생성
#     headers={'user-agent':ua.chrome,'referer' : 'https://finance.daum.net/'}
#     url='https://finance.daum.net/api/search/ranks?limit=10'
#     res = requests.get(url, headers=headers)
#     # res=requests.get(url)   # referer 이전페이지
#     # print(res)
#     dic= json.loads(res.text)
#     # print(dic)
#     # print(dic['data'])
#     for i in dic['data']:
#         str='{},{},{},{}\n'.format(i['rank'],i['name'],i['tradePrice'],i['changeRate'])
#         # print(i['name'],i['tradePrice'],i['changeRate'])
#         f.write(str)

#-------------------------------------------------------------------------------

# import os
# import sys
# import json
# import urllib.request
# client_id = "7CAC11uBnXpcEgjr8qR7"
# client_secret = "vosC6CrO49"
# encText = urllib.parse.quote("성탄절")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과 display=100& <--넣어서 100개 검색
# # url = "https://openapi.naver.com/v1/search/blog?display=100&query=" + encText # json 결과 display=100& <--넣어서 100개 검색
# # url = "https://openapi.naver.com/v1/search/blog?start=101&display=100&query=" + encText #start=101& 101번째부터 읽기.
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result=response_body.decode('utf-8')
#     # print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)
# dic=json.loads(result)
# print(dic)


# 성탄절로 1000건 검색하여 title,discription (제목,상세내용)을 blog.csv로 저장하세요. for{}.format



import os
import sys
import json
import urllib.request
client_id = "7CAC11uBnXpcEgjr8qR7"
client_secret = "vosC6CrO49"
encText = urllib.parse.quote("성탄절")
with open('data\\blog.csv',mode='w',encoding='utf-8')as f:
    for page in range(0,10):

        url = "https://openapi.naver.com/v1/search/blog?start={}01&display=100&query=".format(page) + encText # json 결과 display=100& <--넣어서 100개 검색
        # url = "https://openapi.naver.com/v1/search/blog?display=100&query=" + encText # json 결과 display=100& <--넣어서 100개 검색
        # url = "https://openapi.naver.com/v1/search/blog?start=101&display=100&query=" + encText #start=101& 101번째부터 읽기.
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result=response_body.decode('utf-8')
            # print(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
        dic=json.loads(result)
        # print(dic['items'])
        for i in dic['items']:
            str='{},{}\n\n'.format(i['title'],i['description'])
            # print(i['title'],i['description'])
            f.write(str)

