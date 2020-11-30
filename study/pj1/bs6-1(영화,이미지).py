# 영화제목, 점수, 예매율, 상영시간을 추출하여 data\\movie.csv 저장
# 영화포스는 img폴더에 저장.

import requests
from bs4 import BeautifulSoup

def saveImg(imgurl,imgtitle):
    # print(imgurl[79:84])

    filename='img\\'+imgtitle+'.jpg'
    r=requests.get(imgurl)
    with open(filename,mode='wb')as f2:
        f2.write(r.content)

def saveImg(imgurl):

    # imgurl=imgurl.replace('?','')
    # print('****'+imgurl+'*****')
    # imgurl = imgurl.replace('e', '')
    # print(imgurl)
    # print(imgurl[79:84])
    filename='img\\'+imgtitle+'.jpg'





with open('data\\movie.csv',mode='w',encoding='utf-8')as f:
    url='https://movie.naver.com/movie/running/current.nhn'
    re=requests.get(url)
    # print(re.text)
    dom=BeautifulSoup(re.text,'lxml')
    ul=dom.find('ul',class_='lst_detail_t1')
    lis=ul.find_all('li')
    # print(lis)
    # lis=dom.find_all('li')
    # print(li)/
    # result=[]
    # print(len(lis))

    for i in range(len(lis)):
        tit=lis[i].find('dt',class_='tit')
        title=tit.find('a').text    #제목
        # print(title)
        span=lis[i].find('span',class_='num').text #별점
        # print(span)
        # div = lis[i].find('div', class_='star_t1 b_star').find('span',class_='num').text
        # print(div)
        if lis[i].find('div', class_='star_t1 b_star') and lis[i].find('span',class_='num'):# 예매율
            booking=lis[i].find('div', class_='star_t1 b_star').find('span',class_='num').text
            # print(booking)
        else:
            booking=''
            # print(booking)
        # time=lis[i].select('dd', class_='split')
        # print(time)
        # time=lis[i].select('dd',class_='split')
        # print(time)
        imgrul=lis[i].find('img')['src']
        imgtitle=tit.find('a').text
        imgrul=imgrul.strip()
        # print(imgrul)
        # saveImg(imgrul,imgtitle)
        saveImg(imgrul)
        # f.write('{},{},{}\n'.format(title,span,booking))






    # with open(filename,mode='wb') as f2:
    #     f2.write()
