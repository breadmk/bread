# import bs4  # 다가져오겠다.
# import requests
from bs4 import BeautifulSoup  #BeautifulSoup 얘만 가져오겠다. 대문자=클래스
#
# url='http://www.naver.com'
# recvd=requests.get(url)
# print(recvd)    # 접근 결과 코드
# # print(recvd.text)  # html 코드
# print(recvd.encoding) # 인코딩 모드
# print(recvd.headers)    # header 정보

#-------------------------------------------


# import , main()
from bs4 import BeautifulSoup
# 웹페이지에 접근하여 태그 인식 많이 쓰는 모듈.

f=open('data\\test.html',encoding='utf-8').read()
# print(f)
# BeautifulSoup(웹페이지,파싱방식)
# 파싱의 역할은 불완전한 html 문서를 형식에 맞게 추가해서 처리해준다. 가령 /body가 빠져도
# 추가해서 출력해준다.
# 파싱 : html.parser(기본제공) , html5lib(설치필요), lxml (속도는 lxml이 빠르다)
# dom=BeautifulSoup(f,'html.parser')
dom=BeautifulSoup(f,'lxml')
# print(dom)

# dom.find('태그') //태그 추출
# dom.태그         //태그 추출
# dom.find_all('태그')    //모든 태그 추출.

# div=dom.find('div')
# div=dom.div
# print(div)

# divs=dom.find_all('div')
# print(divs)     # 반환형은 리스트 [div,div,....]

# ps=dom.find_all('p')
# print(ps)       #[p,p,...] 리스트로 반환

# --------------------------------------
# div1=dom.div  # 전체 div가져오기
# div2=div1.div # 전체 div에서 첫번째 div 가져오기
# ps=div2.find_all('p')   # 첫번째 div 안에서 모든 p 태그 가져오기.
# print(ps)
# print('-'*30)

# dom.find('태그',class_="클래스명")      예약어를 피하기위해 class_
# dom.find( '태그',{'class':"클래스명"} ) { 안에 들어가니 ' ' 찍어주기 }
# cl=dom.find(class_='ex_class')
# print(cl)
# cl1=dom.find(all,{'class':'ex_class'})
# print(cl)

# dom.find_all('태그',class_="클래스명")
# dom.find_all( '태그',{'class':"클래스명"} )
# dom.find_all(class_='ex_class')   #전체 추출.

# exs=dom.find_all(class_='ex_class')
# exs1=dom.find_all(all,{'class':'ex_class'})
# print(exs1)
# sisters = dom.find_all(class_='sister')
# print(sisters)
# sisters1 = dom.find_all(all,{'class':'sister'})
# print(sisters1)

#id가 third인 모든 태그
thirds=dom.find_all(id='third')
# print(thirds)
# id가 third인 모든 태그의 첫번째 p태그
# print(thirds[0])



# a=['one']
# print(a[0])
# b='one'
# print(b)
















