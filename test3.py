# test3.py
# 공공 데이터 포털 (http://www.data.go.kr) 에서 csv 파일 다운받기
# csv 파일을 읽어 들여서, 읽어 들인 데이터에서 가장 많이 사용된 명사 찾기

import codecs
import csv
from konlpy. tag import Okt

from test2 import mal_list # 다른 py 파일의 리스트 임포트함

okt = Okt()
word_dic={}
lines=[]

# 파일변수 = open('파일명.확장자', '열기모드')
# 파일변수.read(), 파일변수.write()
# 파일 처리가 끝나면 반드시 파일변수.close()

# csv 파일에서 데이터 읽어 들이기: codecs 모듈이 제공하는 함수 이용
# 파일 입출력이 끝나면, 자동 close 되게 하려면 with resource 문 사용하면 됨
with open('./data/sample2.csv') as raws: # 파일변수가 rasw 임
    reader = csv.reader(raws)  #csv 파일 읽기용 객체
    for row in reader:  # reader 를 통해서 한 줄씩 문장 읽어들이기
        lines.append(row) # 한 줄씩 리스트에 저장
        # print(row)

# with --------------------------------------------

# 저장 구조 : [[...],[.....],[.......]]
for line in lines:
    # print(''.join(line))  # '구분자'.join(리스트) -> str: 리스트 안의 값들을 공백으로 구분해서 하나의 문자열로 반환
    mal_list = okt.pos(''.join(line))
    print(mal_list)
