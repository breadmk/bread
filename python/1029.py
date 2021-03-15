# a=[1,5,3,1,2,3,4,5]
# print(a)
# print(len(a))
# print(a.count(5))
# a.append('seven')
# print(a)
# a.append(['one','two','three'])
# print(a)
# a.insert(3,'*')  #a.insert(인덱스,값)
# print(a)
# print(a[9])
# a[3]='!'
# print(a)
# a.remove(5)  #리스트의 처음나타나는 5를 삭제
# print(a)
# a.remove(5)
# print(a)
# del a[:3]  #a 리스트의 0번째부터 2번째까지 삭제
# print(a)
# del a  #객체삭제
# # print(a)
a=['zero','one','two','three','four','five']
# for 변수 in 반복가능객체:
#     내용
# for i in a:   #i='zero','one','two','three'
#     print(i)
# range(시작,종료(<),증감)
# print(range(1,10,1))
# print(list(range(1,10,1)))
# print(tuple(range(1,10,1)))
# for i in range(6):   #i=0,1,2,3,4,5
#     print(i,a[i])
# for i in range(len(a)) :
#     print(i,a[i])

# for i in range(5): #종료값, 시작값생략시 0 ,증감생략시 1
#     print(i)
# # 1-100 숫자 출력
# for i in range(1,101):
#     print(i,end=' ')
# print()
# for i in range(3,1000,3):
#     print(i, end=' ')
# print()
# a=[0,1,2,....100]
# for i in range(101):
#     print(i)
# 컴프리핸션
a=[i for i in range(101)]
print(a)
# b=[7,7,....7]
# for i in range(100):
#     print(7)
# b=[7 for i in range(100)]
# print(b)
# print(len(b))
# print('-'*30)
# c=[]
# for i in range(100):
#     c.append(7)
# print(c)
print('-'*30)
# c=[1,3,5,...99]
# d=['good','good',..]
c=[i for i in range(1,100,2)]
# d=['good' for i in range(5)] #i값이 사용되지 않아 의미를 약화시킴
d=['good' for _ in range(5)]
print(c)
print(d)
e=['good'+str(i) for i in range(5)]
print(e)


# 형변환
# b='3'
# print(type(b))
# print(int(b),type(int(b)))


print('\n\n\n\n\n\n\n\n\n\n\n')






