import requests
from bs4 import BeautifulSoup
import cx_Oracle
con=cx_Oracle.connect('big/big@localhost:1521/xe')
cur=con.cursor()
sql = "insert into ranking values('{}','{}','{}','{}','{}','{}')"
url='https://www.alexa.com/topsites'
res=requests.get(url)
dom=BeautifulSoup(res.text,'lxml')
trs=dom.find_all('div',class_='tr site-listing')
# print(trs)
for tr in trs:
    # print(tr)
    rank=tr.find('div',class_='td').text
    # print(rank)
    site=tr.find('a').text
    # print(site)
    dailyTime=tr.find_all('div',class_='td right')[0].text
    # print(dailyTime)
    pageviews=tr.find_all('div',class_='td right')[1].text
    # print(pageviews)
    traffic=tr.find_all('div',class_='td right')[2].text
    # print(traffic)
    totalsites=tr.find_all('div',class_='td right')[3].text
    # print(totalsites)
    print(rank,site,dailyTime,pageviews, traffic, totalsites)
    cur.execute(sql.format(rank, site, dailyTime, pageviews, traffic, totalsites))
con.commit()
con.close()

