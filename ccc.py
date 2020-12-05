import requests
from bs4 import BeautifulSoup
url='https://www.alexa.com/topsites'
res=requests.get(url)
dom=BeautifulSoup(res.text,'lxml')
#alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child(2)
trs=dom.select('#alx-content div.listings.table > div')
# print(len(trs))
size=0
for tr in range(1,trs):
    # size=size+1
    # if size==1:
    #     continue
    # print(tr)
    divs=tr.find_all('div')
    # print(len(divs))
    # for div in divs:
    #     print(len(div))
        # print(div.text)
    rank=divs[0].text
    rank=rank.replace("\n","")
    site=divs[1].text
    site = site.replace("\n", "")
    dailyTime=divs[2].text
    pageviews=divs[3].text
    traffic=divs[4].text
    totalsites=divs[5].text
    print(rank,site,dailyTime,pageviews,traffic,totalsites)

