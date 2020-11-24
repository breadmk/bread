# data= {'S_PAGENUMBER': 3,
# 'S_MB_CD': 'W0223900',
# 'S_HNAB_GBN': 'I',
# 'hanmb_nm': '임창정',
# 'sort_field': 'SORT_PBCTN_DAY'}
# url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
#
# import requests
# from bs4 import BeautifulSoup
# import cx_Oracle
# conn=cx_Oracle.connect("java01/java01@localhost:1521/xe")
# cur= conn.cursor()
# sql= "insert into music values (music_seq.nextval,'{}','{}','{}')"
# url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
# res= requests.get(url,data=data).text
# # print(res)
# dom=BeautifulSoup(res,'lxml')
# divs=dom.find_all('div',class_='board col')
# div=divs[1]
# # print(div)
# tbody=div.find('tbody')
# trs = tbody.find_all('tr')
# # print(trs)
# # td=trs.find_('td')
# # print(td)
#
# for i in range(len(trs)):
#     name=trs[i].find_all('td')[0].text
#     singer = trs[i].find_all('td')[1].text
#     writer = trs[i].find_all('td')[2].text
#     # print(name)
#     # print(singer)
#     # print(writer)
#     cur.execute(sql.format(name,singer,writer))
# conn.commit()
# conn.close()

#-----------------------------------------

data= {'S_PAGENUMBER': 3,
'S_MB_CD': 'W0223900',
'S_HNAB_GBN': 'I',
'hanmb_nm': '임창정',
'sort_field': 'SORT_PBCTN_DAY'}
url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'

import requests
from bs4 import BeautifulSoup
import cx_Oracle
conn=cx_Oracle.connect("java01/java01@localhost:1521/xe")
cur= conn.cursor()
sql= "insert into music values (music_seq.nextval,:1,:2,:3)"
url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
res= requests.get(url,data=data).text
# print(res)
dom=BeautifulSoup(res,'lxml')
divs=dom.find_all('div',class_='board col')
div=divs[1]
# print(div)
tbody=div.find('tbody')
trs = tbody.find_all('tr')
# print(trs)
# td=trs.find_('td')
# print(td)

for i in range(len(trs)):
    name=trs[i].find_all('td')[0].text
    singer = trs[i].find_all('td')[1].text
    writer = trs[i].find_all('td')[2].text
    # print(name)
    # print(singer)
    # print(writer)
    cur.execute(sql,(name,singer,writer))
conn.commit()
conn.close()