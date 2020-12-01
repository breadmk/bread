import logging
import os
# 프로그램 운영시 중요한 부분을 로그로 남기는것, 단순한 에러인지, 출력인지 등을 관리하는 모듈
# logging.debug('DEBUG')         # 필요한 정보를 기록
# logging.info('INFO')          # 정보알림
# logging.warning('WARNING')       # 작동은 하지만 예상치 못한일이 발생할 것으로 예측
# logging.error('ERROR')         # 에러
# logging.critical('CRITICAL')      # 심각한 오휴

# 1) 로거 생성 logging.getLogger('테스트명')
logger=logging.getLogger('1차테스트')
# 1-1) 레벨설정
logger.setLevel(logging.DEBUG)
# 2) 파일핸들러 생성 logging.FileHandler(self, filename, mode='a', encoding=None, delay=False)
f1 = logging.FileHandler('data\\default.log',encoding='utf-8')
f2 = logging.FileHandler('data\\secret.log',encoding='utf-8')
# 2-1) 레벨설정
f1.setLevel(logging.WARNING) # f1는 워닐부터 보겠다.
f2.setLevel(logging.DEBUG) # f2는 디버그부터 보겠다.
logger.addHandler(f1)
logger.addHandler(f2)
# 3) 포매터 생성
# print('%s,%s,%s',name,age,birth) 아래에 - 으로 연결해서 이어줌;

fomatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s') # 첫번째 %s는 시간 , %s 레벨네임, %s 메세지
f1.setFormatter(fomatter)
f2.setFormatter(fomatter)
print(3)
logger.debug('DEBUG')
logger.info('INFO')
logger.warning('WARNING')
logger.error('ERROR')
logger.critical('CRITICAL')

