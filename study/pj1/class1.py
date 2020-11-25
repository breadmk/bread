# class 클래스명:
#     메서드
#     메서드

# class Car:
#     def __init__(self,t,c):   # 생성자
#         print('생성자')
#         self.type=t
#         self.color=c
#     def showInfo(self):
#         print(self.type+','+self.color)
#     def tuning(self,c):
#         self.color=c
#         self.showInfo()     # 내가 가진 함수에 접근할때도 self 입력
    # def __del__(self):
    #     print('소멸자')


# c1 = Car('suv','쥐색')
# c1.showInfo()
# c1.tuning('흰색')

#------ 다중 상속 -----------------------------------------------------


# class X(object):
#     pass
# class Y:
#     pass
# class Z():
#     pass
# # 아무것도 안 쓸 경우 자바와 동일하게 Object 클래스를 상속 받는다.  괄호만 넣음 된다.
# # print('상속관계:', X.mro())
# # print('상속관계:', Y.mro())
# # print('상속관계:', Z.mro())
#
# class A(X,Y):
#     pass
# class B(Y,Z):
#     pass
# class C(A,B,Z):
#     pass
# #상속관계: [<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>]
# print('상속관계:', A.mro())
# #상속관계: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.B'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
# print('상속관계:', C.mro())
# # 너무 복잡한 다중상속은 코드 해석이 어려움 // 다중 상속이 가능하다는 걸 보여주는 거 뿐; 자바는 해당사항 없음;


#------------ 상속 연습 --------------------------------
#
# class Car:
#     def __init__(self,type,color):
#         self.type=type
#         self.color=color
#     def show(self):
#         print('Car class show method', self.type,self.color)
#
# class KiaCar(Car):
#     def __init__(self,carname,type,color):   # 생성자
#         super().__init__(type,color)    # 부모생성자 호출
#         self.carname = carname
#     def show(self):
#         print('KiaCar class show 메서드',self.carname,self.type,self.color)
#     def turning(self,color):
#         self.color=color
#
# class HyundaiCar(Car):
#     def __init__(self,carname,type,color):
#         super().__init__(type,color)
#         self.carname = carname
# k1=KiaCar('k9','세단','검정')   # 객체생성.
# k1.show()
# k1.turning('빨강')
# k1.show()               # 인스턴스 메서드 호출
# print(k1.carname)       # 객체 속성접근
#
# h1 = HyundaiCar('제네시스','세단','쥐색');
# h1.show()

# 파이썬에서는 생성자는 무조건 호출해줘야함 상속의 경우는 무조건 부모 생성자 생성;;;;;;

