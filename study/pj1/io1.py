# open('파일명',모드)
# 사용
# 변수.close()    | 자원 반납
# 모두 : r(읽기),w(쓰기),a(추가)//append

# # f=open('d:\study\pj1\data\poem.txt','r',encoding='UTF-8') //절대경로
# f=open('data\poem.txt','r',encoding='UTF-8')        #상대경로
# # txt=f.read()  //전체 내용 읽기
# txt=f.read(7)    #5글자 읽기
# print(txt)
# print(type(txt))
# f.close()

# print('-'*30)
#
# f=open('data\\poem.txt',encoding='UTF-8')
# txt=f.readline()  #한줄읽기
# print(txt)
# print(type(txt))     #문자열
# f.close()


# print('-'*30)

# f=open('data\\poem.txt',encoding='UTF-8')
# txt=f.readlines()   #줄단위 리스트 반환 //한줄씩 다 읽기. 김인육 / ['사랑의 물리학\n' ...'첫사랑이었다.\n']
# print(txt)
# for line in txt:
#     # print(line,end='')
#     print(line.strip())
# f.close()
# with open('파일명',모드) as 변수명:
#   with 블럭이 끝날때 자동 close
# with open('data\\poem.txt',encoding='utf-8') as f:
#     txt=f.read()
#     print(txt)
# print('-'*30)

# with open('data\\test1.txt','w',encoding='utf-8')as f:
#     f.write('today is monday\n')
#     f.write('홍준씨 연락왔어요?')
# print('-'*30)

# with open('data\\test2.txt',mode='a',encoding='utf-8')as f:    #필수 작성코드는 앞쪽에 작성. 'a'
#     for i in range(100):
#         f.write(str(i)+'\n')
# 없으면 만들고, 있으면 추가하는게 mode='a'

# with open('data\\test1.txt',encoding='utf-8') as f1:
#     print(f1.read())

# print('-'*30)

# fruit=['사과','배','포도']
# with open('data\\test2.txt',mode='a',encoding='utf-8') as f:
#     # for a in fruit:
#     #     f.write(a)
#     f.writelines(fruit) #리스트를 파일에 쓰기. 위랑 같은 코드
# print('-'*30)

# with open('data\\test1.txt',mode='w',encoding='utf-8')as f:
#     print('test print',file=f)
# print('-'*30)

col=['이름','나이','주소']
names=['홍길동','심청','이몽룡','성춘향']
age=[20,16,16,16]
juso=['서울','서산','남원','진주']

# with open('data\\addr.txt',mode='w',encoding='utf-8')as f:
#     f.write(','.join(col)+'\n')     #join 함수
#     for i in range(len(names)): #i=0,1,2,3
#         str='{},{},{}\n'.format(names[i],age[i],juso[i])
#         # print(str)    # 줄바꿈 잘됨.   \n 안 넣어도됨.
#         f.write(str)    # 줄바꿈 안됨. \n 직접추가.
# print('-'*30)
#
# a=['one','two','three','four']
# # '연결문자'.join(리스트 or 튜플)
# print('-'.join(a))
# print('연결할거야!'.join(a))
# print(type(a))
#
# b=('원','투','쓰리')
# print('-'.join(b))
# print(type(b))
# print('-'*30)

### 이미지 저장 ###

# 이미지 저장 (https://movie-phinf.pstatic.net/20201104_45/160445535053439akc_JPEG/movie_image.jpg)

import requests # 웹서버에 접근
url='https://movie-phinf.pstatic.net/20201104_45/160445535053439akc_JPEG/movie_image.jpg'
recived=requests.get(url)
print(recived)  #<Response [200]> : 접근성공.
with open('img\\movie.jpg',mode='wb')as f:  # 이미지는 이진파일이라 wb:binary
    f.write(recived.content)


























