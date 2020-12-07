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
sql = "insert into stock (title,siga,gijun,beadang,suik,beadang1) values(%s,%s,%s,%s,%s,%s)"
for page in range(1,26):

    url='https://finance.naver.com/sise/dividend_list.nhn?&page={}'.format(page)
    res=requests.get(url)
    # print(res)
    dom = BeautifulSoup(res.text,'lxml')
    # table = dom.select("#contentarea_left > table.type_1.tb_ty > tbody")
    with open(os.path.join('data','stock1.csv'),mode='w',encoding='utf-8')as f:
        table = dom.select('#contentarea_left > table.type_1.tb_ty > tbody > tr')
        # print(table)
        # if table==dom.find_all(class_='tr_frst') or dom.find_all(class_='tr_last'):
        #     continue
        # print(table)
        # str = "가"
        # k=0
        # k=k+7\
        k=0
        for i in table:
            if page==25 and k==52:
                break
            elif k%7!=0:
                if k%7!=6:
            # if type(i.find("td",class_="num").text)==:
            #         print(i.text.strip())
            #         i=i.text.strip()
            #         print(i)
                    tds=i.find_all("td")
                    title=tds[0].text
                    # print(title)
                    siga = tds[1].text
                    # siga = tds[1].text.replace("-","0").replace(",","")
                    # siga = tds[1].text.replace(",", "")
                    siga = tds[1].text.replace(",","")
                    siga = float(siga)
                    gijun = tds[2].text
                    beadang = tds[3].text.replace(",","")
                    beadang = float(beadang)
                    suik = tds[4].text
                    # print(siga)
                    # print(k)
                    beadang1 = tds[5].text.replace(",", "")
                    if(beadang1[-1]=="-"):
                        beadang1=beadang1.replace("-","0")
                    # print(beadang1)
                    beadang1 = float(beadang1)
                    str = '{},{},{},{},{},{}\n'.format(title, siga, gijun, beadang, suik, beadang1)
                    print(str)
                    # for j in tds:
                    #     title = j[0].text
                    #     print(title)
                    # tds1 = (i+50).find("td").text
                    cur.execute(sql, (title, siga, gijun, beadang, suik,beadang1))
            k = k + 1
con.commit()
con.close()
                    # print(i[0])

            # elif k%7!=6:
            #     print(i)

            # print(len(i))


        # sss = re.compile(r'[^ \u3131-\u3163\uac00-\ud7a3]+',str)
        # print(sss)

        # table = filter(None,table)
        # for i in table:
        #     print(i)
        #
        # for i in table:
        #     # no_space(i.get_text())
        #     # title = i.find_all('a')
        #     index = i.find_all('td')
        #     # if index[0]=="":
        #     #     index[0]=filter(None,index[0])
        #     # print(index)
        #     title = index[0].text.strip()
        #     # title = title.strip()
        #     # print(title)
        #     # print(title)
        #     siga = index[1].text.strip()
        #     # print(siga)
        #     gijun = index[2].text.strip()
        #     # print(gijun)
        #     beadang = index[3].text.strip()
        #     # print(beadang)
        #     suik = index[4].text.strip()
        #     # print(suik)
        #     beadang1 = index[5].text.replace('%','').strip()
        #     # beadang1 = beadang1
        #     # print(beadang1)
        #     str = '{},{},{},{},{},{}\n'.format(title,siga,gijun,beadang,suik,beadang1)
        #
        #     print(str)

#             # f.write(str)
#             time.sleep(1)
#             print(str)
#             cur.execute(sql, (title, siga, gijun, beadang, suik, beadang1))
# con.commit()
# con.close()