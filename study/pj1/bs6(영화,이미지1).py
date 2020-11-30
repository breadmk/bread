# 영화제목, 점수, 예매율, 상영시간을 추출하여 data\\movie.csv 저장
# 영화포스는 img폴더에 저장.

import requests
from bs4 import BeautifulSoup
# url='https://movie.naver.com/movie/running/current.nhn'
# re=requests.get(url)
# # print(re)
# # print(re.text)
# dom=BeautifulSoup(re.text,'lxml')   #파싱의 종류는 3가지가 있음.
# # <ul class="lst_detail_t1">
# ul=dom.find('ul',class_='lst_detail_t1')
# # print(ul)
# lis=ul.find_all('li') #[li,li,li,...,li] 197개
# # print(len(lis))
# for li in lis:
#     img=li.find('img')['src']       # 이미지 경로 추출.
#     # print(img)
#     title = li.find('dt',class_='tit').find('a').text # 영화제목 추출
#     # print(title)
#     score = li.find('span',class_='num').text #별점 추출
#     # print(score)
#     # ---------------------------------------------------------- 아래 긴 코드를 이렇게 수정.
#     reserve = li.find('div', class_='star_t1 b_star')
#     if reserve==None :
#         temp=''
#     else:
#         temp=reserve.find('span',class_='num').text
#     reserve=temp
#     # reserve = li.find('div',class_='star_t1 b_star').find('span',class_='num').text #예매율 추출 //전체를 돌리니 예매율이 없는게 있음.
#
#
#     # print(reserve)
#     #class ="info_txt1" >
#     play = li.find('dl',class_='info_txt1').text    #상영시간 추출
#     # print('**'+play+'**')
#     # play.split('|')       # | 기준으로 자르기
#     # play.split('|')[1]    # | 기준으로 리스트로 접근
#     # play.split('|')[1].strip()    # 좌우 공백 제거
#     # print(play.split('|')[1].strip())   # 완성
#     # playtime=play.split('|')[1].strip()
#     playlist=play.split('|') #[]
#     playtime=''
#     for p in playlist:
#         if p.count('분')==1:             #분만 추출하기
#             if p.count('개요')==1:        # 미정상 데이터 있을시 변수처리.
#                 p=p.replace('개요','')
#             playtime=p.strip()
#             break
#     str='%s,%s,%s,%s'%(title,score,reserve,playtime)    #   %s 로 처리.   '%s'%(변수명)
#     # str='%s,%s,%s'%(title,score,reserve)
#     print(str)
#-----------------------------------------------------------------------------
import os
def saveImg(imgurl,title):
    # print(imgurl)
    # print(imgurl.index('?'))
    # print(len(imgurl))
    # print(imgurl[79:83])
    # print(imgurl[imgurl.index('?')-4:imgurl.index('?')])        #확장자 뽑아내기.
    title=title.replace(":",'')
    filename='img\\movie\\'+title+imgurl[imgurl.index('?')-4:imgurl.index('?')]
    # print(filename)
    r= requests.get(imgurl)         #이미지 경로 접근
    with open(filename,mode='wb')as f1:
        f1.write(r.content)
with open(os.path.join('data','movie.csv'),mode='w',encoding='utf-8')as f:
    url='https://movie.naver.com/movie/running/current.nhn'
    re=requests.get(url)
    dom=BeautifulSoup(re.text,'lxml')   #파싱의 종류는 3가지가 있음.
    # <ul class="lst_detail_t1">
    ul=dom.find('ul',class_='lst_detail_t1')
    lis=ul.find_all('li') #[li,li,li,...,li] 197개
    for li in lis:
        img=li.find('img')['src']       # 이미지 경로 추출.
        title = li.find('dt',class_='tit').find('a').text # 영화제목 추출
        saveImg(img,title)

        score = li.find('span',class_='num').text #별점 추출
        # ---------------------------------------------------------- 아래 긴 코드를 이렇게 수정.
        reserve = li.find('div', class_='star_t1 b_star')
        if reserve==None :
            temp=''
        else:
            temp=reserve.find('span',class_='num').text
        reserve=temp
        # reserve = li.find('div',class_='star_t1 b_star').find('span',class_='num').text #예매율 추출 //전체를 돌리니 예매율이 없는게 있음.
        #class ="info_txt1" >
        play = li.find('dl',class_='info_txt1').text    #상영시간 추출
        playlist=play.split('|') #[]
        playtime=''
        for p in playlist:
            if p.count('분')==1:             #분만 추출하기
                if p.count('개요')==1:        # 미정상 데이터 있을시 변수처리.
                    p=p.replace('개요','')
                playtime=p.strip()
                break
        str='%s,%s,%s,%s\n'%(title,score,reserve,playtime)    #   %s 로 처리.   '%s'%(변수명)
        f.write(str)

#-----------------------------------------------------------------------------
# apple 에만 접근하는법
# a=' 777 |  apple |곰  분    | 아아아 '
# print(a.split('|'))     # | 기준으로 자르고 리스트 형식으로 반환. []
# print( a.split('|') )   # a.split('|') 전체를 변수로 생각하고 리스트로 접근.
# print( a.split('|')[1] )  # 리스트 기준으로 [] 로 접근.
# print( a.split('|')[1].strip() )  #좌우 공백 제거.

# 분 이라는 글씨가 있는 내용만 추출.
# a=' 777 |  apple |곰  분    | 아아아 '
# for s in a.split('|'):
#     print(s,s.count('분'))