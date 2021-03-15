#1) 함수정의
# def 함수명(매개변수):
#     내용
# 2)함수호출
# 함수명(매개변수)
# f1('kim')  함수는 정의후 사용
def f1(name):
    print('hi~'+name)
# f1('kim')
# print(f1('lee'))
def f2(name):
    return 'hi~ '+name
# print(f2('lee'))

def f3(x):
    y1=x*2
    y2=x*20
    y3=x*30
    return y1,y2,y3
# a,b,c=10,20,30
# r1,r2,r3=f3(7)
# print(r1,r2,r3)
# r1=f3(70)   #튜플
# print(r1)
# print(list(r1))
def f4(x):
    y1=x*2
    y2=x*20
    y3=x*30
    return [y1,y2,y3]
# r1=f4(8)
# print(r1)
# r1,r2,r3=f4(8)
# print(r1,r2,r3)
def f5(x):
    y1=x*2
    y2=x*20
    y3=x*30
    return {'y1':y1,'y2':y2,'y3':y3}
# r1=f5(8)
# print(r1)
# print(r1.keys(),r1.values())
# print(r1.items())
def f6(x,y):
    print('f6실행중')
    print(x,y)
# f6(3,4)
# f6(3,4,5)  오류
def f7(x=1,y=2,z=3):
    print(x,y,z)
# f7(10,20,30)
# f7()
# f7(11,22)
# f7(110)
# f7(z=99)
# def f8(x=1,y=2,z):   오류
#     print(x,y,z)
def f9(x,y,z=3):
    print(x,y,z)
# f9() err
# f9(1) err
# f9(10,20)
# f9(10,20,30)
# 가변인수 : *, **
def f10(*args):
    print(args)
    print(type(args))
    hap=0
    for i in args:
        hap=hap+i
    print('hap=',hap)
# f10()
# f10(1,2,3)
# f10(1,2,3,4,5)
# # f10('one','two')   숫자와 문자의 + 오류
def f11(**args):   #딕션어리로 매개변수 받을경우
    print(args)
    print(type(args))

# f11('a','b','c')
f11(name='kim',addr='pusan',age=10)


