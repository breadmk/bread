import requests
from bs4 import BeautifulSoup
import json

def saveImg(img,title):
    # print(img[-4:])
    name=img[-4:]
    title=title.replace('?','')
    filename='..\\img\\youtube\\'+title+name
    # print(filename)
    r=requests.get(img)
    with open(filename,mode='wb')as f1:
        f1.write(r.content)


with open('..\\data\\youtube.csv',mode='w',encoding='utf-8')as f:

    for i in range(1,4):
        url = 'https://moobe.co.kr/api/contents?page={}'.format(i)
        recvd=requests.get(url)
        # print(recvd)
        dom = BeautifulSoup(recvd.text,'lxml')
        # print(dom.text)
        dic = json.loads(dom.text)
        content =dic['contents']
        for title1 in content:
            title=title1['title']
            addr=title1['store']['address1']
            img=title1['thumbnailUrl']
            saveImg(img,title)
            # print(img)
            str = '{}:\n-{}\n'.format(title,addr)
            f.write(str)