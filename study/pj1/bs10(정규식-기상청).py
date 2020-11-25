import requests
import re
url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
recvd=requests.get(url)
# print(recvd)

# <location wl_ver="3">
# 줄바꿈 포함 // re.DOTALL  //문자1개이상 조회 // + // 게으른 방식 // ? // ( ) // 내가 원하는 데이터만 추출
locations = re.findall(r'<location wl_ver="3">(.+?)</location>',recvd.text,re.DOTALL)
# print(len(locations))
for location in locations:
    # print(location)
    # province 만 찾는 경우 아랫줄;
    # province=re.findall(r'<province>(.+?)</province>',location,re.DOTALL)
    # print(province)
    # province 랑 city 같이 찾는 경우 # [('서울ㆍ인천ㆍ경기도', '서울')]
    pc = re.findall(r'<province>(.+?)</province>.+?<city>(.+?)</city>',location,re.DOTALL)
    # print(pc)
    # pc[0] = ('서울ㆍ인천ㆍ경기도', '서울')
    province=pc[0][0]
    city = pc[0][1]
    # print(province)  # 서울ㆍ인천ㆍ경기도
    # print(city)      # 서울
    datas = re.findall(r'<data>(.+?)</data>',location,re.DOTALL)
    # print(len(datas))
    for data in datas:
       # print(data)
       temps = re.findall(
           r'<mode>(.+?)</mode>.+?'
           r'<tmEf>(.+?)</tmEf>.+?'
           r'<wf>(.+?)</wf>.+?'
           r'<tmn>(.+?)</tmn>.+?'
           r'<tmx>(.+?)</tmx>.+?'
           r'<reliability></reliability>.+?'
           r'<rnSt>(.+?)</rnSt>',
           data,re.DOTALL)
       print(temps)


       break


    break

# a= [('서울ㆍ인천ㆍ경기도', '서울'),('서울ㆍ인천ㆍ경기도', '인천')]
# alist[0]=('서울ㆍ인천ㆍ경기도', '서울')
# alist[0][0]=('서울ㆍ인천ㆍ경기도')
# alist[1][1]=('인천')




















