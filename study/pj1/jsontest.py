import json
import os
import sys
import urllib.request
client_id = "7CAC11uBnXpcEgjr8qR7"
client_secret = "vosC6CrO49"
encText = urllib.parse.quote("성탄절")
# with open('..\\data\\blog.csv',mode='w',encoding='utf-8')as f:
with open(os.path.join('..','data','blog.csv'),mode='w',encoding='utf-8')as f:  # 데이터누적안됌.
    for page in range(0,10):
        url = "https://openapi.naver.com/v1/search/blog?start={}01&display=100&query=".format(page) + encText # json 결과
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
            # print(i['title'],i['description'])
            str='{}::{}\n\n'.format(i['title'],i['description'])
            f.write(str)