# 만개의 레시피에서 밑반찬 레시피를 recipe.txt 로 저장하세요.

import requests
from bs4 import BeautifulSoup

def makeData(pageurl):
    r=requests.get(pageurl)
    d=BeautifulSoup(r.text,'lxml')
    # print(d)
    title = d.find('h3').text
    # materal = d.find('div',class_='ready_ingre3').text
    # print(title)
    # materal=materal.replace('\n','')
    # materal = materal.replace('   ', '')
    # print(materal)
    view_step=d.find('div',class_='view_step')
    # print(view_step)
    # divs = view_step.find_all('div',{'class':'media-body'})
    divs = view_step.find_all('div',class_='media-body')
    # print(divs)

    for div in divs:
        # i=i+1
        rece = (div.text)
        # print(str(i)+')'+div.text)
        # str = "{}\n::{}\n".format(title,rece)
        # f.write(str)
        print(rece)
       
# with open('data\\recipe.txt',mode='w',encoding='utf-8') as f:


url='https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4=63&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='
res=requests.get(url)
# print(res)
dom = BeautifulSoup(res.text,'lxml')
# print(dom)
# lis = dom.find_all('li',class_='common_sp_list_li')
# print(len(lis))
div=dom.find_all('div',class_='common_sp_thumb')
# print(len(div))
for a in div:
    aes = a.find('a')['href']
    # print(aes)
    pageurl = 'https://10000recipe.com'+aes
    # print(pageurl)
    # print(h)
    makeData(pageurl)
    break
# --------------------------------------





# < div class ="common_sp_caption_tit line2" > 초간단 아이반찬 오징어간장조림 아이밑반찬으로 좋아요 < / div >