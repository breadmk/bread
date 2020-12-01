# import basic
# def hap(n):
#     basic.logger.info('hap함수 호출')
#     h=0
#     for i in range(n+1):
#         h=h+i
#         if h>1000:
#             basic.logger.critical("합이 1000을 초과"+str(i)+","+str(h))
#     return h
#
# print(hap(10))
# print(hap(100))

# ----------- 예외처리 ---------------------------
# try:
#     예외가 발생할 가능성이 있는 코드
# except 예외명1:
#     코드
# except 예외명2:
#     코드
# else:    #예외가 없을 경우 실행
#     코드
# finally:
#     코드

# names = ["kim",'lee','park']
# try:
#     i='lee'
#     i2='choi'
#     print(names.index(i))   # 1 => 첫 번째 자리에 있다.
#     # print(names.index(i2))
# except:
#     print("예외발생")       # 예외가 없어서 pass 처리됨.
# else:
#     print('ok')             # 예외가 없어서 ok 출력
# finally:
#     print('무조건실행')      # 무조건 출력

# names = ["kim",'lee','park']
# try:
#     x=[1,2]
#     y='test'
#     z=x+y
# except ValueError:
#     print("해당값이 리스트에 없음")
# except TypeError:
#     print("리스트와 문자열을 연결못함")
# else:
#     print('ok')
# finally:
#     print('무조건실행')

# 제너레이터--------------------------
n=[1,2,3,4,5]
rn=reversed(n)
# print(rn)
# 이터러블 : 리스트, 문자열, 튜플,딕션어리 처럼 요소를 차례차례 꺼낼 수 있는 객체
# for c in 'python':
#     print(c)
# 이터레이터: 이터러블 중에서 next() 함수를 사용해서 하나하나 꺼낼 수 있는 객체
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# for i in rn:
#     print(i)

# def test():
#     print("test 함수 호출")
#     yield 'test'
#
# print('a')
# test()
#
# print('b')
# test()
#
# print(test())
# test()

# 제너레이터 함수 : 제너레이터를 리턴하는 함수
# 제너레이터 next()함수를 이용하여 함수의 내부 코드 실행

def test1():
    print('one')
    yield 11
    print('two')
    yield 22
    print('three')
    yield 33
# yield 는 한번 호출되고 끝나는게 아니라 남아서 계속 활용할 수 있음.
# r1=test1()
# print('four')
# r2=next(test1())
# print(r2)
# r2=next(test1())
# print(r2)
# for i in test1():
#     print(i)
#     print()

# 아나콘다 설치, 가상환경 설정, 스크래피 설정, 쥬피터노트북 사용법
# https://copycoding.tistory.com/60
# 가상환경 pj3 생성