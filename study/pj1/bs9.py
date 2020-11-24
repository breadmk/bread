# https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp
# S_PAGENUMBER: 4
# S_MB_CD: W0726200
# S_HNAB_GBN: I
# hanmb_nm: 권지용
# sort_field: SORT_PBCTN_DAY

import requests
url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
data={'S_PAGENUMBER': 1,
'S_MB_CD': 'W0726200',
'S_HNAB_GBN': 'I',
'hanmb_nm': '권지용',
'sort_field': 'SORT_PBCTN_DAY'}

# print(rec)

# 1페이지에 있는 저작물명,가수명,작사를 오라클에 저장하세요.
from bs4 import BeautifulSoup
import requests
import cx_Oracle
con=cx_Oracle.connect("happy/day@localhost:1521/xe")
cur = con.cursor()
sql = "insert into music values (music_seq.nextval,'{}','{}','{}')"
url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
rec = requests.post(url,data=data).text
dom=BeautifulSoup(rec,'lxml')
divs = dom.find_all('div',class_='board col')
div=divs[1]
# print(div)
tbody=div.find('tbody')
# print(tbody)

trs = tbody.find_all('tr')
# print(trs)

for i in range(len(trs)):
    name=trs[i].find_all('td')[0].text
    singer=trs[i].find_all('td')[1].text
    writer=trs[i].find_all('td')[2].text
    # print(name)
    # print(writers)
    # print(writers)
    cur.execute(sql.format(name,singer,writer))
con.commit()
con.close()


# for i in range(tbody):
#     name=tbody.find('td')[0]
#     print(name)

# for i in range(trs):
    # print(trs)

# tds = trs.find_all('td')
# print(tds)
# name = trs.find('td')
# print(name)
# print(div.text)
# for i in range(trs):
#     print(trs.find('td')[0])
# name=trs.find_all('td')[0].text
# singer=div.find_all('td')[1].text
# writer=div.find_all('td')[2].text
# print(name)

# for i in range(name):














