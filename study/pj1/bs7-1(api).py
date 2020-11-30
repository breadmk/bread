## 성탄절로 1000건 검색하여 제목과 상세내용을 blog.csv 로 저장하세요.
# 뽑는법
# for i in range(1,1000,100):
#     url = 'aabc?start={}&display=100'.format(i)
#     print(url)


# for i in range(1,1000,100):
#     for j in range(1,10):
#         url = 'aabc?start={}&display={}00'.format(i,j)
#         print(url)




import os
import sys
import json
import urllib.request
# client_id = "7CAC11uBnXpcEgjr8qR7"
# client_secret = "vosC6CrO49"
# encText = urllib.parse.quote("성탄절")
# with open(os.path.join('data','blog.csv'),mode='a',encoding='utf-8')as f:   # 모드를 a 로 해야 추가됌.
#     for i in range(1,1000,100):
#         url = "https://openapi.naver.com/v1/search/blog?start={}&display=100&query=" + encText # json 결과
#         # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
#         request = urllib.request.Request(url.format(i))
#         request.add_header("X-Naver-Client-Id",client_id)
#         request.add_header("X-Naver-Client-Secret",client_secret)
#         response = urllib.request.urlopen(request)
#         rescode = response.getcode()
#         if(rescode==200):
#             response_body = response.read()
#             result = response_body.decode('utf-8')
#             # print(response_body.decode('utf-8'))
#         else:
#             print("Error Code:" + rescode)
#         dic=json.loads(result)
#         # print(dic)
#         for i in dic['items']:
#             # print(i['title'],i['description'])
#             str = '{}::{}\n'.format(i['title'], i['description'])
#             f.write(str)

# print("-"*50)
#
# client_id = "7CAC11uBnXpcEgjr8qR7"
# client_secret = "vosC6CrO49"
# encText = urllib.parse.quote("가을")
# url = "https://openapi.naver.com/v1/search/movie.json?start=1&display=100&query=" + encText # json 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result = response_body.decode('utf-8')
#     # print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)
# dic=json.loads(result)
# print(dic)

#-----------------------------------------------------------------

# # i have a dream 을 검색하여 한국어로 번역하세요---------------------

import os
import sys
import urllib.request
# client_id = "xqsh8LtDECfIs8TqgzxY"
# client_secret = "xKKuJOAsp8"
# with open('data\\dream.txt',encoding='utf-8',mode='r')as f:
#     str=f.read()
#     encText = urllib.parse.quote(str)
#     data = "source=en&target=ko&text=" + encText
#     url = "https://openapi.naver.com/v1/papago/n2mt"
#     request = urllib.request.Request(url)
#     request.add_header("X-Naver-Client-Id",client_id)
#     request.add_header("X-Naver-Client-Secret",client_secret)
#     response = urllib.request.urlopen(request, data=data.encode("utf-8"))
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         result1=response_body.decode('utf-8')
#         # print(response_body.decode('utf-8'))
#
#     else:
#         print("Error Code:" + rescode)
#
#     dic=json.loads(result1)
#     # print(dic)
#     for i in dic["message"]:
#         print(i)
#         for j in i['result']:
#             print(j['translatedText'])



