import os
import glob

# def f1(n):
#     return n*10

# print(f1(4))
# a=f1
# print(type(a))
# print(a(10))

# -------------------------------- 람다함수 ------------------------------------------
# 람다함수 : 메모리절약, 가독성 향상, 코드 간결.

# 형식 )))) lambda 매개변수:반환값
# b=lambda n:n*10

# print(b(20))

# def f2(x,y,f):
#     print(x*y*f(x+y))
# f2(10,100,lambda n:n+1)

#-----------------------------------------------------

# a=[1,2,3,4,5]  # ==>[3,6,9,12,15]
#
# def f3(n):
#     result =[]
#     for i in n:
#         result.append(i*3)
#     return result

# print(f3(a))

#------------------------------ map 함수 ---------------------

# map() : 매개변수로 함수와 반복가능 객체를 입력
#  형식))) map(함수,반복가능객체)
# def f4(x):
#     return x*3
# print(f4(7))
# print(f4([1,2,3]))      # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(map(f4,[1,2,3]))  # map객체 <map object at 0x000000ABFD9B6588>
# print(list(map(f4,[1,2,3])))                #[3, 6, 9]
# print(list(map(lambda n:n*4,[1,2,3])))      #[4, 8, 12]
# print(list(map(lambda n:n/4,[4,8,12])))         # [1.0, 2.0, 3.0]
# print(list(map(int,list(map(lambda n:n/4,[4,8,12])))))  #[1, 2, 3]

#--------------------------------------------------------------
# 파일경로 리눅스,맥에서는 /
#               윈도우 \

# os모듈 : 디렉토리, 파일등의 os자원 제어
# glob모듈


# print('현재 작업디렉토리',os.getcwd())  #current working directory
# print('현재 작업디렉토리의 목록',os.listdir())
# print('d:\목록',os.listdir('d:\\'))
# print(os.listdir('d:\\down\\erd'))  # 목록보기
# # print(os.path.join('..','test1'))   # 경로생성
# print(os.listdir(os.path.join('..','test1')))
# print(os.path.join('..','test1','Scripts'))    # OS 환경이 다를 경우를 생각해서 사용한다. 윈도우\\ 리눅스/ 다르기 때문에.

# with open('data\\webtoon.csv',mode='w',encoding='utf-8') as f:
# with open(os.path.join('data',webtoon.csv'),mode='w',encoding='utf-8') as f:



# print(glob.glob('*'))       # 경로에 있는 것을 다 보겠다.
# print(glob.glob('*.py'))    # 경로에 있는 파일중에 확장자가 .py 인 것만 보겠다.

# f1='D:\\study\\pj1\\data\\Beauty.smi'
# print(os.path.dirname(f1))      # 폴더명
# print(os.path.basename(f1))     # 가장 마지막에 있는 이름(파일,디렉토리 모두)

#-----------------------------------------------------------------------------

# f=open(os.path.join('data','Beauty.smi'))
# print(f.read())
# print(f.readline())     # 1줄 읽고 끝
# print(f.readlines())    # 전체 다 읽을때
# f.close()

# -----------------------------------------------------
# f=open(os.path.join('data','Beauty.smi'))
#
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line,end="")
# f.close()

# -----------------------------------------------------
# ---------------- data 폴더에 있는 파일 내용 출력 ---------------------

# filelist = glob.glob(os.path.join('data','*'))      # 반환형 list
# print(filelist)
#
# for file in filelist:
#     with open(file,encoding='utf-8') as f:
#         print(os.path.basename(file))
#         if os.path.basename(file)!='io2.py':
#             print(f.read())
#             print('-'*30)

# 'Beauty.smi' --> [자막만]-->'Beauty.txt'

inputFile='data\\Beauty.smi'

def makeTxt(inputFile):

    f=open(inputFile,encoding='utf-8')
    result=[]
    for line in f:
        line=line.replace('\n','')
        if len(line)<4:
            continue
        elif line.count(':')>3:
            continue
        line=line.replace('<b>','')
        line=line.replace('</b>','')
        line = line.replace('<i>', '')
        line = line.replace('</i>', '')
        # print(line)
        result.append(line)
        # print(line.count(':'))
    f.close()
    return result

# print(result)
#-------------------------------------------------------
inputFile='data\\Beauty.smi'
def makeFile(inputFile,temp):
    filename=inputFile[:-3]+'txt'
    # print(filename)
    with open(filename,mode='w',encoding='utf-8')as fw:
        for t in temp:
            fw.write(t+'\n')

def main():
    inputFile='data\\Beauty.smi'
    temp=makeTxt(inputFile)
    makeFile(inputFile,temp)
if __name__=='__main__':
    main()

# with open(inputFile,encoding='utf-8') as f:












