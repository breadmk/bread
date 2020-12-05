import re
def no_space(text):
    text = re.sub('&nbsp; | &nbsp; | \n|\t|\r',"",text)

import requests
from bs4 import BeautifulSoup
import os
import pymysql as my
import time
con=my.connect(host='localhost',user='root',password='1234',db='pkc',charset='utf8')
cur = con.cursor()
sql = "insert into stock1 (title,siga,gijun,beadang,suik,beadang1) values(%s,%s,%s,%s,%s,%s)"
for page in range(0,26):

    url='https://finance.naver.com/sise/dividend_list.nhn?&page={}'.format(page)
    res=requests.get(url)
    # print(res)
    dom = BeautifulSoup(res.text,'lxml')
    # table = dom.select("#contentarea_left > table.type_1.tb_ty > tbody")
    with open(os.path.join('..','data','stock1.csv'),mode='w',encoding='utf-8')as f:

        table = dom.select('#contentarea_left > table.type_1.tb_ty > tbody > tr')
        # print(table)
        # sss = re.compile(r'[^ \u3131-\u3163\uac00-\ud7a3]+',str)
        # print(sss)

        # table = filter(None,table)
        # for i in table:
        #     print(i)

        for i in table:
            # no_space(i.get_text())
            # title = i.find_all('a')
            index = i.find_all('td')
            if index[0]=="":
                index[0]=filter(None,index[0])
            # print(index)
            title = index[0].text
            # title = title.strip()
            # print(title)
            # print(title)
            siga = index[1].text
            # print(siga)
            gijun = index[2].text
            # print(gijun)
            beadang = index[3].text
            # print(beadang)
            suik = index[4].text
            # print(suik)
            beadang1 = index[5].text
            # print(beadang1)
            str = '{}:{}won/{}(yy-mm)/{}won/{}%/{}%\n'.format(title,siga,gijun,beadang,suik,beadang1)
            str = str.replace("\n","")
            # print(str)
#             # f.write(str)
#             time.sleep(1)
            cur.execute(sql, (title, siga, gijun, beadang, suik, beadang1))
con.commit()
con.close()
