# create table music1(
#     no number primary key,
#     title varchar2(100),
#     singer varchar2(100),
#     song varchar2(100)
# );
#
# create sequence music1_seq;

# import requests
# from bs4 import BeautifulSoup
# import cx_Oracle
# conn=cx_Oracle.connect("happy/day@localhost:1521/xe")
# cur= conn.cursor()  # select 할때는 dictionary 커서가 편함.
# sql = "insert into music1 values (music1_seq.nextval,'{}','{}','{}')"
# # 페이지 마다 출력할 수 있게끔 하는법;================================
# for page in range(1,3):  # 1,2 페이지만 출력
#     url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
#     data={'S_PAGENUMBER': page,
#     'S_MB_CD': 'W0726200',
#     'S_HNAB_GBN': 'I',
#     'hanmb_nm': '권지용',
#     'sort_field': 'SORT_PBCTN_DAY'}
#
#     rec = requests.post(url,data=data)
#     # print(rec)
#
#     dom=BeautifulSoup(rec.text,'lxml')
#     tables=dom.find_all('table')
#     # print(len(tables))
#     trs=tables[1].find_all('tr')
#     # print(len(trs)) #11
#     for i in range(1,len(trs)):   # i=1,2,3,4,5,6,7,8,9,10
#         tds=trs[i].find_all('td')
#         title=tds[0].text
#         singer=tds[1].text
#         song=tds[2].text
#         # print(title,singer,song)
#         cur.execute(sql.format(title,singer,song))
# conn.commit()
# conn.close()

#-------------------------- xml 데이터에 대문자가 있으면 소문자로 처리해야 값이 추출된다.--------------------------

import requests
from bs4 import BeautifulSoup
with open('data\\kma.csv',mode='w',encoding='utf-8') as f:

    url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108' #? 있으니 get방식
    res = requests.get(url)
    # print(res.text)
    # bs4
    dom = BeautifulSoup(res.text,'lxml')
    # 서울ㆍ인천ㆍ경기도
    locations = dom.find_all('location')
    # print(len(location))

    for location in locations:
        province=location.find('province').text
        city=location.find('city').text
        # print(province,city)
        datas = location.find_all('data')
        for data in datas:
            mode=data.find('mode').text
            tmEf=data.find('tmef').text # 시간    ( 소문자로 변경 )
            wf=data.find('wf').text     # 기본날씨
            tmn=data.find('tmn').text   # 최저기온
            tmx=data.find('tmx').text
            reliability=data.find('reliability').text
            rnSt=data.find('rnst').text # 최대기온  ( 소문자로 변경 )
            str='{},{},{},{},{},{},{},{},{}\n'.format(province,city,mode,tmEf,wf,tmn,tmx,reliability,rnSt)
            f.write(str)
            # print(str)
            # < mode > A02 < / mode >
            # < tmEf > 2020 - 11 - 27
            # 00: 00 < / tmEf >
            # < wf > 구름많음 < / wf >
            # < tmn > 2 < / tmn >
            # < tmx > 7 < / tmx >
            # < reliability / >
            # < rnSt > 20 < / rnSt >


import requests
from bs4 import BeautifulSoup
# with open('data\\kma.csv',mode='w',encoding='utf-8') as f:

url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108' #? 있으니 get방식
res = requests.get(url)
print(res.text)
# # bs4
# dom = BeautifulSoup(res.text,'lxml')
# # 서울ㆍ인천ㆍ경기도
# locations = dom.find_all('location')
# # print(len(location))
#
# for location in locations:
#     province=location.find('province').text
#     city=location.find('city').text
#     # print(province,city)
#     datas = location.find_all('data')
#     for data in datas:
#         mode=data.find('mode').text
#         tmEf=data.find('tmef').text # 시간    ( 소문자로 변경 )
#         wf=data.find('wf').text     # 기본날씨
#         tmn=data.find('tmn').text   # 최저기온
#         tmx=data.find('tmx').text
#         reliability=data.find('reliability').text
#         rnSt=data.find('rnst').text # 최대기온  ( 소문자로 변경 )
#         str='{},{},{},{},{},{},{},{},{}\n'.format(province,city,mode,tmEf,wf,tmn,tmx,reliability,rnSt)
#         f.write(str)
#         # print(str)



# 정규식 ===========================================================


