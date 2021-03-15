# people={"name":"둘리","age":"1억살","addr":"쌍문동"}
# print(people)
# print(type(people))
# print(people["age"])
# people['1004']='yes'  #추가
# print(people)
# del people['age']  #삭제
# print(people)
# people['1004']='no' #변경
# for i in people:
#     print(i)
# for i in people.items():
#     print(i)
# for i,v in people.items():
#     print(i,v)
# print(people.keys())
# print(people.values())
# set {}
# a={2,5,3,5,8,2}
# print(a)
# print(type(a))
# b=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
# print(b)
# print(set(b))
# a.add(11)   #추가
# print(a)
# a.update([13,5,17])
# print(a)
# a.remove(2)
# print(a)
#
# people.clear()
# print(people)
# 정규표현식
# ?	0 or 1
# *	0번 이상
# +	1번 이상
# {최소값,최대값}
# . 글자1개, 줄바꿈 제외
# [^ ]	부정
# ^ 시작
# {3}
# {3,}
# {,3}
# | 선택
# [a-zA-Z0-9%^&*()]
# \s 공백
a='''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''
import re   #정규식 사용
# re.findall(r'정규식',문자열)
r1=re.findall(r'[0-9]',a)
print(r1)
r1=re.findall(r'[0-9]+',a)
print(r1)
r1=re.findall(r'[A-Za-z]+',a)
print(r1)
# T로 시작하지 않는 이름 찾기
r1=re.findall(r'[A-SU-Z][a-z]+',a)
print(r1)

print('\n\n\n\n\n\n\n\n\n')