# n=int(input('숫자(1-4)='))
# if n==1:
#     print('안녕')
# elif n==2:
#     print('안녕')
#     print('안녕')
# elif n==3:
#     print('안녕')
#     print('안녕')
#     print('안녕')
# else:
#     print('안녕')
#     print('안녕')
#     print('안녕')
#     print('안녕')
# a=['안녕','안녕',....]
# n=int(input('숫자='))
# # a=[]
# # for i in range(n):
# #     a.append('안녕')
# # print(a)
# a=['안녕' for i in range(n)]
# print(a)
# b=[]
# # 1-20홀수중 3의배수인 것만 b에 넣으세요
# for i in range(1,21,2):
#     if i%3==0:
#         b.append(i)
# print(b)
# -->컴프리핸션:컬렉션을 만드는 한줄짜리 반복문
# b=[i for i in range(1,21,2) if i%3==0]
# print(b)
#튜플:변경X, 사용법은 리스트와 같다
#    파이썬이 주로 사용한다. 매개변수전달시, 반환값 전달시
# a=('감','사과','대추')
# print(a,type(a))
# for i in a:
#     print(i)
# print(a[2])
# # a[2]='복수박'
# print(a,type(a))
# a=('빨강','파랑','노랑','초록')
# # 인덱스와 같이 출력
# for i in enumerate(a):
#     print(i)
# print('-'*30)
# for i,v in enumerate(a):
#     print(i,v)
# a,b,c=1,'two','셋'
# print(a,b,c)
# a=1,'two','셋'
# print(a)
# print(a[0],a[1],a[2])
# a,b=3      err
# print(a,b)
# a=range(10)
# print(a)
# print(list(a))
# print(tuple(a))
# 딕션어리{}
# 순서X,키와 값 셋트, 키는 중복X
# 값은 중복가능
# friend={'name':'kim','age':20,1004:'yes'}
# print(friend)
# print(type(friend))
# print(friend['age'])
# print(friend[1004])
# print('-'*30)
# for i in friend:
#     # print(i)
#     print(i,friend[i])
# print(friend.values())  #리스트로 반환
# print(friend.keys())  #리스트로 반환
# for i in friend.items():   #키와 값 반환
#     print(i)
# for i,v in friend.items():
#     print(i,v)
a='javascript'
# for i in a:
#     print(i)
# r=[i for i in a]
# print(r)
for i in enumerate(a):
    print(i)
# r={}
# for i in enumerate(a):
#     # print(i)
#     # r[i[0]]=i[1]
#     r[i[1]]=i[0]
# print(r)
r={i[1]:i[0] for i in enumerate(a)}
print(r)
print('\n\n\n\n\n\n\n\n')


