# # join 써서 경로합치기
# from urllib.parse import *
# import re
# import os
# import time
# from bs4 import BeautifulSoup
# from urllib.request import urlretrieve      # 다운로드할때 사용
#
#
# # index.html 을 붙여주기
# url='http://docs.python.org/3.8/library/'
# o=urlparse(url)
# # print('urlpase',o)
# savepath= './'+o.netloc+o.path       # 경로 붙이기
# # print('savepath=',savapath)        # 정규식 아닌 내용
# # if savapath[-1]=='/':
# #     print('디렉토리')
#
# if re.search(r'/$',savepath):   # $ 표시는 문장의 끝 정규식
#     # print('디렉토리1')
#     savepath=savepath+'index.html'      # 문장의 끝에 index.html 붙인거
#
# # print(savepath)
# # 디렉토리 유무확인
# # dirname =  ./docs.python.org/3.8/library/
# if not os.path.exists(os.path.dirname(savepath)):        #savepath가 존재하지 않으면
#     os.makedirs(os.path.dirname(savepath))
# # if not os.path.exists(savapath):        #savepath가 존재하지 않으면
# #     os.makedirs(savapath)
# urlretrieve(url,savepath)
# time.sleep(1)
# html=open(savepath,encoding='utf-8').read()
# # print(html)
#
# # 링크
# dom=BeautifulSoup(html,'lxml')
# links = dom.select('a')
# print(links)
# for a in links:
#     # print(a['href'])
#     pageurl=urljoin(url,a['href'])
#     print(a['href'],'==>',pageurl)

# --------------------------------------------------
from urllib.parse import *
import re
import os
import time
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def download_file(url):
    o=urlparse(url)
    savepath = './'+o.netloc+o.path
    if re.search(r'/$',savepath):
        savepath=savepath+'index.html'
        # print('savepath=',savepath)
    if not os.path.exists(os.path.dirname(savepath)):
        os.makedirs(os.path.dirname(savepath))
    try:
        urlretrieve(url,savepath)
        return savepath
    except:
        print("다운로드 실패",url)
        return None

def enum_link(html,base):
    dom=BeautifulSoup(html,'lxml')
    links = dom.select('a')
    result=[]   # 경로를 리스트로 넣기 위한 변수
    for a in links:
        url=urljoin(base,a['href'])
        result.append(url)
        print(a['href'], '==>', url)
    return result

def analyze_html(url,root_url):
    savapath=download_file(url)
    html = open(savapath,encoding='utf-8').read()       # 해당 파일을 읽어서 html에 저장.
    links=enum_link(html,url)
    # print(links)
    for link_url in links:
        if link_url.find(root_url) == -1:
            continue

    # if not savapath == None:

#
# if __name__ == '__main__':  # 내가 나를 실행하면
#     url='http://docs.python.org/3.8/library/'
#     analyze_html(url,url)

a="blue green red"
print(a.find('red'))        # 11번째에 있다.
print(a.find('green'))      # 5번째에 있다.
print(a.find('blue'))       # 처음에 있다.
print(a.find('orange'))     # -1 없다.