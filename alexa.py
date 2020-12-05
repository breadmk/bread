import requests
from bs4 import BeautifulSoup
import selenium
url='https://www.alexa.com/topsites'
res=requests.get(url)
# print(res)
dom=BeautifulSoup(res.text,'lxml')
listngs = dom.find('div',class_='listings table')
# divs = listngs.find_all('div')
# print(len(divs))
sites = listngs.find_all('div',class_='tr site-listing')
# print(len(sites))
# aaa = listngs.find_all('div',class_='td right')
# print(aaa)
# for j in aaa:
#     Pageviews=j.text
#     print(Pageviews)
for i in sites:
    rank=i.find(class_='td').text
#     print(rank)
    site=i.find(class_='td DescriptionCell').text
#     print(site)
    dailytime=i.find(class_='td right').text
    # print(dailytime)
    pageviews=i.select_one('#alx-content > div.row-fluid.TopSites.Alexarest > section.page-product-content.summary > span > span > div > div > div.listings.table > div:nth-child(2) > div:nth-childs')
    print(pageviews)