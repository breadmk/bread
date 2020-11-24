# 작업스케쥴러를 통해서 실행파일exe 실행하여 주기적으로 자료수집
# 절대경로를 사용해야 오류가 나지 않는다 주의!
# D:\study\pj1\dist\sport.exe 만들어주고
# 작업스케쥴러에서 설정으로 생성해주기.

import requests
import json
#  제이슨 문서 연습
# with open('d:\\study\\pj1\\data\\sports.csv',mode='a',encoding='utf-8')as f:
#     url='https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
#     res = requests.get(url)
#     dic=json.loads(res.text)
#     for i in dic['list']:
#         str='{}::{}\n'.format(i['title'],i['subContent'])
#         print(str)
#         f.write(str)

# ↘↘↘↘↘↘ pip install 뒤에 설치하고 싶은 파일명 해서 terminal 에 입력
# (venv) D:\study\pj1>pip install pyinstaller

# ↘↘↘↘↘↘ D:\study\pj1\dist\sport <- 폴더나오고 엄청 많은 파일 존재
# (venv) D:\study\pj1>pyinstaller sports.py

# ↘↘↘↘↘↘ 하나의 exe 파일로 만들기. D:\study\pj1\dist\sport.exe
# (venv) D:\study\pj1>pyinstaller --onefile sports.py

# with open('d:\\study\\pj1\\data\\mlb.csv',mode='a',encoding='utf-8')as f:
#     url='https://sports.news.naver.com/wbaseball/index.nhn'
#     res = requests.get(url)
#     # dic=json.loads(res.text)
#     print(res.text)
    # for i in dic['list']:
    #     str='{}::{}\n'.format(i['title'],i['subContent'])
    #     print(str)
    #     f.write(str)
