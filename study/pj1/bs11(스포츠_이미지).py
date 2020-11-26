import requests
from bs4 import BeautifulSoup
def saveImg(imgurl,title):
    # print(imgurl)
    # print(imgurl.index('?'))
    # print(imgurl[imgurl.index('?')-4:imgurl.index('?')])
    title = title.replace('[','')
    title = title.replace(']', '')
    title = title.replace('?', '')
    title = title.replace(',', '')
    title = title.replace("'", '')
    filename ='img\\sport\\'+title+imgurl[imgurl.index('?')-4:imgurl.index('?')]
    print(filename)
    # print(title)
    r=requests.get(imgurl)
    f=open(filename,mode='wb')
    f.write(r.content)
    f.close()

def makeData(pageurl):
    r=requests.get(pageurl)
    # print(r)
    d=BeautifulSoup(r.text,'lxml')
    # print(d)
    # imgUrl=d.find('span',class_='end_photo_org').find('img')['src']
    imgUrl = d.find('div',id='newsEndContents').find('img')['src']
    title=d.find('h4').text
    saveImg(imgUrl, title)
    # print(imgUrl)
    # print(title)
    content = d.find('div',id='newsEndContents').text
    # print(content)
    str = "{}::\n{}".format(title,content)
    # print(str)


url='https://sports.news.naver.com/index.nhn'
res=requests.get(url)
# print(res.text)
dom=BeautifulSoup(res.text,'lxml')
aes=dom.find_all('a',class_='link_today')
# print(len(aes))

for a in aes:
    h = a['href']
    pageurl = 'https://sports.news.naver.com/' + a['href']
    # print(pageurl)
    makeData(pageurl)


