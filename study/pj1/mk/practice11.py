import requests
from bs4 import BeautifulSoup
url='https://comic.naver.com/webtoon/list.nhn?titleId=749632&weekday=mon&page=1'
res = requests.get(url)
# print(res)
dom = BeautifulSoup(res.text,'lxml')
view=dom.find_all(class_='title')
# view=dom.find(class_='title')
# print(view)
for h in view:
    print(h.text,end='')

# print(view.text)

