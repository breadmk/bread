from bs4 import BeautifulSoup
with open('data\\test.html',mode='r',encoding='utf-8') as f:
    txt=f.read()
    # print(txt)
    # print(type(txt))
    dom=BeautifulSoup(txt,'lxml')
    # print(dom)
    # classes=dom.find_all(class_="ex_class")
    # print(classes[1])

    # 태그가 div인 것 모두 추출.
    # divs = dom.find_all('div')
    # print(divs)

    # div태그중에  'ex_class' 클래스중에 첫 번째 것 추출
    # divs=dom.find('div',{'class':"ex_class"})
    # print(divs)

    # div태그중에  클래스가 'ex_class' 인것 모두 추출
    # divs=dom.find_all('div',{'class':"ex_class"})
    # print(divs)

    # 'ex_class' 인것 모두 추출
    # divs=dom.find_all(class_='ex_class')
    # print(divs)

    # id가 'ex_id' 추출 (하나는 하나만 존재) find_all 개념이 없음.
    # ids=dom.find(id='ex_id')
    # print(ids)

    # id가 'ex_id' 인것중 모든 p태그 추출
    # ids = dom.find(id='ex_id')
    # ps=ids.find_all('p')
    # print(ps)       # 반환형 list

#---------------------------------------
# data 추출
    # dom.string
    # dom.text
    # dom.get_text

# 속성추출
#     dom['속성']
#     dom.get('속성')
#     dom.attrs['속성']

#---------------------------------------

# DOM추적 ----------------------------------

# dom.parent                부모
# dom.parents               조상,객체로 반환(for문 활용)
# dom.children              자식
# dom.descendants           자손
# dom.next_siblings          아래쪽 형제요소
# dom.previous_siblings     위쪽 형제요소

# dom 추적 ----------------------------------


# title에 있는 글씨만 추출.
# title = dom.find('title')
# print(title.string)     #뷰티플 숩
# print(title.text)       #뷰티풀 숩
# print(title.get_text()) #뷰티풀 숩

    # a 태그의 텍스트(내용 추출)
    # aes=dom.find_all('a')
    # print(aes) #list임.
    # for a in aes:
    #     print(a.text)
    #     print(a.get('href'))


#     id가 link2인 요소의 class 추출
#     link2=dom.find(id='link2')
#     print(link2.get('class'))



    # title = dom.find('p',class_='title')
    # print(title)
    # print(title.parent)
    # print('parents',title.parents)
    # for p in title.parents:
    #     print(p)
    #     print('-'*30)

# 아이디가 second 인 div

# div=dom.find(id='second')
# print(div)
# divchild=div.children
# # print(childdiv)
#
# for chd in divchild:
#     print("!"*30)
#     print(chd)      # 줄바꿈도 자식처리해서 빈칸이 추출.
# print(div.descendants)
# divdes= div.descendants
# for c in divdes:
#     print("@"*30)
#     print(c)

# 아이디가 link2인 a의 형제 찾기
a= dom.find(id='link2')
anext = a.next_siblings
print(anext)
for temp in anext:
    print(temp)
    print('#'*30)


#os.path.join()
